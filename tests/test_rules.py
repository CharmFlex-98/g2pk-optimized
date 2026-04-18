# -*- coding: utf-8 -*-
"""
Unit tests for Korean pronunciation rules in g2pK.
Each test verifies:
  1. The output phonetic form matches the expected pronunciation.
  2. The expected rule ID is present in the verbose applied_rules list.

Rules tested: 5.1, 5.2, 5.3, 5.4.1, 9, 10, 10.1, 11, 11.1,
              12, 12.4, 13, 14, 15, 17, 18, 19, 20, 23, 24, 25,
              26, 27, 28, 29, 30.1, 30.2, 30.3
"""

import pytest
from g2pk import G2p


@pytest.fixture(scope="module")
def g2p():
    return G2p()


def rule_ids(applied_rules):
    return {r["rule_id"] for r in applied_rules}


# ── Rule 5.1 ─────────────────────────────────────────────────────────────────
# 져/쪄/쳐 → 저/쩌/처 (always applied, not just descriptive)

def test_rule_5_1_jyeo(g2p):
    out, rules, _ = g2p("가져", verbose=True)
    assert out == "가저", f"Expected '가저', got '{out}'"
    assert "5.1" in rule_ids(rules)


def test_rule_5_1_jyeo_2(g2p):
    out, rules, _ = g2p("다쳐", verbose=True)
    assert out == "다처", f"Expected '다처', got '{out}'"
    assert "5.1" in rule_ids(rules)


# ── Rule 5.2 ─────────────────────────────────────────────────────────────────
# ㅖ → ㅔ after consonants (descriptive only)

def test_rule_5_2_ye_descriptive(g2p):
    out, rules, _ = g2p("시계", descriptive=True, verbose=True)
    assert out == "시게", f"Expected '시게', got '{out}'"
    assert "5.2" in rule_ids(rules)


# ── Rule 5.3 ─────────────────────────────────────────────────────────────────
# consonant + ㅢ → consonant + ㅣ

def test_rule_5_3_consonant_ui(g2p):
    out, rules, _ = g2p("무늬", verbose=True)
    assert out == "무니", f"Expected '무니', got '{out}'"
    assert "5.3" in rule_ids(rules)


def test_rule_5_3_consonant_ui_2(g2p):
    out, rules, _ = g2p("희망", verbose=True)
    assert out == "히망", f"Expected '히망', got '{out}'"
    assert "5.3" in rule_ids(rules)


# ── Rule 5.4.1 ───────────────────────────────────────────────────────────────
# Non-initial 의 → 이 (descriptive only)

def test_rule_5_4_1_vowel_ui_descriptive(g2p):
    out, rules, _ = g2p("주의", descriptive=True, verbose=True)
    assert out == "주이", f"Expected '주이', got '{out}'"
    assert "5.4.1" in rule_ids(rules)


# ── Rule 9 ───────────────────────────────────────────────────────────────────
# Coda neutralisation: ᆩᆿᆺᆻᆽᆾᇀᇂᇁ → representative ᆨᆮᆸ

def test_rule_9_coda_neutralisation(g2p):
    out, rules, _ = g2p("닦다", verbose=True)
    assert out == "닥따", f"Expected '닥따', got '{out}'"
    assert "9" in rule_ids(rules)


def test_rule_9_coda_neutralisation_2(g2p):
    out, rules, _ = g2p("앞", verbose=True)
    assert out == "압", f"Expected '압', got '{out}'"
    assert "9" in rule_ids(rules)


# ── Rule 10 ──────────────────────────────────────────────────────────────────
# Complex coda reduction: ᆪ→ᆨ, ᆬ→ᆫ, ᆲᆳᆴ→ᆯ, ᆹ→ᆸ at syllable coda

def test_rule_10_complex_coda(g2p):
    out, rules, _ = g2p("넋", verbose=True)
    assert out == "넉", f"Expected '넉', got '{out}'"
    assert "10" in rule_ids(rules)


def test_rule_10_complex_coda_2(g2p):
    out, rules, _ = g2p("앉다", verbose=True)
    assert out == "안따", f"Expected '안따', got '{out}'"
    assert "10" in rule_ids(rules)


# ── Rule 10.1 ────────────────────────────────────────────────────────────────
# 밟- before consonant → ᆸ (exception to rule 10)

def test_rule_10_1_balb(g2p):
    out, rules, _ = g2p("밟다", verbose=True)
    assert out == "밥따", f"Expected '밥따', got '{out}'"
    assert "10.1" in rule_ids(rules)


# ── Rule 11 ──────────────────────────────────────────────────────────────────
# ᆰ→ᆨ, ᆱ→ᆷ, ᆵ→ᆸ in coda position

def test_rule_11_complex_coda_rieul(g2p):
    out, rules, _ = g2p("닭", verbose=True)
    assert out == "닥", f"Expected '닥', got '{out}'"
    assert "11" in rule_ids(rules)


def test_rule_11_complex_coda_rieul_2(g2p):
    out, rules, _ = g2p("삶", verbose=True)
    assert out == "삼", f"Expected '삼', got '{out}'"
    assert "11" in rule_ids(rules)


# ── Rule 11.1 ────────────────────────────────────────────────────────────────
# Verb stem ᆰ before ᄀ → ᆯ (exception: ᆰ/P + ᄀ → ᆯᄁ)

def test_rule_11_1_rieulgiyeok(g2p):
    out, rules, _ = g2p("맑게", verbose=True)
    assert out == "말께", f"Expected '말께', got '{out}'"
    assert "11.1" in rule_ids(rules)


# ── Rule 12 ──────────────────────────────────────────────────────────────────
# ᇂ + ᄀ/ᄃ/ᄌ → aspiration ᄏ/ᄐ/ᄎ

def test_rule_12_hieut_aspiration(g2p):
    out, rules, _ = g2p("놓고", verbose=True)
    assert out == "노코", f"Expected '노코', got '{out}'"
    assert "12" in rule_ids(rules)


def test_rule_12_hieut_aspiration_2(g2p):
    out, rules, _ = g2p("많고", verbose=True)
    assert out == "만코", f"Expected '만코', got '{out}'"
    assert "12" in rule_ids(rules)


# ── Rule 12.4 ────────────────────────────────────────────────────────────────
# ᇂ (or ᆭ/ᆶ) + vowel-initial suffix → ᇂ is dropped

def test_rule_12_4_hieut_drop(g2p):
    out, rules, _ = g2p("낳은", verbose=True)
    assert out == "나은", f"Expected '나은', got '{out}'"
    assert "12.4" in rule_ids(rules)


def test_rule_12_4_hieut_drop_2(g2p):
    out, rules, _ = g2p("많아", verbose=True)
    assert out == "마나", f"Expected '마나', got '{out}'"
    assert "12.4" in rule_ids(rules)


# ── Rule 13 ──────────────────────────────────────────────────────────────────
# Simple coda + vowel-initial grammatical morpheme → liaison

def test_rule_13_simple_liaison(g2p):
    out, rules, _ = g2p("옷이", verbose=True)
    assert out == "오시", f"Expected '오시', got '{out}'"
    assert "13" in rule_ids(rules)


def test_rule_13_simple_liaison_2(g2p):
    out, rules, _ = g2p("있어", verbose=True)
    assert out == "이써", f"Expected '이써', got '{out}'"
    assert "13" in rule_ids(rules)


# ── Rule 14 ──────────────────────────────────────────────────────────────────
# Complex coda + vowel-initial grammatical morpheme → only second consonant liaises

def test_rule_14_complex_liaison(g2p):
    out, rules, _ = g2p("넋이", verbose=True)
    assert out == "넉씨", f"Expected '넉씨', got '{out}'"
    assert "14" in rule_ids(rules)


def test_rule_14_complex_liaison_2(g2p):
    out, rules, _ = g2p("없어", verbose=True)
    assert out == "업써", f"Expected '업써', got '{out}'"
    assert "14" in rule_ids(rules)


# ── Rule 15 ──────────────────────────────────────────────────────────────────
# Coda liaison before vowel-initial content morpheme (실질형태소)

def test_rule_15_content_liaison(g2p):
    out, rules, _ = g2p("맛없다", verbose=True)
    assert out == "마덥따", f"Expected '마덥따', got '{out}'"
    assert "15" in rule_ids(rules)


# ── Rule 17 ──────────────────────────────────────────────────────────────────
# Palatalization: ᆮ/ᇀ + 이/야/여/요/유 → ᄌ/ᄎ

def test_rule_17_palatalization(g2p):
    out, rules, _ = g2p("굳이", verbose=True)
    assert out == "구지", f"Expected '구지', got '{out}'"
    assert "17" in rule_ids(rules)


def test_rule_17_palatalization_2(g2p):
    out, rules, _ = g2p("밭이", verbose=True)
    assert out == "바치", f"Expected '바치', got '{out}'"
    assert "17" in rule_ids(rules)


# ── Rule 18 ──────────────────────────────────────────────────────────────────
# Nasalisation: ᆨᆮᆸ + ᄂ/ᄆ → ᆼᆫᆷ + ᄂ/ᄆ

def test_rule_18_nasalisation(g2p):
    out, rules, _ = g2p("먹는", verbose=True)
    assert out == "멍는", f"Expected '멍는', got '{out}'"
    assert "18" in rule_ids(rules)


def test_rule_18_nasalisation_2(g2p):
    out, rules, _ = g2p("국물", verbose=True)
    assert out == "궁물", f"Expected '궁물', got '{out}'"
    assert "18" in rule_ids(rules)


# ── Rule 19 ──────────────────────────────────────────────────────────────────
# ᄅ → ᄂ after ᆷ/ᆼ (or ᆨ/ᆸ via 붙임)

def test_rule_19_rieul_nasalisation(g2p):
    out, rules, _ = g2p("강릉", verbose=True)
    assert out == "강능", f"Expected '강능', got '{out}'"
    assert "19" in rule_ids(rules)


def test_rule_19_rieul_nasalisation_2(g2p):
    out, rules, _ = g2p("침략", verbose=True)
    assert out == "침냑", f"Expected '침냑', got '{out}'"
    assert "19" in rule_ids(rules)


# ── Rule 20 ──────────────────────────────────────────────────────────────────
# ᆫ + ᄅ or ᄅ + ᄂ → lateral assimilation [ᆯ+ᄅ]

def test_rule_20_lateralisation(g2p):
    out, rules, _ = g2p("신라", verbose=True)
    assert out == "실라", f"Expected '실라', got '{out}'"
    assert "20" in rule_ids(rules)


def test_rule_20_lateralisation_2(g2p):
    out, rules, _ = g2p("난로", verbose=True)
    assert out == "날로", f"Expected '날로', got '{out}'"
    assert "20" in rule_ids(rules)


# ── Rule 23 ──────────────────────────────────────────────────────────────────
# Tensification: ᆨᆮᆸ + plain obstruent → tensed obstruent

def test_rule_23_tensification(g2p):
    out, rules, _ = g2p("국밥", verbose=True)
    assert out == "국빱", f"Expected '국빱', got '{out}'"
    assert "23" in rule_ids(rules)


def test_rule_23_tensification_2(g2p):
    out, rules, _ = g2p("덮개", verbose=True)
    assert out == "덥깨", f"Expected '덥깨', got '{out}'"
    assert "23" in rule_ids(rules)


# ── Rule 24 ──────────────────────────────────────────────────────────────────
# Verb stem ᆫ(ᆬ)/ᆷ(ᆱ) + plain obstruent → tensed (된소리)

def test_rule_24_verb_tensification(g2p):
    out, rules, _ = g2p("앉고", verbose=True)
    assert out == "안꼬", f"Expected '안꼬', got '{out}'"
    assert "24" in rule_ids(rules)


def test_rule_24_verb_tensification_2(g2p):
    out, rules, _ = g2p("젊지", verbose=True)
    assert out == "점찌", f"Expected '점찌', got '{out}'"
    assert "24" in rule_ids(rules)


# ── Rule 25 ──────────────────────────────────────────────────────────────────
# Verb stem ᆲ/ᆴ + plain obstruent → tensed

def test_rule_25_rieulbieub_tensification(g2p):
    out, rules, _ = g2p("넓게", verbose=True)
    assert out == "널께", f"Expected '널께', got '{out}'"
    assert "25" in rule_ids(rules)


# ── Rule 26 ──────────────────────────────────────────────────────────────────
# Sino-Korean: ᆯ + ᄃ/ᄉ/ᄌ → tensed (된소리)

def test_rule_26_sino_korean_fortis(g2p):
    out, rules, _ = g2p("갈등", verbose=True)
    assert out == "갈뜽", f"Expected '갈뜽', got '{out}'"
    assert "26" in rule_ids(rules)


def test_rule_26_sino_korean_fortis_2(g2p):
    out, rules, _ = g2p("발전", verbose=True)
    assert out == "발쩐", f"Expected '발쩐', got '{out}'"
    assert "26" in rule_ids(rules)


# ── Rule 27 ──────────────────────────────────────────────────────────────────
# Modifying -(으)ᆯ + plain obstruent → tensed

def test_rule_27_modifying_rieul(g2p):
    out, rules, _ = g2p("할수록", verbose=True)
    assert out == "할쑤록", f"Expected '할쑤록', got '{out}'"
    assert "27" in rule_ids(rules)


def test_rule_27_modifying_rieul_2(g2p):
    out, rules, _ = g2p("할지라도", verbose=True)
    assert out == "할찌라도", f"Expected '할찌라도', got '{out}'"
    assert "27" in rule_ids(rules)


# ── Rule 28 ──────────────────────────────────────────────────────────────────
# Native compound nouns without saisiot: onset of second element tensed

def test_rule_28_compound_tensification(g2p):
    out, rules, _ = g2p("문고리", verbose=True)
    assert out == "문꼬리", f"Expected '문꼬리', got '{out}'"
    assert "28" in rule_ids(rules)


def test_rule_28_compound_tensification_2(g2p):
    out, rules, _ = g2p("눈동자", verbose=True)
    assert out == "눈똥자", f"Expected '눈똥자', got '{out}'"
    assert "28" in rule_ids(rules)


# ── Rule 29 ──────────────────────────────────────────────────────────────────
# ᄂ insertion: compound where first morpheme ends in consonant,
# second morpheme starts with 이/야/여/요/유

def test_rule_29_n_insertion(g2p):
    out, rules, _ = g2p("솜이불", verbose=True)
    assert out == "솜니불", f"Expected '솜니불', got '{out}'"
    assert "29" in rule_ids(rules)


def test_rule_29_n_insertion_2(g2p):
    out, rules, _ = g2p("담요", verbose=True)
    assert out == "담뇨", f"Expected '담뇨', got '{out}'"
    assert "29" in rule_ids(rules)


# ── Rule 30.1 ────────────────────────────────────────────────────────────────
# 사이시옷 + plain obstruent → tensed

def test_rule_30_1_saisiot_tensification(g2p):
    out, rules, _ = g2p("냇가", verbose=True)
    assert out == "내까", f"Expected '내까', got '{out}'"
    assert "30.1" in rule_ids(rules)


def test_rule_30_1_saisiot_tensification_2(g2p):
    out, rules, _ = g2p("햇살", verbose=True)
    assert out == "해쌀", f"Expected '해쌀', got '{out}'"
    assert "30.1" in rule_ids(rules)


# ── Rule 30.2 ────────────────────────────────────────────────────────────────
# 사이시옷 + ᄂ/ᄆ → [ᄂ] insertion

def test_rule_30_2_saisiot_nasal(g2p):
    out, rules, _ = g2p("콧날", verbose=True)
    assert out == "콘날", f"Expected '콘날', got '{out}'"
    assert "30.2" in rule_ids(rules)


def test_rule_30_2_saisiot_nasal_2(g2p):
    out, rules, _ = g2p("뱃머리", verbose=True)
    assert out == "밴머리", f"Expected '밴머리', got '{out}'"
    assert "30.2" in rule_ids(rules)


# ── Rule 30.3 ────────────────────────────────────────────────────────────────
# 사이시옷 + vowel-initial second element → [ᄂᄂ] insertion

def test_rule_30_3_saisiot_vowel(g2p):
    out, rules, _ = g2p("깻잎", verbose=True)
    assert out == "깬닙", f"Expected '깬닙', got '{out}'"
    assert "30.3" in rule_ids(rules)


def test_rule_30_3_saisiot_vowel_2(g2p):
    out, rules, _ = g2p("나뭇잎", verbose=True)
    assert out == "나문닙", f"Expected '나문닙', got '{out}'"
    assert "30.3" in rule_ids(rules)
