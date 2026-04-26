import re
from jamo import h2j, j2h
import os

############## English ##############
def adjust(arpabets):
    '''Modify arpabets so that it fits our processes'''
    string = " " + " ".join(arpabets) + " $"
    string = re.sub("\d", "", string)
    string = string.replace(" T S ", " TS ")
    string = string.replace(" D Z ", " DZ ")
    string = string.replace(" AW ER ", " AWER ")
    string = string.replace(" IH R $", " IH ER ")
    string = string.replace(" EH R $", " EH ER ")
    string = string.replace(" $", "")

    return string.strip("$ ").split()


def to_choseong(arpabet):
    '''Arpabet to choseong or onset'''
    d = \
        {'B': 'ᄇ',
         'CH': 'ᄎ',
         'D': 'ᄃ',
         'DH': 'ᄃ',
         'DZ': 'ᄌ',
         'F': 'ᄑ',
         'G': 'ᄀ',
         'HH': 'ᄒ',
         'JH': 'ᄌ',
         'K': 'ᄏ',
         'L': 'ᄅ',
         'M': 'ᄆ',
         'N': 'ᄂ',
         'NG': 'ᄋ',
         'P': 'ᄑ',
         'R': 'ᄅ',
         'S': 'ᄉ',
         'SH': 'ᄉ',
         'T': 'ᄐ',
         'TH': 'ᄉ',
         'TS': 'ᄎ',
         'V': 'ᄇ',
         'W': 'W',
         'Y': 'Y',
         'Z': 'ᄌ',
         'ZH': 'ᄌ'}

    return d.get(arpabet, arpabet)

def to_jungseong(arpabet):
    '''Arpabet to jungseong or vowel'''
    d = \
        {'AA': 'ᅡ',
         'AE': 'ᅢ',
         'AH': 'ᅥ',
         'AO': 'ᅩ',
         'AW': 'ᅡ우',
         'AWER': "ᅡ워",
         'AY': 'ᅡ이',
         'EH': 'ᅦ',
         'ER': 'ᅥ',
         'EY': 'ᅦ이',
         'IH': 'ᅵ',
         'IY': 'ᅵ',
         'OW': 'ᅩ',
         'OY': 'ᅩ이',
         'UH': 'ᅮ',
         'UW': 'ᅮ'}
    return d.get(arpabet, arpabet)

def to_jongseong(arpabet):
    '''Arpabet to jongseong or coda'''
    d = \
        {'B': 'ᆸ',
         'CH': 'ᆾ',
         'D': 'ᆮ',
         'DH': 'ᆮ',
         'F': 'ᇁ',
         'G': 'ᆨ',
         'HH': 'ᇂ',
         'JH': 'ᆽ',
         'K': 'ᆨ',
         'L': 'ᆯ',
         'M': 'ᆷ',
         'N': 'ᆫ',
         'NG': 'ᆼ',
         'P': 'ᆸ',
         'R': 'ᆯ',
         'S': 'ᆺ',
         'SH': 'ᆺ',
         'T': 'ᆺ',
         'TH': 'ᆺ',
         'V': 'ᆸ',
         'W': 'ᆼ',
         'Y': 'ᆼ',
         'Z': 'ᆽ',
         'ZH': 'ᆽ'}

    return d.get(arpabet, arpabet)


def reconstruct(string):
    '''Some postprocessing rules'''
    pairs = [("그W", "ᄀW"),
             ("흐W", "ᄒW"),
             ("크W", "ᄏW"),
             ("ᄂYᅥ", "니어"),
             ("ᄃYᅥ", "디어"),
             ("ᄅYᅥ", "리어"),
             ("Yᅵ", "ᅵ"),
             ("Yᅡ", "ᅣ"),
             ("Yᅢ", "ᅤ"),
             ("Yᅥ", "ᅧ"),
             ("Yᅦ", "ᅨ"),
             ("Yᅩ", "ᅭ"),
             ("Yᅮ", "ᅲ"),
             ("Wᅡ", "ᅪ"),
             ("Wᅢ", "ᅫ"),
             ("Wᅥ", "ᅯ"),
             ("Wᅩ", "ᅯ"),
             ("Wᅮ", "ᅮ"),
             ("Wᅦ", "ᅰ"),
             ("Wᅵ", "ᅱ"),
             ("ᅳᅵ", "ᅴ"),
             ("Y", "ᅵ"),
             ("W", "ᅮ")
             ]
    for str1, str2 in pairs:
        string = string.replace(str1, str2)
    return string


############## Hangul ##############
def parse_table():
    '''Parse the main rule table'''
    lines = open(os.path.dirname(os.path.abspath(__file__)) + '/table.csv', 'r', encoding='utf8').read().splitlines()
    onsets = lines[0].split(",")
    table = []
    for line in lines[1:]:
        cols = line.split(",")
        coda = cols[0]
        for i, onset in enumerate(onsets):
            cell = cols[i]
            if len(cell)==0: continue
            if i==0:
                continue
            else:
                str1 = f"{coda}{onset}"
                if "(" in cell:
                    str2 = cell.split("(")[0]
                    rule_ids = cell.split("(")[1][:-1].split("/")
                else:
                    str2 = cell
                    rule_ids = []

                table.append((str1, str2, rule_ids))
    return table


############## Preprocessing ##############
def annotate(string, mecab):
    '''attach pos tags to the given string using Mecab
    mecab: mecab object
    '''
    morphs = list(mecab.parse(string))
    if string.replace(" ", "") != "".join(m.surface for m in morphs):
        return string

    blanks = [i for i, char in enumerate(string) if char == " "]

    # Build character-level POS tag sequence from parse results
    tag_seq = []
    for morph in morphs:
        tag = morph.feature.pos.split("+")[-1]
        if tag == "NNBC":
            tag = "B"
        else:
            tag = tag[0]
        tag_seq.append("_" * (len(morph.surface) - 1) + tag)
    tag_seq = "".join(tag_seq)

    for i in blanks:
        tag_seq = tag_seq[:i] + " " + tag_seq[i:]

    _RULE15_VOWELS = frozenset('\u1161\u1165\u1169\u116e\u1171')
    _CONTENT_POS = frozenset('NVMI')

    def _qualifies(tok, tag_raw):
        tag = tag_raw.split('+')[-1]
        pos = 'B' if tag == 'NNBC' else tag[0]
        if pos not in _CONTENT_POS or not tok:
            return False
        jamo = h2j(tok[0])
        return len(jamo) >= 2 and jamo[0] == '\u110b'

    # Single pass: collect /C positions for both cross-word and compound-internal
    # boundaries using the one parse result.
    c_positions = set()
    cursor = 0
    for i_morph, morph in enumerate(morphs):
        pos = string.find(morph.surface, cursor)
        if pos == -1:
            continue
        cursor = pos + len(morph.surface)
        tok_end = pos + len(morph.surface) - 1

        # Cross-word boundary: next token is a qualifying content morpheme
        if i_morph < len(morphs) - 1:
            next_morph = morphs[i_morph + 1]
            if _qualifies(next_morph.surface, next_morph.feature.pos) and len(h2j(string[tok_end])) >= 3:
                c_positions.add(tok_end)

        # Compound-internal boundary: scan expression parts for qualifying transitions
        if morph.feature.type == 'Compound':
            expression = morph.feature.expression
            if expression and '+' in expression:
                parts = expression.split('+')
                char_offset = pos
                for i_part, part_str in enumerate(parts[:-1]):
                    surf = part_str.split('/')[0]
                    next_str = parts[i_part + 1]
                    next_surf = next_str.split('/')[0]
                    next_pos_tag = next_str.split('/')[1] if len(next_str.split('/')) > 1 else 'X'
                    surf_end = char_offset + len(surf) - 1
                    if _qualifies(next_surf, next_pos_tag) and len(h2j(string[surf_end])) >= 3:
                        c_positions.add(surf_end)
                    char_offset += len(surf)

    annotated = ""
    for i, (char, tag) in enumerate(zip(string, tag_seq)):
        annotated += char
        if char == "의" and tag == "J":
            annotated += "/J"
        elif tag == "E":
            if h2j(char)[-1] in "ᆯ":
                annotated += "/E"
        elif tag == "V":
            if h2j(char)[-1] in "ᆫᆬᆷᆱᆰᆲᆴ":
                annotated += "/P"
        elif tag == "B":
            annotated += "/B"
        if i in c_positions:
            annotated += "/C"

    return annotated


############## Postprocessing ##############
def compose(letters):
    # insert placeholder
    letters = re.sub("(^|[^\u1100-\u1112])([\u1161-\u1175])", r"\1ᄋ\2", letters)

    string = letters # assembled characters
    # c+v+c
    syls = set(re.findall("[\u1100-\u1112][\u1161-\u1175][\u11A8-\u11C2]", string))
    for syl in syls:
        string = string.replace(syl, j2h(*syl))

    # c+v
    syls = set(re.findall("[\u1100-\u1112][\u1161-\u1175]", string))
    for syl in syls:
        string = string.replace(syl, j2h(*syl))

    return string


def group(inp):
    '''For group_vowels=True
    Contemporarily, Korean speakers don't distinguish some vowels.
    '''
    inp = inp.replace("ᅢ", "ᅦ")
    inp = inp.replace("ᅤ", "ᅨ")
    inp = inp.replace("ᅫ", "ᅬ")
    inp = inp.replace("ᅰ", "ᅬ")

    return inp


def _get_examples():
    '''For internal use'''
    text = open('rules.txt', 'r', encoding='utf8').read().splitlines()
    examples = []
    for line in text:
        if line.startswith("->"):
            examples.extend(re.findall("([ㄱ-힣][ ㄱ-힣]*)\[([ㄱ-힣][ ㄱ-힣]*)]", line))
    _examples = []
    for inp, gt in examples:
        for each in gt.split("/"):
            _examples.append((inp, each))

    return _examples


############## Utilities ##############
def get_rule_id2text():
    '''for verbose=True'''
    rules = open(os.path.dirname(os.path.abspath(__file__)) + '/rules.txt', 'r', encoding='utf8').read().strip().split("\n\n")
    rule_id2text = dict()
    for rule in rules:
        rule_id, texts = rule.splitlines()[0], rule.splitlines()[1:]
        rule_id2text[rule_id.strip()] = "\n".join(texts)
    return rule_id2text


def _strip_common_affixes(before, after):
    '''Strip common prefix and suffix characters, returning just the changed core.
    Falls back to (before, after) if stripping would leave an empty string.
    '''
    i = 0
    while i < len(before) and i < len(after) and before[i] == after[i]:
        i += 1
    j = 0
    while j < len(before) - i and j < len(after) - i and before[-(j+1)] == after[-(j+1)]:
        j += 1
    before_core = before[i: len(before) - j if j else len(before)]
    after_core = after[i: len(after) - j if j else len(after)]
    if not before_core or not after_core:
        return before, after
    return before_core, after_core


def _extract_word_changes(before, after):
    '''Compare two strings word-by-word and return per-word diffs.
    Returns: list of (before_word, after_word, [word_index])
    Each changed word is its own entry — no grouping of adjacent changes.
    Falls back to [(before, after, all_indices)] if word count changes.
    '''
    before_words = before.split(" ")
    after_words = after.split(" ")
    if len(before_words) != len(after_words):
        return [(before, after, list(range(len(before_words))))]
    changes = []
    for i in range(len(before_words)):
        if before_words[i] != after_words[i]:
            changes.append((before_words[i], after_words[i], [i]))
    return changes


def gloss(verbose, out, inp, rule_id, applied_rules=None):
    '''displays the process and relevant information'''
    if verbose and out != inp and out != re.sub("/[EJPBC]", "", inp):
        if applied_rules is not None:
            clean_inp = re.sub("/[EJPBC]", "", inp)
            clean_out = re.sub("/[EJPBC]", "", out)
            for before_word, after_word, indices in _extract_word_changes(compose(clean_inp), compose(clean_out)):
                applied_rules.append({
                    "rule_id": rule_id,
                    "before": before_word,
                    "after": after_word,
                    "word_indices": indices,
                })


_N_INSERTION_EXCEPTIONS = frozenset({'6·25', '3·1절', '송별연', '등용문'})
_N_INSERTION_PHRASE_EXCEPTIONS = frozenset({'송별 연', '등용 문'})
_YIOTIZED_VOWELS = frozenset({'ᅵ', 'ᅣ', 'ᅧ', 'ᅭ', 'ᅲ'})  # ᅵᅣᅧᅭᅲ
_JONGSEONG_START = 'ᆨ'  # ᆨ
_JONGSEONG_END = 'ᇂ'    # ᇂ
_NULL_ONSET = 'ᄋ'       # ᄋ
_RIEUL_JONGSEONG = 'ᆯ'  # ᆯ
_NIEUN_ONSET = 'ᄂ'      # ᄂ
_RIEUL_ONSET = 'ᄅ'      # ᄅ


def _apply_n_insertion_at_boundary(left_surf, right_surf):
    '''Returns modified right_surf with ᄋ replaced by ᄂ/ᄅ, or None if not applicable.'''
    left_jamo = h2j(left_surf)
    right_jamo = h2j(right_surf)
    if not left_jamo or len(right_jamo) < 2:
        return None
    last = left_jamo[-1]
    if not (_JONGSEONG_START <= last <= _JONGSEONG_END):
        return None
    if right_jamo[0] != _NULL_ONSET:
        return None
    if right_jamo[1] not in _YIOTIZED_VOWELS:
        return None
    new_onset = _RIEUL_ONSET if last == _RIEUL_JONGSEONG else _NIEUN_ONSET
    return compose(new_onset + right_jamo[1:])


def n_insertion(string, mecab_inst, verbose=False, applied_rules=None):
    '''Rule 29: ᄂ insertion at compound and phrase boundaries.
    When first morpheme/word ends in a consonant and second starts with 이/야/여/요/유,
    insert ᄂ (or ᄅ for ᆯ-final, per 붙임1). Handles both MeCab Compound tokens
    and whitespace-separated word pairs (붙임2).
    '''
    out = string
    cursor = 0

    # Compound pass (existing behaviour)
    for morph in mecab_inst.parse(string):
        pos = string.find(morph.surface, cursor)
        if pos == -1:
            continue
        cursor = pos + len(morph.surface)

        if morph.feature.type != 'Compound':
            continue
        expression = morph.feature.expression
        if not expression or '+' not in expression:
            continue
        if morph.surface in _N_INSERTION_EXCEPTIONS:
            continue

        parts = expression.split('+')
        first_surf = parts[0].split('/')[0]
        second_surf = parts[1].split('/')[0]

        new_second = _apply_n_insertion_at_boundary(first_surf, second_surf)
        if new_second is None:
            continue

        new_surf = compose(h2j(first_surf) + h2j(new_second))
        out = out[:pos] + new_surf + out[pos + len(morph.surface):]

    # 붙임 2 pass: whitespace-separated word pairs
    segments = [(m.group(), not m.group()[0].isspace())
                for m in re.finditer(r'\S+|\s+', out)]
    # segments: list of (text, is_word)
    words = [(i, text) for i, (text, is_word) in enumerate(segments) if is_word]

    rebuilt = [text for text, _ in segments]
    for k in range(len(words) - 1):
        i, left = words[k]
        j, right = words[k + 1]
        if left in _N_INSERTION_EXCEPTIONS or right in _N_INSERTION_EXCEPTIONS:
            continue
        phrase = left + ' ' + right
        if phrase in _N_INSERTION_PHRASE_EXCEPTIONS:
            continue
        new_right = _apply_n_insertion_at_boundary(left, right)
        if new_right is None:
            continue
        rebuilt[j] = new_right
        words[k + 1] = (j, new_right)

    out = ''.join(rebuilt)

    gloss(verbose, out, string, "29", applied_rules)
    return out



def getCompoundToken(string, mecab):
    tokens = []

    for morph in mecab.parse(string):
        tokenType = morph.feature.type
        expression = morph.feature.expression 

        if tokenType == 'Compound' and '+' in expression:
            for part in expression.split('+'):
                surface = part.split('/')[0]
                pos = part.split('/')[1]
                tokens.append((surface, pos, True))

        else:
            tokens.append((morph.surface, morph.feature.pos, False))

    return tokens




