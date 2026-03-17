"""Difficulty ranker identifying hardest sounds per native language."""

from __future__ import annotations

from accentcoach.models import DifficultyProfile, NativeLanguage


class DifficultyRanker:
    """Rank English phonemes by difficulty for speakers of different native languages."""

    PROFILES: dict[NativeLanguage, DifficultyProfile] = {
        NativeLanguage.SPANISH: DifficultyProfile(
            native_language=NativeLanguage.SPANISH,
            difficult_phonemes=["\u03b8", "\u00f0", "\u0292", "\u0283", "\u028c", "z", "v", "\u014b", "d\u0292", "j"],
            confusion_pairs=[
                ("v", "b"), ("\u03b8", "s"), ("\u00f0", "d"), ("z", "s"),
                ("\u0283", "t\u0283"), ("\u028c", "\u0251\u02d0"), ("j", "d\u0292"),
            ],
            tips=[
                "Spanish has no /v/ sound; practice distinguishing /v/ (teeth on lip) from /b/ (both lips).",
                "The /\u03b8/ and /\u00f0/ sounds do not exist in most Latin American Spanish.",
                "English /z/ is voiced, unlike Spanish /s/.",
            ],
        ),
        NativeLanguage.MANDARIN: DifficultyProfile(
            native_language=NativeLanguage.MANDARIN,
            difficult_phonemes=["\u03b8", "\u00f0", "\u0279", "v", "l", "n", "\u014b", "\u0292"],
            confusion_pairs=[
                ("\u03b8", "s"), ("\u00f0", "d"), ("\u0279", "l"), ("v", "w"),
                ("n", "l"), ("l", "\u0279"),
            ],
            tips=[
                "English /\u0279/ is very different from Mandarin r-sound; curl the tongue tip back.",
                "Distinguish /l/ (tongue touches ridge) from /n/ (air through nose).",
                "/\u03b8/ and /\u00f0/ do not exist in Mandarin; practice tongue-between-teeth position.",
            ],
        ),
        NativeLanguage.HINDI: DifficultyProfile(
            native_language=NativeLanguage.HINDI,
            difficult_phonemes=["\u03b8", "\u00f0", "\u00e6", "\u0252", "\u0254\u02d0", "\u025c\u02d0"],
            confusion_pairs=[
                ("\u03b8", "t"), ("\u00f0", "d"), ("\u00e6", "e"),
                ("v", "w"), ("\u0252", "\u0254\u02d0"),
            ],
            tips=[
                "English /\u03b8/ and /\u00f0/ are dental fricatives, not stops.",
                "English /v/ uses teeth on lip; Hindi /w/ and /v/ overlap.",
                "Distinguish the vowels in 'cat' /\u00e6/, 'cot' /\u0252/, and 'caught' /\u0254\u02d0/.",
            ],
        ),
        NativeLanguage.ARABIC: DifficultyProfile(
            native_language=NativeLanguage.ARABIC,
            difficult_phonemes=["p", "v", "\u014b", "t\u0283", "\u0259", "\u025c\u02d0", "\u00e6"],
            confusion_pairs=[
                ("p", "b"), ("v", "f"), ("t\u0283", "\u0283"),
                ("\u00e6", "\u0251\u02d0"),
            ],
            tips=[
                "English /p/ is voiceless; Arabic doesn't distinguish /p/ from /b/.",
                "Practice /v/ (voiced, teeth on lip) vs /f/ (voiceless).",
                "The schwa /\u0259/ is very common in English unstressed syllables.",
            ],
        ),
        NativeLanguage.JAPANESE: DifficultyProfile(
            native_language=NativeLanguage.JAPANESE,
            difficult_phonemes=["\u03b8", "\u00f0", "\u0279", "l", "v", "f", "\u00e6", "si", "\u028c"],
            confusion_pairs=[
                ("\u0279", "l"), ("\u03b8", "s"), ("v", "b"), ("f", "h"),
                ("l", "\u0279"), ("\u00e6", "\u0251\u02d0"),
            ],
            tips=[
                "The /\u0279/-/l/ distinction is critical: /l/ touches the ridge, /\u0279/ curls back.",
                "English /f/ uses teeth on lip; Japanese fu is bilabial.",
                "/\u03b8/ requires tongue between teeth, not /s/.",
            ],
        ),
        NativeLanguage.KOREAN: DifficultyProfile(
            native_language=NativeLanguage.KOREAN,
            difficult_phonemes=["\u03b8", "\u00f0", "\u0279", "l", "f", "v", "z", "\u00e6"],
            confusion_pairs=[
                ("\u0279", "l"), ("f", "p"), ("v", "b"), ("z", "s"),
                ("\u03b8", "s"),
            ],
            tips=[
                "Korean does not distinguish /\u0279/ from /l/; practice minimal pairs like 'right'/'light'.",
                "/f/ uses teeth on lower lip, unlike Korean /p/.",
                "/z/ is voiced /s/; feel the vibration in your throat.",
            ],
        ),
        NativeLanguage.FRENCH: DifficultyProfile(
            native_language=NativeLanguage.FRENCH,
            difficult_phonemes=["\u03b8", "\u00f0", "h", "\u014b", "\u00e6", "\u028c"],
            confusion_pairs=[
                ("\u03b8", "s"), ("\u00f0", "z"), ("h", "(silent)"),
                ("\u00e6", "e"),
            ],
            tips=[
                "English /h/ must be pronounced; it is not silent as in French.",
                "/\u03b8/ and /\u00f0/ require tongue between teeth.",
                "Distinguish /\u00e6/ (open, as in 'cat') from /e/ (as in 'bed').",
            ],
        ),
        NativeLanguage.GERMAN: DifficultyProfile(
            native_language=NativeLanguage.GERMAN,
            difficult_phonemes=["\u03b8", "\u00f0", "w", "\u00e6", "\u028c"],
            confusion_pairs=[
                ("\u03b8", "s"), ("\u00f0", "d"), ("w", "v"),
                ("\u00e6", "e"),
            ],
            tips=[
                "English /w/ rounds the lips; German /w/ is pronounced as /v/.",
                "Practice /\u03b8/ with tongue between teeth, not /s/ or /f/.",
            ],
        ),
        NativeLanguage.PORTUGUESE: DifficultyProfile(
            native_language=NativeLanguage.PORTUGUESE,
            difficult_phonemes=["\u03b8", "\u00f0", "\u00e6", "\u028c", "h"],
            confusion_pairs=[
                ("\u03b8", "t"), ("\u00f0", "d"), ("\u00e6", "\u0251\u02d0"),
            ],
            tips=[
                "English /\u03b8/ and /\u00f0/ are dental fricatives.",
                "The /h/ sound is always pronounced at the start of words in English.",
            ],
        ),
        NativeLanguage.RUSSIAN: DifficultyProfile(
            native_language=NativeLanguage.RUSSIAN,
            difficult_phonemes=["\u03b8", "\u00f0", "w", "\u00e6", "\u014b", "\u0279"],
            confusion_pairs=[
                ("\u03b8", "s"), ("\u00f0", "z"), ("w", "v"),
                ("\u00e6", "e"), ("\u0279", "r"),
            ],
            tips=[
                "English /w/ is a labial-velar glide, not Russian /v/.",
                "English /\u0279/ is an approximant, not a trill or tap.",
            ],
        ),
        NativeLanguage.ITALIAN: DifficultyProfile(
            native_language=NativeLanguage.ITALIAN,
            difficult_phonemes=["\u03b8", "\u00f0", "\u00e6", "\u028c", "\u0259", "h", "\u014b"],
            confusion_pairs=[
                ("\u03b8", "t"), ("\u00f0", "d"), ("\u00e6", "e"), ("h", "(silent)"),
            ],
            tips=[
                "English /h/ must be pronounced at the start of words.",
                "The schwa /\u0259/ appears in many unstressed English syllables.",
            ],
        ),
        NativeLanguage.TURKISH: DifficultyProfile(
            native_language=NativeLanguage.TURKISH,
            difficult_phonemes=["\u03b8", "\u00f0", "\u00e6", "\u028c", "w"],
            confusion_pairs=[("\u03b8", "t"), ("\u00f0", "d"), ("w", "v")],
            tips=["Practice /\u03b8/ and /\u00f0/ with tongue between teeth."],
        ),
        NativeLanguage.VIETNAMESE: DifficultyProfile(
            native_language=NativeLanguage.VIETNAMESE,
            difficult_phonemes=["\u03b8", "\u00f0", "\u0283", "\u0292", "d\u0292", "\u00e6", "\u0279"],
            confusion_pairs=[("\u03b8", "t"), ("\u00f0", "d"), ("\u0283", "s")],
            tips=["English final consonants must be fully released, unlike Vietnamese."],
        ),
        NativeLanguage.THAI: DifficultyProfile(
            native_language=NativeLanguage.THAI,
            difficult_phonemes=["\u03b8", "\u00f0", "v", "z", "\u0279", "l", "\u00e6"],
            confusion_pairs=[("\u03b8", "t"), ("v", "w"), ("\u0279", "l"), ("z", "s")],
            tips=["Distinguish English /\u0279/ from /l/; they are separate phonemes."],
        ),
        NativeLanguage.POLISH: DifficultyProfile(
            native_language=NativeLanguage.POLISH,
            difficult_phonemes=["\u03b8", "\u00f0", "\u00e6", "\u028c", "\u0259"],
            confusion_pairs=[("\u03b8", "f"), ("\u00f0", "d"), ("\u00e6", "e")],
            tips=[
                "English /\u03b8/ is dental, not labiodental like /f/.",
                "Practice the schwa /\u0259/ in unstressed syllables.",
            ],
        ),
    }

    def get_profile(self, native_language: NativeLanguage) -> DifficultyProfile:
        """Get the difficulty profile for a native language."""
        return self.PROFILES[native_language]

    def rank_phonemes(self, native_language: NativeLanguage) -> list[str]:
        """Return phonemes ranked from hardest to easiest for the given native language."""
        profile = self.PROFILES[native_language]
        return list(profile.difficult_phonemes)

    def get_confusion_pairs(self, native_language: NativeLanguage) -> list[tuple[str, str]]:
        """Return commonly confused phoneme pairs."""
        return self.PROFILES[native_language].confusion_pairs

    def get_tips(self, native_language: NativeLanguage) -> list[str]:
        """Return pronunciation tips for the native language."""
        return self.PROFILES[native_language].tips

    def list_languages(self) -> list[NativeLanguage]:
        """List all supported native languages."""
        return list(self.PROFILES.keys())
