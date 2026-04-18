# -*- coding: utf-8 -*-
'''
Special rule for processing Hangul
https://github.com/kyubyong/g2pK
'''

import re

from g2pk.utils import gloss


############################ vowels ############################
def jyeo(inp, descriptive=False, verbose=False, applied_rules=None):
    # 일반적인 규칙으로 취급한다 by kyubyong

    out = re.sub("([ᄌᄍᄎ])ᅧ", r"\1ᅥ", inp)
    gloss(verbose, out, inp, "5.1", applied_rules)
    return out


def ye(inp, descriptive=False, verbose=False, applied_rules=None):
    # 실제로 언중은 예, 녜, 셰, 쎼 이외의 'ㅖ'는 [ㅔ]로 발음한다. by kyubyong

    if descriptive:
        out = re.sub("([ᄀᄁᄃᄄᄅᄆᄇᄈᄌᄍᄎᄏᄐᄑᄒ])ᅨ", r"\1ᅦ", inp)
    else:
        out = inp
    gloss(verbose, out, inp, "5.2", applied_rules)
    return out


def consonant_ui(inp, descriptive=False, verbose=False, applied_rules=None):
    out = re.sub("([ᄀᄁᄂᄃᄄᄅᄆᄇᄈᄉᄊᄌᄍᄎᄏᄐᄑᄒ])ᅴ", r"\1ᅵ", inp)
    gloss(verbose, out, inp, "5.3", applied_rules)
    return out


def josa_ui(inp, descriptive=False, verbose=False, applied_rules=None):
    # 실제로 언중은 높은 확률로 조사 '의'는 [ㅔ]로 발음한다.
    if descriptive:
        out = re.sub("의/J", "에", inp)
    else:
        out = inp.replace("/J", "")
    gloss(verbose, out, inp, "5.4.2", applied_rules)
    return out


def vowel_ui(inp, descriptive=False, verbose=False, applied_rules=None):
    # 실제로 언중은 높은 확률로 단어의 첫음절 이외의 '의'는 [ㅣ]로 발음한다."""
    if descriptive:
        out = re.sub("(\Sᄋ)ᅴ", r"\1ᅵ", inp)
    else:
        out = inp
    gloss(verbose, out, inp, "5.4.1", applied_rules)
    return out


def jamo(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    out = re.sub("([그])ᆮᄋ", r"\1ᄉ", out)
    out = re.sub("([으])[ᆽᆾᇀᇂ]ᄋ", r"\1ᄉ", out)
    out = re.sub("([으])[ᆿ]ᄋ", r"\1ᄀ", out)
    out = re.sub("([으])[ᇁ]ᄋ", r"\1ᄇ", out)

    gloss(verbose, out, inp, "16", applied_rules)
    return out


    ############################ 어간 받침 ############################
def rieulgiyeok(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp
    out = re.sub("ᆰ/Pᄀ", "ᆯᄁ", out)

    gloss(verbose, out, inp, "11.1", applied_rules)
    return out


def rieulbieub(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    out = re.sub("([ᆲᆴ])/Pᄀ", r"\1ᄁ", out)
    out = re.sub("([ᆲᆴ])/Pᄃ", r"\1ᄄ", out)
    out = re.sub("([ᆲᆴ])/Pᄉ", r"\1ᄊ", out)
    out = re.sub("([ᆲᆴ])/Pᄌ", r"\1ᄍ", out)

    gloss(verbose, out, inp, "25", applied_rules)
    return out


def verb_nieun(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    pairs = [
        ("([ᆫᆷ])/Pᄀ", r"\1ᄁ"),
        ("([ᆫᆷ])/Pᄃ", r"\1ᄄ"),
        ("([ᆫᆷ])/Pᄉ", r"\1ᄊ"),
        ("([ᆫᆷ])/Pᄌ", r"\1ᄍ"),

        # IMPORTANT: cluster forms are treated SAME as ㄴ/ㅁ here
        ("ᆬ/Pᄀ", "ᆬᄁ"),
        ("ᆬ/Pᄃ", "ᆬᄄ"),
        ("ᆬ/Pᄉ", "ᆬᄊ"),
        ("ᆬ/Pᄌ", "ᆬᄍ"),

        ("ᆱ/Pᄀ", "ᆱᄁ"),
        ("ᆱ/Pᄃ", "ᆱᄄ"),
        ("ᆱ/Pᄉ", "ᆱᄊ"),
        ("ᆱ/Pᄌ", "ᆱᄍ"),
    ]

    for str1, str2 in pairs:
        out = re.sub(str1, str2, out)

    gloss(verbose, out, inp, "24", applied_rules)
    return out


def balb(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp
    syllable_final_or_consonants = r"($|[\u1100-\u110a\u110c-\u1111])"

    # exceptions
    out = re.sub(f"(바)ᆲ({syllable_final_or_consonants})", r"\1ᆸ\2", out)
    out = re.sub(f"(너)ᆲ([ᄌᄍ]ᅮ|[ᄃᄄ]ᅮ)", r"\1ᆸ\2", out)
    gloss(verbose, out, inp, "10.1", applied_rules)
    return out


def palatalize(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    out = re.sub("ᆮᄋ([ᅵᅣᅧᅭᅲ])", r"ᄌ\1", out)
    out = re.sub("ᇀᄋ([ᅵᅣᅧᅭᅲ])", r"ᄎ\1", out)
    out = re.sub("ᆴᄋ([ᅵᅣᅧᅭᅲ])", r"ᆯᄎ\1", out)

    out = re.sub("ᆮᄒ([ᅵᅣᅧᅭᅲ])", r"ᄎ\1", out)

    gloss(verbose, out, inp, "17", applied_rules)
    return out


def modifying_rieul(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    pairs = [   ("ᆯ/E ᄀ", r"ᆯ ᄁ"),
                ("ᆯ/E ᄃ", r"ᆯ ᄄ"),
                ("ᆯ/E ᄇ", r"ᆯ ᄈ"),
                ("ᆯ/E ᄉ", r"ᆯ ᄊ"),
                ("ᆯ/E ᄌ", r"ᆯ ᄍ"),

                ("ᆯ걸", "ᆯ껄"),
                ("ᆯ밖에", "ᆯ빠께"),
                ("ᆯ세라", "ᆯ쎄라"),
                ("ᆯ수록", "ᆯ쑤록"),
                ("ᆯ지라도", "ᆯ찌라도"),
                ("ᆯ지언정", "ᆯ찌언정"),
                ("ᆯ진대", "ᆯ찐대") ]

    for str1, str2 in pairs:
        out = re.sub(str1, str2, out)

    gloss(verbose, out, inp, "27", applied_rules)
    return out


def link3(inp, descriptive=False, verbose=False, applied_rules=None):
    # Rule 15: coda liaison before a content morpheme (실질형태소) boundary.
    # annotate() marks such boundaries with /C when the next word starts with
    # null-onset ᄋ + rule-15 vowel (ᅡᅥᅩᅮᅱ). The table pre-neutralizes codas
    # at word boundaries, so only the 6 representative codas are live here.
    out = inp

    pairs = [
        # cross-space liaison — representative codas
        ('ᆨ/C ᄋ', ' ᄀ'),
        ('ᆫ/C ᄋ', ' ᄂ'),
        ('ᆮ/C ᄋ', ' ᄃ'),
        ('ᆯ/C ᄋ', ' ᄅ'),
        ('ᆷ/C ᄋ', ' ᄆ'),
        ('ᆸ/C ᄋ', ' ᄇ'),
        # cross-space liaison — non-representative codas (neutralize then liaise)
        ('ᆩ/C ᄋ', ' ᄀ'),           # ᆩ→ᆨ→ᄀ
        ('ᆺ/C ᄋ', ' ᄃ'),           # ᆺ→ᆮ→ᄃ
        ('ᆻ/C ᄋ', ' ᄃ'),           # ᆻ→ᆮ→ᄃ
        ('ᆽ/C ᄋ', ' ᄃ'),           # ᆽ→ᆮ→ᄃ
        ('ᆾ/C ᄋ', ' ᄃ'),           # ᆾ→ᆮ→ᄃ
        ('ᇀ/C ᄋ', ' ᄃ'),           # ᇀ→ᆮ→ᄃ
        ('ᇂ/C ᄋ', ' ᄋ'),           # ᇂ drops, vowel takes null onset
        # intra-word liaison (no space) — representative codas
        ('ᆨ/Cᄋ', 'ᄀ'),
        ('ᆫ/Cᄋ', 'ᄂ'),
        ('ᆮ/Cᄋ', 'ᄃ'),
        ('ᆯ/Cᄋ', 'ᄅ'),
        ('ᆷ/Cᄋ', 'ᄆ'),
        ('ᆸ/Cᄋ', 'ᄇ'),
        # intra-word liaison (no space) — non-representative codas
        ('ᆩ/Cᄋ', 'ᄀ'),            # ᆩ→ᆨ→ᄀ
        ('ᆺ/Cᄋ', 'ᄃ'),            # ᆺ→ᆮ→ᄃ
        ('ᆻ/Cᄋ', 'ᄃ'),            # ᆻ→ᆮ→ᄃ
        ('ᆽ/Cᄋ', 'ᄃ'),            # ᆽ→ᆮ→ᄃ  (e.g. 젖어미 → 저더미)
        ('ᆾ/Cᄋ', 'ᄃ'),            # ᆾ→ᆮ→ᄃ
        ('ᇀ/Cᄋ', 'ᄃ'),            # ᇀ→ᆮ→ᄃ
        ('ᇂ/Cᄋ', 'ᄋ'),            # ᇂ drops, vowel takes null onset
    ]
    for str1, str2 in pairs:
        out = out.replace(str1, str2)

    gloss(verbose, out, inp, "15", applied_rules)
    return out
