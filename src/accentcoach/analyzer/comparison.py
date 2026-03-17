"""Pronunciation comparator comparing user vs reference pronunciation."""

from __future__ import annotations

from accentcoach.analyzer.phoneme import PhonemeAnalyzer
from accentcoach.models import PronunciationComparison


class PronunciationComparator:
    """Compare a user's phoneme sequence against the reference pronunciation."""

    def __init__(self, analyzer: PhonemeAnalyzer | None = None) -> None:
        self.analyzer = analyzer or PhonemeAnalyzer()

    def compare(self, word: str, user_phonemes: list[str]) -> PronunciationComparison:
        """Compare user phoneme input to the reference for the given word."""
        ref = self.analyzer.get_pronunciation(word)
        if ref is None:
            return PronunciationComparison(
                word=word,
                reference_ipa="(unknown)",
                user_ipa=" ".join(user_phonemes),
                accuracy=0.0,
                feedback=[f"Word '{word}' not found in dictionary."],
            )

        ref_phonemes = ref.phonemes
        matching: list[str] = []
        mismatched: list[tuple[str, str]] = []
        feedback: list[str] = []

        # Align by index (simple positional comparison)
        max_len = max(len(ref_phonemes), len(user_phonemes))
        for i in range(max_len):
            ref_p = ref_phonemes[i] if i < len(ref_phonemes) else "(none)"
            usr_p = user_phonemes[i] if i < len(user_phonemes) else "(none)"

            if ref_p == usr_p:
                matching.append(ref_p)
            else:
                mismatched.append((ref_p, usr_p))
                tip = self._mismatch_tip(ref_p, usr_p)
                if tip:
                    feedback.append(tip)

        if len(user_phonemes) != len(ref_phonemes):
            feedback.append(
                f"Expected {len(ref_phonemes)} phonemes but got {len(user_phonemes)}."
            )

        accuracy = len(matching) / max(max_len, 1)

        if accuracy == 1.0:
            feedback.append("Perfect pronunciation!")
        elif accuracy >= 0.8:
            feedback.append("Very close! Minor adjustments needed.")
        elif accuracy >= 0.5:
            feedback.append("Good attempt. Focus on the mismatched sounds.")
        else:
            feedback.append("Needs practice. Try listening to the reference again.")

        return PronunciationComparison(
            word=word,
            reference_ipa=ref.ipa,
            user_ipa=" ".join(user_phonemes),
            matching_phonemes=matching,
            mismatched_phonemes=mismatched,
            accuracy=round(accuracy, 3),
            feedback=feedback,
        )

    @staticmethod
    def _mismatch_tip(expected: str, actual: str) -> str | None:
        """Provide a tip for a specific phoneme mismatch."""
        tips: dict[tuple[str, str], str] = {
            ("\u03b8", "t"): "For /\u03b8/, place your tongue between your teeth and blow air, not as /t/.",
            ("\u03b8", "s"): "For /\u03b8/, use the tongue between teeth, not the /s/ behind teeth.",
            ("\u00f0", "d"): "For /\u00f0/, tongue between teeth with voicing, not /d/.",
            ("\u00f0", "z"): "For /\u00f0/, tongue tip between teeth, not /z/.",
            ("\u0279", "l"): "English /\u0279/ curls the tongue tip back; /l/ touches the ridge.",
            ("\u0279", "\u0261"): "English /\u0279/ is a tongue-back approximant, not a stop like /\u0261/.",
            ("v", "b"): "For /v/, use upper teeth on lower lip, not both lips together.",
            ("v", "w"): "For /v/, teeth on lip with friction; /w/ is a glide with rounded lips.",
            ("\u00e6", "e"): "Open your mouth wider for /\u00e6/ (as in 'cat') vs /e/ (as in 'bed').",
            ("\u028c", "\u0259"): "/\u028c/ is stressed (as in 'cup'); /\u0259/ is unstressed (as in 'about').",
            ("i\u02d0", "\u026a"): "Hold /i\u02d0/ longer and tense your tongue more than for /\u026a/.",
            ("u\u02d0", "\u028a"): "Hold /u\u02d0/ longer and round lips more than for /\u028a/.",
            ("\u014b", "n"): "For /\u014b/, the back of your tongue touches the soft palate, not the ridge.",
        }
        return tips.get((expected, actual))

    def compare_ipa_string(self, word: str, user_ipa: str) -> PronunciationComparison:
        """Compare using a raw IPA string from the user."""
        phonemes = self.analyzer._extract_phonemes(user_ipa)
        return self.compare(word, phonemes)
