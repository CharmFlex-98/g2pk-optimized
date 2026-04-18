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
    # annotate() marks such boundaries with /C. This runs before the table
    # rules, so codas are still in their original (non-neutralized) form;
    # all simple and double codas must be handled here.
    out = inp

    pairs = [
        # cross-space liaison — simple codas (representative)
        ('ᆨ/C ᄋ', ' ᄀ'),
        ('ᆫ/C ᄋ', ' ᄂ'),
        ('ᆮ/C ᄋ', ' ᄃ'),
        ('ᆯ/C ᄋ', ' ᄅ'),
        ('ᆷ/C ᄋ', ' ᄆ'),
        ('ᆸ/C ᄋ', ' ᄇ'),
        # cross-space liaison — simple codas (non-representative, neutralize then liaise)
        ('ᆩ/C ᄋ', ' ᄀ'),           # ᆩ→ᆨ→ᄀ
        ('ᆺ/C ᄋ', ' ᄃ'),           # ᆺ→ᆮ→ᄃ
        ('ᆻ/C ᄋ', ' ᄃ'),           # ᆻ→ᆮ→ᄃ
        ('ᆽ/C ᄋ', ' ᄃ'),           # ᆽ→ᆮ→ᄃ
        ('ᆾ/C ᄋ', ' ᄃ'),           # ᆾ→ᆮ→ᄃ
        ('ᇀ/C ᄋ', ' ᄃ'),           # ᇀ→ᆮ→ᄃ
        ('ᇂ/C ᄋ', ' ᄋ'),           # ᇂ drops, vowel takes null onset
        # cross-space liaison — double codas (left coda kept, neutralize then liaise)
        ('ᆪ/C ᄋ', ' ᄀ'),           # ᆪ(ᆨ+ᆺ)→ᆨ→ᄀ
        ('ᆬ/C ᄋ', ' ᄂ'),           # ᆬ(ᆫ+ᆽ)→ᆫ→ᄂ
        ('ᆭ/C ᄋ', ' ᄂ'),           # ᆭ(ᆫ+ᇂ)→ᆫ→ᄂ
        ('ᆰ/C ᄋ', ' ᄅ'),           # ᆰ(ᆯ+ᆨ)→ᆯ→ᄅ
        ('ᆱ/C ᄋ', ' ᄅ'),           # ᆱ(ᆯ+ᆷ)→ᆯ→ᄅ
        ('ᆲ/C ᄋ', ' ᄅ'),           # ᆲ(ᆯ+ᆸ)→ᆯ→ᄅ
        ('ᆳ/C ᄋ', ' ᄅ'),           # ᆳ(ᆯ+ᆺ)→ᆯ→ᄅ
        ('ᆴ/C ᄋ', ' ᄅ'),           # ᆴ(ᆯ+ᇀ)→ᆯ→ᄅ
        ('ᆵ/C ᄋ', ' ᄅ'),           # ᆵ(ᆯ+ᆾ)→ᆯ→ᄅ
        ('ᆶ/C ᄋ', ' ᄅ'),           # ᆶ(ᆯ+ᇂ)→ᆯ→ᄅ
        ('ᆹ/C ᄋ', ' ᄇ'),           # ᆹ(ᆸ+ᆺ)→ᆸ→ᄇ  e.g. 값 있다 → 가 빋따
        # intra-word liaison (no space) — simple codas (representative)
        ('ᆨ/Cᄋ', 'ᄀ'),
        ('ᆫ/Cᄋ', 'ᄂ'),
        ('ᆮ/Cᄋ', 'ᄃ'),
        ('ᆯ/Cᄋ', 'ᄅ'),
        ('ᆷ/Cᄋ', 'ᄆ'),
        ('ᆸ/Cᄋ', 'ᄇ'),
        # intra-word liaison (no space) — simple codas (non-representative)
        ('ᆩ/Cᄋ', 'ᄀ'),            # ᆩ→ᆨ→ᄀ
        ('ᆺ/Cᄋ', 'ᄃ'),            # ᆺ→ᆮ→ᄃ
        ('ᆻ/Cᄋ', 'ᄃ'),            # ᆻ→ᆮ→ᄃ
        ('ᆽ/Cᄋ', 'ᄃ'),            # ᆽ→ᆮ→ᄃ  (e.g. 젖어미 → 저더미)
        ('ᆾ/Cᄋ', 'ᄃ'),            # ᆾ→ᆮ→ᄃ
        ('ᇀ/Cᄋ', 'ᄃ'),            # ᇀ→ᆮ→ᄃ
        ('ᇂ/Cᄋ', 'ᄋ'),            # ᇂ drops, vowel takes null onset
        # intra-word liaison (no space) — double codas
        ('ᆪ/Cᄋ', 'ᄀ'),            # ᆪ(ᆨ+ᆺ)→ᆨ→ᄀ
        ('ᆬ/Cᄋ', 'ᄂ'),            # ᆬ(ᆫ+ᆽ)→ᆫ→ᄂ
        ('ᆭ/Cᄋ', 'ᄂ'),            # ᆭ(ᆫ+ᇂ)→ᆫ→ᄂ
        ('ᆰ/Cᄋ', 'ᄅ'),            # ᆰ(ᆯ+ᆨ)→ᆯ→ᄅ
        ('ᆱ/Cᄋ', 'ᄅ'),            # ᆱ(ᆯ+ᆷ)→ᆯ→ᄅ
        ('ᆲ/Cᄋ', 'ᄅ'),            # ᆲ(ᆯ+ᆸ)→ᆯ→ᄅ
        ('ᆳ/Cᄋ', 'ᄅ'),            # ᆳ(ᆯ+ᆺ)→ᆯ→ᄅ
        ('ᆴ/Cᄋ', 'ᄅ'),            # ᆴ(ᆯ+ᇀ)→ᆯ→ᄅ
        ('ᆵ/Cᄋ', 'ᄅ'),            # ᆵ(ᆯ+ᆾ)→ᆯ→ᄅ
        ('ᆶ/Cᄋ', 'ᄅ'),            # ᆶ(ᆯ+ᇂ)→ᆯ→ᄅ
        ('ᆹ/Cᄋ', 'ᄇ'),            # ᆹ(ᆸ+ᆺ)→ᆸ→ᄇ
    ]
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
