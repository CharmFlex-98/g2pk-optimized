# -*- coding: utf-8 -*-
'''
https://github.com/kyubyong/g2pK
'''

import os, re

import nltk
import mecab
from jamo import h2j
from nltk.corpus import cmudict

# For further info. about cmu dict, consult http://www.speech.cs.cmu.edu/cgi-bin/cmudict.
try:
    nltk.data.find('corpora/cmudict.zip')
except LookupError:
    nltk.download('cmudict')

from g2pk.special import jyeo, ye, consonant_ui, josa_ui, vowel_ui, jamo, rieulgiyeok, rieulbieub, verb_nieun, balb, palatalize, modifying_rieul
from g2pk.regular import link1, link2, link3, link4
from g2pk.utils import annotate, compose, group, gloss, parse_table, get_rule_id2text
from g2pk.english import convert_eng
from g2pk.numerals import convert_num


class G2p(object):
    def __init__(self):
        self.mecab = self.get_mecab()
        self.table = parse_table()

        self.cmu = cmudict.dict() # for English

        self.rule2text = get_rule_id2text() # for comments of main rules
        self.idioms_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "idioms.txt")

    def get_mecab(self):
        try:
            return mecab.MeCab(dictionary_path='/usr/local/lib/mecab/dic/mecab-ko-dic')
        except Exception as e:
            raise Exception(
                'If you want to install mecab, The command is... pip install python-mecab-ko'
            )

    def idioms(self, string, descriptive=False, verbose=False, applied_rules=None):
        '''Process each line in `idioms.txt`
        Each line is delimited by "===",
        and the left string is replaced by the right one.
        inp: input string.
        descriptive: not used.
        verbose: boolean.

        >>> idioms("지금 mp3 파일을 다운받고 있어요")
        지금 엠피쓰리 파일을 다운받고 있어요
        '''
        current_rule_id = None
        out = string

        for raw_line in open(self.idioms_path, 'r', encoding="utf8"):
            raw_line = raw_line.strip()
            if raw_line.startswith("# rule:"):
                current_rule_id = raw_line[len("# rule:"):].strip()
                continue
            line = raw_line.split("#")[0].strip()
            if "===" in line:
                str1, str2 = line.split("===")
                _out = re.sub(str1, str2, out)
                if applied_rules is not None and _out != out and current_rule_id is not None:
                    applied_rules.append({
                        "rule_id": current_rule_id,
                        "before": out,
                        "after": _out,
                    })
                out = _out

        return out

    def __call__(self, string, descriptive=False, verbose=False, group_vowels=False, to_syl=True):
        '''Main function
        string: input string
        descriptive: boolean.
        verbose: boolean. If True, returns (output, applied_rules) where applied_rules is a list
                 of dicts with keys: rule_id, before, after.
        group_vowels: boolean. If True, the vowels of the identical sound are normalized.
        to_syl: boolean. If True, hangul letters or jamo are assembled to form syllables.

        For example, given an input string "나의 친구가 mp3 file 3개를 다운받고 있다",
        STEP 1. idioms
        -> 나의 친구가 엠피쓰리 file 3개를 다운받고 있다

        STEP 2. English to Hangul
        -> 나의 친구가 엠피쓰리 파일 3개를 다운받고 있다

        STEP 3. annotate
        -> 나의/J 친구가 엠피쓰리 파일 3개/B를 다운받고 있다

        STEP 4. Spell out arabic numbers
        -> 나의/J 친구가 엠피쓰리 파일 세개/B를 다운받고 있다

        STEP 5. decompose
        -> 나의/J 친구가 엠피쓰리 파일 세개/B를 다운받고 있다

        STEP 6-9. Hangul
        -> 나의 친구가 엠피쓰리 파일 세개를 다운받꼬 읻따
        '''
        applied_rules = [] if verbose else None

        # 1. idioms
        string = self.idioms(string, descriptive, verbose, applied_rules)

        # 2 English to Hangul
        string = convert_eng(string, self.cmu)

        # 3. annotate
        string = annotate(string, self.mecab)

        # 4. Spell out arabic numbers
        string = convert_num(string)

        # 5. decompose
        inp = h2j(string)

        # 6. special
        for func in (jyeo, ye, consonant_ui, josa_ui, vowel_ui, \
                     jamo, rieulgiyeok, rieulbieub, verb_nieun, \
                     balb, palatalize, modifying_rieul):
            inp = func(inp, descriptive, verbose, applied_rules)
        inp = re.sub("/[PJEB]", "", inp)

        # 7. regular table: batchim + onset
        for str1, str2, rule_ids in self.table:
            _inp = inp
            inp = re.sub(str1, str2, inp)

            for rule_id in rule_ids:
                gloss(verbose, inp, _inp, rule_id, applied_rules)

        # 8 link
        for func in (link1, link2, link3, link4):
            inp = func(inp, descriptive, verbose, applied_rules)

        # 9. postprocessing
        if group_vowels:
            inp = group(inp)

        if to_syl:
            inp = compose(inp)

        if verbose:
            return inp, applied_rules
        return inp

if __name__ == "__main__":
    g2p = G2p()
    g2p("나의 친구가 mp3 file 3개를 다운받고 있다")
