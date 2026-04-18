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
 
@pytest.mark.parametrize("inp, expected", [
    ("가져", "가저"),
    ("다쳐", "다처"),
    ("쪄",   "쩌"),
])
def test_rule_5_1_jyeo(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "5.1" in rule_ids(rules)
 
 
# ── Rule 5.2 ─────────────────────────────────────────────────────────────────
# ㅖ → ㅔ after consonants (descriptive only)
 
@pytest.mark.parametrize("inp, expected", [
    ("시계", "시게"),
    ("혜택", "헤택"),
    ("지혜", "지헤"),
])
def test_rule_5_2_ye_descriptive(g2p, inp, expected):
    out, rules, _ = g2p(inp, descriptive=True, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "5.2" in rule_ids(rules)
 
 
# ── Rule 5.3 ─────────────────────────────────────────────────────────────────
# consonant + ㅢ → consonant + ㅣ
 
@pytest.mark.parametrize("inp, expected", [
    ("무늬", "무니"),
    ("희망", "히망"),
    ("유희", "유히"),
    ("씌어", "씨어"),
])
def test_rule_5_3_consonant_ui(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "5.3" in rule_ids(rules)
 
 
# ── Rule 5.4.1 ───────────────────────────────────────────────────────────────
# Non-initial 의 → 이 (descriptive only)
 
@pytest.mark.parametrize("inp, expected", [
    ("주의", "주이"),
    ("협의", "혀비"),
])
def test_rule_5_4_1_vowel_ui_descriptive(g2p, inp, expected):
    out, rules, _ = g2p(inp, descriptive=True, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "5.4.1" in rule_ids(rules)
 
 
# ── Rule 9 ───────────────────────────────────────────────────────────────────
# Coda neutralisation: ᆩᆿᆺᆻᆽᆾᇀᇂᇁ → representative ᆨᆮᆸ
 
@pytest.mark.parametrize("inp, expected", [
    ("닦다", "닥따"),
    ("앞",   "압"),
    ("젖",   "젇"),
    ("꽃",   "꼳"),
    ("덮다", "덥따"),
])
def test_rule_9_coda_neutralisation(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "9" in rule_ids(rules)
 
 
# ── Rule 10 ──────────────────────────────────────────────────────────────────
# Complex coda reduction: ᆪ→ᆨ, ᆬ→ᆫ, ᆲᆳᆴ→ᆯ, ᆹ→ᆸ at syllable coda
 
@pytest.mark.parametrize("inp, expected", [
    ("넋",   "넉"),
    ("앉다", "안따"),
    ("값",   "갑"),
    ("여덟", "여덜"),
])
def test_rule_10_complex_coda(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "10" in rule_ids(rules)
 
 
# ── Rule 10.1 ────────────────────────────────────────────────────────────────
# 밟- before consonant → ᆸ (exception to rule 10)
 
@pytest.mark.parametrize("inp, expected", [
    ("밟다", "밥따"),
    ("밟고", "밥꼬"),
    ("밟소", "밥쏘"),
])
def test_rule_10_1_balb(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "10.1" in rule_ids(rules)
 
 
# ── Rule 11 ──────────────────────────────────────────────────────────────────
# ᆰ→ᆨ, ᆱ→ᆷ, ᆵ→ᆸ in coda position
 
@pytest.mark.parametrize("inp, expected", [
    ("닭",   "닥"),
    ("삶",   "삼"),
    ("맑다", "막따"),
    ("흙과", "흑꽈"),
])
def test_rule_11_complex_coda_rieul(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "11" in rule_ids(rules)
 
 
# ── Rule 11.1 ────────────────────────────────────────────────────────────────
# Verb stem ᆰ before ᄀ → ᆯ (exception: ᆰ/P + ᄀ → ᆯᄁ)
 
@pytest.mark.parametrize("inp, expected", [
    ("맑게",   "말께"),
    ("묽고",   "물꼬"),
    ("읽거나", "일꺼나"),
])
def test_rule_11_1_rieulgiyeok(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "11.1" in rule_ids(rules)
 
 
# ── Rule 12 ──────────────────────────────────────────────────────────────────
# ᇂ + ᄀ/ᄃ/ᄌ → aspiration ᄏ/ᄐ/ᄎ; also ᆨ/ᆮ/ᆸ + ᄒ → aspiration
 
@pytest.mark.parametrize("inp, expected", [
    ("놓고", "노코"),
    ("많고", "만코"),
    ("좋던", "조턴"),
    ("쌓지", "싸치"),
    ("각하", "가카"),
])
def test_rule_12_hieut_aspiration(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "12" in rule_ids(rules)
 
 
# ── Rule 12.4 ────────────────────────────────────────────────────────────────
# ᇂ (or ᆭ/ᆶ) + vowel-initial suffix → ᇂ is dropped
 
@pytest.mark.parametrize("inp, expected", [
    ("낳은",   "나은"),
    ("많아",   "마나"),
    ("놓아",   "노아"),
    ("싫어도", "시러도"),
])
def test_rule_12_4_hieut_drop(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "12.4" in rule_ids(rules)
 
 
# ── Rule 13 ──────────────────────────────────────────────────────────────────
# Simple coda + vowel-initial grammatical morpheme → liaison
 
@pytest.mark.parametrize("inp, expected", [
    ("옷이",   "오시"),
    ("있어",   "이써"),
    ("낮이",   "나지"),
    ("앞으로", "아프로"),
    ("깎아",   "까까"),
])
def test_rule_13_simple_liaison(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "13" in rule_ids(rules)
 
 
# ── Rule 14 ──────────────────────────────────────────────────────────────────
# Complex coda + vowel-initial grammatical morpheme → only second consonant liaises
 
@pytest.mark.parametrize("inp, expected", [
    ("넋이", "넉씨"),
    ("없어", "업써"),
    ("닭을", "달글"),
    ("값을", "갑쓸"),
    ("앉아", "안자"),
])
def test_rule_14_complex_liaison(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "14" in rule_ids(rules)
 
 
# ── Rule 15 ──────────────────────────────────────────────────────────────────
# Coda liaison before vowel-initial content morpheme (실질형태소)
 
@pytest.mark.parametrize("inp, expected", [
    ("맛없다", "마덥따"),
])
def test_rule_15_content_liaison(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "15" in rule_ids(rules)
 
 
# ── Rule 17 ──────────────────────────────────────────────────────────────────
# Palatalization: ᆮ/ᇀ + 이/야/여/요/유 → ᄌ/ᄎ
 
@pytest.mark.parametrize("inp, expected", [
    ("굳이",   "구지"),
    ("밭이",   "바치"),
    ("미닫이", "미다지"),
    ("굳히다", "구치다"),
])
def test_rule_17_palatalization(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "17" in rule_ids(rules)
 
 
# ── Rule 18 ──────────────────────────────────────────────────────────────────
# Nasalisation: ᆨᆮᆸ + ᄂ/ᄆ → ᆼᆫᆷ + ᄂ/ᄆ
 
@pytest.mark.parametrize("inp, expected", [
    ("먹는",   "멍는"),
    ("국물",   "궁물"),
    ("잡는",   "잠는"),
    ("밥물",   "밤물"),
    ("앞마당", "암마당"),
])
def test_rule_18_nasalisation(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "18" in rule_ids(rules)
 
 
# ── Rule 19 ──────────────────────────────────────────────────────────────────
# ᄅ → ᄂ after ᆷ/ᆼ (or ᆨ/ᆸ via 붙임)
 
@pytest.mark.parametrize("inp, expected", [
    ("강릉", "강능"),
    ("침략", "침냑"),
    ("항로", "항노"),
    ("협력", "혐녁"),
])
def test_rule_19_rieul_nasalisation(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "19" in rule_ids(rules)
 
 
# ── Rule 20 ──────────────────────────────────────────────────────────────────
# ᆫ + ᄅ or ᄅ + ᄂ → lateral assimilation [ᆯ+ᄅ]
 
@pytest.mark.parametrize("inp, expected", [
    ("신라", "실라"),
    ("난로", "날로"),
    ("천리", "철리"),
    ("칼날", "칼랄"),
])
def test_rule_20_lateralisation(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "20" in rule_ids(rules)
 
 
# ── Rule 23 ──────────────────────────────────────────────────────────────────
# Tensification: ᆨᆮᆸ + plain obstruent → tensed obstruent
 
@pytest.mark.parametrize("inp, expected", [
    ("국밥",   "국빱"),
    ("덮개",   "덥깨"),
    ("옆집",   "엽찝"),
    ("낯설다", "낟썰다"),
    ("깎다",   "깍따"),
])
def test_rule_23_tensification(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "23" in rule_ids(rules)
 
 
# ── Rule 24 ──────────────────────────────────────────────────────────────────
# Verb stem ᆫ(ᆬ)/ᆷ(ᆱ) + plain obstruent → tensed (된소리)
 
@pytest.mark.parametrize("inp, expected", [
    ("앉고",   "안꼬"),
    ("젊지",   "점찌"),
    ("얹다",   "언따"),
    ("더듬지", "더듬찌"),
    ("닮고",   "담꼬"),
])
def test_rule_24_verb_tensification(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "24" in rule_ids(rules)
 
 
# ── Rule 25 ──────────────────────────────────────────────────────────────────
# Verb stem ᆲ/ᆴ + plain obstruent → tensed
 
@pytest.mark.parametrize("inp, expected", [
    ("넓게", "널께"),
    ("핥다", "할따"),
    ("훑소", "훌쏘"),
    ("떫지", "떨찌"),
])
def test_rule_25_rieulbieub_tensification(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "25" in rule_ids(rules)
 
 
# ── Rule 26 ──────────────────────────────────────────────────────────────────
# Sino-Korean: ᆯ + ᄃ/ᄉ/ᄌ → tensed (된소리)
 
@pytest.mark.parametrize("inp, expected", [
    ("갈등", "갈뜽"),
    ("발전", "발쩐"),
    ("말살", "말쌀"),
    ("물질", "물찔"),
    ("절도", "절또"),
])
def test_rule_26_sino_korean_fortis(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "26" in rule_ids(rules)
 
 
# ── Rule 27 ──────────────────────────────────────────────────────────────────
# Modifying -(으)ᆯ + plain obstruent → tensed
 
@pytest.mark.parametrize("inp, expected", [
    ("할수록",   "할쑤록"),
    ("할지라도", "할찌라도"),
    ("할걸",     "할껄"),
    ("할밖에",   "할빠께"),
    ("할세라",   "할쎄라"),
])
def test_rule_27_modifying_rieul(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "27" in rule_ids(rules)
 
 
# ── Rule 28 ──────────────────────────────────────────────────────────────────
# Native compound nouns without saisiot: onset of second element tensed
 
@pytest.mark.parametrize("inp, expected", [
    ("문고리", "문꼬리"),
    ("눈동자", "눈똥자"),
    ("신바람", "신빠람"),
    ("길가",   "길까"),
    ("술잔",   "술짠"),
])
def test_rule_28_compound_tensification(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "28" in rule_ids(rules)
 
 
# ── Rule 29 ──────────────────────────────────────────────────────────────────
# ᄂ insertion: compound where first morpheme ends in consonant,
# second morpheme starts with 이/야/여/요/유
 
@pytest.mark.parametrize("inp, expected", [
    ("솜이불", "솜니불"),
    ("담요",   "담뇨"),
    ("꽃잎",   "꼰닙"),
    ("색연필", "생년필"),
    ("막일",   "망닐"),
])
def test_rule_29_n_insertion(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "29" in rule_ids(rules)
 
 
# ── Rule 30.1 ────────────────────────────────────────────────────────────────
# 사이시옷 + plain obstruent → tensed
 
@pytest.mark.parametrize("inp, expected", [
    ("냇가",   "내까"),
    ("햇살",   "해쌀"),
    ("샛길",   "새낄"),
    ("뱃속",   "배쏙"),
    ("깃발",   "기빨"),
])
def test_rule_30_1_saisiot_tensification(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "30.1" in rule_ids(rules)
 
 
# ── Rule 30.2 ────────────────────────────────────────────────────────────────
# 사이시옷 + ᄂ/ᄆ → [ᄂ] insertion
 
@pytest.mark.parametrize("inp, expected", [
    ("콧날",   "콘날"),
    ("뱃머리", "밴머리"),
    ("아랫니", "아랜니"),
    ("툇마루", "퇸마루"),
])
def test_rule_30_2_saisiot_nasal(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "30.2" in rule_ids(rules)
 
 
# ── Rule 30.3 ────────────────────────────────────────────────────────────────
# 사이시옷 + vowel-initial second element → [ᄂᄂ] insertion
 
@pytest.mark.parametrize("inp, expected", [
    ("깻잎",     "깬닙"),
    ("나뭇잎",   "나문닙"),
    ("도리깻열", "도리깬녈"),
])
def test_rule_30_3_saisiot_vowel(g2p, inp, expected):
    out, rules, _ = g2p(inp, verbose=True)
    assert out == expected, f"Expected '{expected}', got '{out}'"
    assert "30.3" in rule_ids(rules)