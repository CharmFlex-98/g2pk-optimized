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
    out = inp

    pairs = [ ("ᆨ ᄋ", " ᄀ"),
              ("ᆩ ᄋ", " ᄁ"),
              ("ᆫ ᄋ", " ᄂ"),
              ("ᆮ ᄋ", " ᄃ"),
              ("ᆯ ᄋ", " ᄅ"),
              ("ᆷ ᄋ", " ᄆ"),
              ("ᆸ ᄋ", " ᄇ"),
              ("ᆺ ᄋ", " ᄉ"),
              ("ᆻ ᄋ", " ᄊ"),
              ("ᆽ ᄋ", " ᄌ"),
              ("ᆾ ᄋ", " ᄎ"),
              ("ᆿ ᄋ", " ᄏ"),
              ("ᇀ ᄋ", " ᄐ"),
              ("ᇁ ᄋ", " ᄑ"),

              ("ᆪ ᄋ", "ᆨ ᄊ"),
              ("ᆬ ᄋ", "ᆫ ᄌ"),
              ("ᆰ ᄋ", "ᆯ ᄀ"),
              ("ᆱ ᄋ", "ᆯ ᄆ"),
              ("ᆲ ᄋ", "ᆯ ᄇ"),
              ("ᆳ ᄋ", "ᆯ ᄊ"),
              ("ᆴ ᄋ", "ᆯ ᄐ"),
              ("ᆵ ᄋ", "ᆯ ᄑ"),
              ("ᆹ ᄋ", "ᆸ ᄊ") ]

    for str1, str2 in pairs:
        out = out.replace(str1, str2)

    gloss(verbose, out, inp, "15", applied_rules)
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
