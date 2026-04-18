# -*- coding: utf-8 -*-
'''
https://github.com/kyubyong/g2pK
'''

from g2pk.utils import gloss


def link1(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    pairs = [ ("ᆨᄋ", "ᄀ"),
              ("ᆩᄋ", "ᄁ"),
              ("ᆫᄋ", "ᄂ"),
              ("ᆮᄋ", "ᄃ"),
              ("ᆯᄋ", "ᄅ"),
              ("ᆷᄋ", "ᄆ"),
              ("ᆸᄋ", "ᄇ"),
              ("ᆺᄋ", "ᄉ"),
              ("ᆻᄋ", "ᄊ"),
              ("ᆽᄋ", "ᄌ"),
              ("ᆾᄋ", "ᄎ"),
              ("ᆿᄋ", "ᄏ"),
              ("ᇀᄋ", "ᄐ"),
              ("ᇁᄋ", "ᄑ")]
    for str1, str2 in pairs:
        out = out.replace(str1, str2)

    gloss(verbose, out, inp, "13", applied_rules)
    return out


def link2(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    pairs = [ ("ᆪᄋ", "ᆨᄊ"),
              ("ᆬᄋ", "ᆫᄌ"),
              ("ᆰᄋ", "ᆯᄀ"),
              ("ᆱᄋ", "ᆯᄆ"),
              ("ᆲᄋ", "ᆯᄇ"),
              ("ᆳᄋ", "ᆯᄊ"),
              ("ᆴᄋ", "ᆯᄐ"),
              ("ᆵᄋ", "ᆯᄑ"),
              ("ᆹᄋ", "ᆸᄊ") ]
    for str1, str2 in pairs:
        out = out.replace(str1, str2)

    gloss(verbose, out, inp, "14", applied_rules)
    return out


def link3(inp, descriptive=False, verbose=False, applied_rules=None):
    # Rule 15: coda liaison before a content morpheme (실질형태소) boundary.
    # annotate() marks such boundaries with /C when the next word starts with
    # null-onset ᄋ + rule-15 vowel (ᅡᅥᅩᅮᅱ). The table pre-neutralizes codas
    # at word boundaries, so only the 6 representative codas are live here.
    out = inp

    pairs = [
        ('ᆨ/C ᄋ', ' ᄀ'),  # cross-space liaison
        ('ᆫ/C ᄋ', ' ᄂ'),
        ('ᆮ/C ᄋ', ' ᄃ'),
        ('ᆯ/C ᄋ', ' ᄅ'),
        ('ᆷ/C ᄋ', ' ᄆ'),
        ('ᆸ/C ᄋ', ' ᄇ'),
        ('ᆨ/Cᄋ', 'ᄀ'),    # intra-word liaison (no space)
        ('ᆫ/Cᄋ', 'ᄂ'),
        ('ᆮ/Cᄋ', 'ᄃ'),
        ('ᆯ/Cᄋ', 'ᄅ'),
        ('ᆷ/Cᄋ', 'ᄆ'),
        ('ᆸ/Cᄋ', 'ᄇ'),
    ]
    for str1, str2 in pairs:
        out = out.replace(str1, str2)
    out = out.replace('/C', '')  # clean up unused /C markers

    gloss(verbose, out, inp.replace('/C', ''), "15", applied_rules)
    return out


def link4(inp, descriptive=False, verbose=False, applied_rules=None):
    out = inp

    pairs = [ ("ᇂᄋ", "ᄋ"),
              ("ᆭᄋ", "ᄂ"),
              ("ᆶᄋ", "ᄅ") ]

    for str1, str2 in pairs:
        out = out.replace(str1, str2)

    gloss(verbose, out, inp, "12.4", applied_rules)
    return out
