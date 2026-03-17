"""Data models for AccentCoach."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class PhonemeCategory(str, Enum):
    VOWEL = "vowel"
    CONSONANT = "consonant"
    DIPHTHONG = "diphthong"


class Phoneme(BaseModel):
    """An IPA phoneme with metadata."""

    ipa: str = Field(description="IPA symbol")
    category: PhonemeCategory
    example_word: str = Field(description="Example word containing this phoneme")
    description: str = Field(default="", description="Articulatory description")
    voice: bool = Field(default=True, description="Whether the phoneme is voiced")


class WordPronunciation(BaseModel):
    """Pronunciation data for a word."""

    word: str
    ipa: str = Field(description="IPA transcription")
    phonemes: list[str] = Field(description="List of IPA phoneme symbols")
    syllable_count: int = 1
    stress_pattern: str = Field(default="", description="e.g. '1-0' for 2-syllable with stress on first")
    difficulty: float = Field(default=0.5, ge=0.0, le=1.0)
    common_errors: list[str] = Field(default_factory=list, description="Frequently confused pronunciations")


class PronunciationComparison(BaseModel):
    """Result of comparing user pronunciation with reference."""

    word: str
    reference_ipa: str
    user_ipa: str
    matching_phonemes: list[str] = Field(default_factory=list)
    mismatched_phonemes: list[tuple[str, str]] = Field(
        default_factory=list, description="List of (expected, actual) mismatches"
    )
    accuracy: float = Field(ge=0.0, le=1.0)
    feedback: list[str] = Field(default_factory=list)


class NativeLanguage(str, Enum):
    SPANISH = "spanish"
    MANDARIN = "mandarin"
    HINDI = "hindi"
    ARABIC = "arabic"
    JAPANESE = "japanese"
    KOREAN = "korean"
    FRENCH = "french"
    GERMAN = "german"
    PORTUGUESE = "portuguese"
    RUSSIAN = "russian"
    ITALIAN = "italian"
    TURKISH = "turkish"
    VIETNAMESE = "vietnamese"
    THAI = "thai"
    POLISH = "polish"


class DifficultyProfile(BaseModel):
    """Phonemes that are difficult for speakers of a given native language."""

    native_language: NativeLanguage
    difficult_phonemes: list[str] = Field(description="IPA symbols that are hard")
    confusion_pairs: list[tuple[str, str]] = Field(
        default_factory=list, description="Commonly confused phoneme pairs"
    )
    tips: list[str] = Field(default_factory=list)


class DrillType(str, Enum):
    MINIMAL_PAIR = "minimal_pair"
    TONGUE_TWISTER = "tongue_twister"
    WORD_LIST = "word_list"


class Drill(BaseModel):
    """A pronunciation drill exercise."""

    drill_type: DrillType
    target_phonemes: list[str]
    items: list[str] = Field(description="Words, pairs, or tongue twisters")
    instructions: str = ""
    difficulty: float = Field(default=0.5, ge=0.0, le=1.0)


class PracticeSession(BaseModel):
    """A practice session summary."""

    words_practiced: int = 0
    accuracy_scores: list[float] = Field(default_factory=list)
    problem_phonemes: list[str] = Field(default_factory=list)
    drills_completed: int = 0

    @property
    def average_accuracy(self) -> float:
        if not self.accuracy_scores:
            return 0.0
        return sum(self.accuracy_scores) / len(self.accuracy_scores)
