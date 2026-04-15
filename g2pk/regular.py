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
    # Rule 15: coda before a SPACE + vowel-initial content morpheme (실질형태소).
    # The space distinguishes this from rules 13/14 (grammatical morphemes, no space).
    #
    # The table (step 7) pre-neutralizes non-representative codas at word boundaries
    # via its (\W|$) column (rule 9): e.g. ᆾ+space → ᆮ+space, ᇀ+space → ᆮ+space.
    # So by the time this function runs, only the representative codas
    # (ᆨ, ᆫ, ᆮ, ᆯ, ᆷ, ᆸ) will realistically match the single-coda pairs below.
    # The non-representative pairs (ᆺ→ᄉ, ᆾ→ᄎ, ᇀ→ᄐ, etc.) are effectively dead
    # code — if they somehow fired they would be wrong (e.g. 꽃 위: ᆾ is already
    # ᆮ by this point, so ("ᆮ ᄋ"," ᄃ") fires correctly giving [꼬뒤], not ᄎ).
    # Similarly, double-coda pairs below are dead code because the table already
    # reduces them (e.g. ᆰ+space → ᆨ+space), so ("ᆨ ᄋ"," ᄀ") fires instead.
    out = inp

    pairs = [ ("ᆨ ᄋ", " ᄀ"),
              ("ᆩ ᄋ", " ᄁ"),  # dead: table converts ᆩ+space → ᆨ+space first
              ("ᆫ ᄋ", " ᄂ"),
              ("ᆮ ᄋ", " ᄃ"),
              ("ᆯ ᄋ", " ᄅ"),
              ("ᆷ ᄋ", " ᄆ"),
              ("ᆸ ᄋ", " ᄇ"),
              ("ᆺ ᄋ", " ᄉ"),  # dead: table converts ᆺ+space → ᆮ+space first
              ("ᆻ ᄋ", " ᄊ"),  # dead: table converts ᆻ+space → ᆮ+space first
              ("ᆽ ᄋ", " ᄌ"),  # dead: table converts ᆽ+space → ᆮ+space first
              ("ᆾ ᄋ", " ᄎ"),  # dead: table converts ᆾ+space → ᆮ+space first
              ("ᆿ ᄋ", " ᄏ"),  # dead: table converts ᆿ+space → ᆨ+space first
              ("ᇀ ᄋ", " ᄐ"),  # dead: table converts ᇀ+space → ᆮ+space first
              ("ᇁ ᄋ", " ᄑ"),  # dead: table converts ᇁ+space → ᆸ+space first

              ("ᆪ ᄋ", "ᆨ ᄊ"),  # dead: table reduces ᆪ+space → ᆨ+space first
              ("ᆬ ᄋ", "ᆫ ᄌ"),  # dead: table reduces ᆬ+space → ᆫ+space first
              ("ᆰ ᄋ", "ᆯ ᄀ"),  # dead: table reduces ᆰ+space → ᆨ+space first
              ("ᆱ ᄋ", "ᆯ ᄆ"),  # dead: table reduces ᆱ+space → ᆷ+space first
              ("ᆲ ᄋ", "ᆯ ᄇ"),  # dead: table reduces ᆲ+space → ᆯ+space first
              ("ᆳ ᄋ", "ᆯ ᄊ"),  # dead: table reduces ᆳ+space → ᆯ+space first
              ("ᆴ ᄋ", "ᆯ ᄐ"),  # dead: table reduces ᆴ+space → ᆯ+space first
              ("ᆵ ᄋ", "ᆯ ᄑ"),  # dead: table reduces ᆵ+space → ᆸ+space first
              ("ᆹ ᄋ", "ᆸ ᄊ") ]  # dead: table reduces ᆹ+space → ᆸ+space first

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
