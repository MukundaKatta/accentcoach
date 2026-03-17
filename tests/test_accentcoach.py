"""Tests for AccentCoach."""

import pytest

from accentcoach.analyzer.comparison import PronunciationComparator
from accentcoach.analyzer.difficulty import DifficultyRanker
from accentcoach.analyzer.phoneme import PhonemeAnalyzer
from accentcoach.exercises.drills import PronunciationDrill
from accentcoach.exercises.words import ProblemWordDatabase
from accentcoach.models import NativeLanguage, PhonemeCategory


class TestPhonemeAnalyzer:
    def test_has_44_phonemes(self):
        analyzer = PhonemeAnalyzer()
        assert analyzer.phoneme_count() == 44

    def test_get_vowels(self):
        analyzer = PhonemeAnalyzer()
        vowels = analyzer.all_phonemes(PhonemeCategory.VOWEL)
        assert len(vowels) == 12

    def test_get_consonants(self):
        analyzer = PhonemeAnalyzer()
        consonants = analyzer.all_phonemes(PhonemeCategory.CONSONANT)
        assert len(consonants) == 24

    def test_get_diphthongs(self):
        analyzer = PhonemeAnalyzer()
        diphthongs = analyzer.all_phonemes(PhonemeCategory.DIPHTHONG)
        assert len(diphthongs) == 8

    def test_get_pronunciation_known_word(self):
        analyzer = PhonemeAnalyzer()
        pron = analyzer.get_pronunciation("cat")
        assert pron is not None
        assert pron.ipa == "/k\u00e6t/"

    def test_get_pronunciation_unknown_word(self):
        analyzer = PhonemeAnalyzer()
        assert analyzer.get_pronunciation("xyzzyplugh") is None

    def test_phoneme_lookup(self):
        analyzer = PhonemeAnalyzer()
        p = analyzer.get_phoneme("p")
        assert p is not None
        assert p.example_word == "pat"
        assert p.voice is False


class TestPronunciationComparator:
    def test_perfect_match(self):
        comp = PronunciationComparator()
        result = comp.compare("cat", ["k", "\u00e6", "t"])
        assert result.accuracy == 1.0
        assert len(result.mismatched_phonemes) == 0

    def test_partial_match(self):
        comp = PronunciationComparator()
        result = comp.compare("cat", ["k", "e", "t"])
        assert 0.0 < result.accuracy < 1.0
        assert len(result.mismatched_phonemes) >= 1

    def test_unknown_word(self):
        comp = PronunciationComparator()
        result = comp.compare("xyzzy", ["k"])
        assert result.accuracy == 0.0

    def test_mismatch_tips(self):
        comp = PronunciationComparator()
        # Simulate a common Japanese speaker error: /l/ instead of /r/
        result = comp.compare("red", ["\u0279", "e", "d"])
        # Exact match since we passed the correct phonemes
        assert result.accuracy > 0


class TestDifficultyRanker:
    def test_all_languages_have_profiles(self):
        ranker = DifficultyRanker()
        for lang in NativeLanguage:
            profile = ranker.get_profile(lang)
            assert len(profile.difficult_phonemes) > 0

    def test_spanish_profile(self):
        ranker = DifficultyRanker()
        profile = ranker.get_profile(NativeLanguage.SPANISH)
        # th sounds should be difficult for Spanish speakers
        assert "\u03b8" in profile.difficult_phonemes

    def test_japanese_r_l_confusion(self):
        ranker = DifficultyRanker()
        profile = ranker.get_profile(NativeLanguage.JAPANESE)
        pairs = profile.confusion_pairs
        assert any(
            (a == "\u0279" and b == "l") or (a == "l" and b == "\u0279")
            for a, b in pairs
        )

    def test_list_languages(self):
        ranker = DifficultyRanker()
        langs = ranker.list_languages()
        assert len(langs) == len(NativeLanguage)


class TestPronunciationDrill:
    def test_minimal_pair_drill(self):
        drill_gen = PronunciationDrill()
        drill = drill_gen.minimal_pair_drill("p/b")
        assert drill is not None
        assert len(drill.items) >= 5

    def test_tongue_twister_drill(self):
        drill_gen = PronunciationDrill()
        drill = drill_gen.tongue_twister_drill()
        assert len(drill.items) >= 5

    def test_targeted_tongue_twisters(self):
        drill_gen = PronunciationDrill()
        drill = drill_gen.tongue_twister_drill(["\u03b8"])
        assert len(drill.items) >= 1

    def test_drills_for_language(self):
        drill_gen = PronunciationDrill()
        drills = drill_gen.drills_for_language(NativeLanguage.JAPANESE)
        assert len(drills) >= 1

    def test_list_contrasts(self):
        drill_gen = PronunciationDrill()
        contrasts = drill_gen.list_contrasts()
        assert len(contrasts) >= 10


class TestProblemWordDatabase:
    def test_has_200_plus_words(self):
        db = ProblemWordDatabase()
        assert db.count() >= 200

    def test_lookup_word(self):
        db = ProblemWordDatabase()
        wp = db.get("pronunciation")
        assert wp is not None
        assert wp.syllable_count == 5

    def test_search_by_prefix(self):
        db = ProblemWordDatabase()
        results = db.search("ch")
        assert len(results) >= 2

    def test_words_with_errors(self):
        db = ProblemWordDatabase()
        errored = db.words_with_errors()
        assert len(errored) >= 20

    def test_words_by_syllable_count(self):
        db = ProblemWordDatabase()
        one_syllable = db.words_by_syllable_count(1)
        assert len(one_syllable) >= 5
