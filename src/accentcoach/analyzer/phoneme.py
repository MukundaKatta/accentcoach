"""Phoneme analyzer mapping words to IPA phonemes with 44 English phonemes."""

from __future__ import annotations

from accentcoach.models import Phoneme, PhonemeCategory, WordPronunciation


class PhonemeAnalyzer:
    """Map English words to IPA phonemes using a built-in dictionary."""

    # Complete 44-phoneme chart for General American English
    PHONEMES: dict[str, Phoneme] = {
        # --- Consonants (24) ---
        "p": Phoneme(ipa="p", category=PhonemeCategory.CONSONANT, example_word="pat", description="voiceless bilabial plosive", voice=False),
        "b": Phoneme(ipa="b", category=PhonemeCategory.CONSONANT, example_word="bat", description="voiced bilabial plosive"),
        "t": Phoneme(ipa="t", category=PhonemeCategory.CONSONANT, example_word="tap", description="voiceless alveolar plosive", voice=False),
        "d": Phoneme(ipa="d", category=PhonemeCategory.CONSONANT, example_word="dog", description="voiced alveolar plosive"),
        "k": Phoneme(ipa="k", category=PhonemeCategory.CONSONANT, example_word="cat", description="voiceless velar plosive", voice=False),
        "\u0261": Phoneme(ipa="\u0261", category=PhonemeCategory.CONSONANT, example_word="go", description="voiced velar plosive"),
        "f": Phoneme(ipa="f", category=PhonemeCategory.CONSONANT, example_word="fan", description="voiceless labiodental fricative", voice=False),
        "v": Phoneme(ipa="v", category=PhonemeCategory.CONSONANT, example_word="van", description="voiced labiodental fricative"),
        "\u03b8": Phoneme(ipa="\u03b8", category=PhonemeCategory.CONSONANT, example_word="think", description="voiceless dental fricative", voice=False),
        "\u00f0": Phoneme(ipa="\u00f0", category=PhonemeCategory.CONSONANT, example_word="this", description="voiced dental fricative"),
        "s": Phoneme(ipa="s", category=PhonemeCategory.CONSONANT, example_word="sit", description="voiceless alveolar fricative", voice=False),
        "z": Phoneme(ipa="z", category=PhonemeCategory.CONSONANT, example_word="zoo", description="voiced alveolar fricative"),
        "\u0283": Phoneme(ipa="\u0283", category=PhonemeCategory.CONSONANT, example_word="ship", description="voiceless postalveolar fricative", voice=False),
        "\u0292": Phoneme(ipa="\u0292", category=PhonemeCategory.CONSONANT, example_word="measure", description="voiced postalveolar fricative"),
        "h": Phoneme(ipa="h", category=PhonemeCategory.CONSONANT, example_word="hat", description="voiceless glottal fricative", voice=False),
        "t\u0283": Phoneme(ipa="t\u0283", category=PhonemeCategory.CONSONANT, example_word="church", description="voiceless postalveolar affricate", voice=False),
        "d\u0292": Phoneme(ipa="d\u0292", category=PhonemeCategory.CONSONANT, example_word="judge", description="voiced postalveolar affricate"),
        "m": Phoneme(ipa="m", category=PhonemeCategory.CONSONANT, example_word="map", description="bilabial nasal"),
        "n": Phoneme(ipa="n", category=PhonemeCategory.CONSONANT, example_word="nap", description="alveolar nasal"),
        "\u014b": Phoneme(ipa="\u014b", category=PhonemeCategory.CONSONANT, example_word="sing", description="velar nasal"),
        "l": Phoneme(ipa="l", category=PhonemeCategory.CONSONANT, example_word="lip", description="alveolar lateral approximant"),
        "\u0279": Phoneme(ipa="\u0279", category=PhonemeCategory.CONSONANT, example_word="red", description="alveolar approximant"),
        "w": Phoneme(ipa="w", category=PhonemeCategory.CONSONANT, example_word="wet", description="labial-velar approximant"),
        "j": Phoneme(ipa="j", category=PhonemeCategory.CONSONANT, example_word="yes", description="palatal approximant"),
        # --- Monophthong Vowels (12) ---
        "i\u02d0": Phoneme(ipa="i\u02d0", category=PhonemeCategory.VOWEL, example_word="see", description="close front unrounded"),
        "\u026a": Phoneme(ipa="\u026a", category=PhonemeCategory.VOWEL, example_word="sit", description="near-close near-front unrounded"),
        "e": Phoneme(ipa="e", category=PhonemeCategory.VOWEL, example_word="bed", description="close-mid front unrounded"),
        "\u00e6": Phoneme(ipa="\u00e6", category=PhonemeCategory.VOWEL, example_word="cat", description="near-open front unrounded"),
        "\u0251\u02d0": Phoneme(ipa="\u0251\u02d0", category=PhonemeCategory.VOWEL, example_word="car", description="open back unrounded"),
        "\u0252": Phoneme(ipa="\u0252", category=PhonemeCategory.VOWEL, example_word="lot", description="open back rounded"),
        "\u0254\u02d0": Phoneme(ipa="\u0254\u02d0", category=PhonemeCategory.VOWEL, example_word="thought", description="open-mid back rounded"),
        "\u028a": Phoneme(ipa="\u028a", category=PhonemeCategory.VOWEL, example_word="put", description="near-close near-back rounded"),
        "u\u02d0": Phoneme(ipa="u\u02d0", category=PhonemeCategory.VOWEL, example_word="too", description="close back rounded"),
        "\u028c": Phoneme(ipa="\u028c", category=PhonemeCategory.VOWEL, example_word="cup", description="open-mid back unrounded"),
        "\u025c\u02d0": Phoneme(ipa="\u025c\u02d0", category=PhonemeCategory.VOWEL, example_word="bird", description="open-mid central unrounded"),
        "\u0259": Phoneme(ipa="\u0259", category=PhonemeCategory.VOWEL, example_word="about", description="mid central (schwa)"),
        # --- Diphthongs (8) ---
        "e\u026a": Phoneme(ipa="e\u026a", category=PhonemeCategory.DIPHTHONG, example_word="say", description="closing front diphthong"),
        "a\u026a": Phoneme(ipa="a\u026a", category=PhonemeCategory.DIPHTHONG, example_word="my", description="closing front diphthong"),
        "\u0254\u026a": Phoneme(ipa="\u0254\u026a", category=PhonemeCategory.DIPHTHONG, example_word="boy", description="closing front diphthong"),
        "\u0259\u028a": Phoneme(ipa="\u0259\u028a", category=PhonemeCategory.DIPHTHONG, example_word="go", description="closing back diphthong"),
        "a\u028a": Phoneme(ipa="a\u028a", category=PhonemeCategory.DIPHTHONG, example_word="now", description="closing back diphthong"),
        "\u026a\u0259": Phoneme(ipa="\u026a\u0259", category=PhonemeCategory.DIPHTHONG, example_word="near", description="centring diphthong"),
        "e\u0259": Phoneme(ipa="e\u0259", category=PhonemeCategory.DIPHTHONG, example_word="hair", description="centring diphthong"),
        "\u028a\u0259": Phoneme(ipa="\u028a\u0259", category=PhonemeCategory.DIPHTHONG, example_word="tour", description="centring diphthong"),
    }

    # Word -> IPA transcription dictionary (subset for demo)
    WORD_IPA: dict[str, str] = {
        "the": "/\u00f0\u0259/",
        "hello": "/h\u0259\u02c8l\u0259\u028a/",
        "world": "/w\u025c\u02d0ld/",
        "think": "/\u03b8\u026a\u014bk/",
        "this": "/\u00f0\u026as/",
        "cat": "/k\u00e6t/",
        "dog": "/d\u0252\u0261/",
        "ship": "/\u0283\u026ap/",
        "sheep": "/\u0283i\u02d0p/",
        "bit": "/b\u026at/",
        "beat": "/bi\u02d0t/",
        "sit": "/s\u026at/",
        "seat": "/si\u02d0t/",
        "full": "/f\u028al/",
        "fool": "/fu\u02d0l/",
        "bed": "/bed/",
        "bad": "/b\u00e6d/",
        "hat": "/h\u00e6t/",
        "hot": "/h\u0252t/",
        "put": "/p\u028at/",
        "putt": "/p\u028ct/",
        "cup": "/k\u028cp/",
        "bird": "/b\u025c\u02d0d/",
        "about": "/\u0259\u02c8ba\u028at/",
        "church": "/t\u0283\u025c\u02d0t\u0283/",
        "judge": "/d\u0292\u028cd\u0292/",
        "sing": "/s\u026a\u014b/",
        "red": "/\u0279ed/",
        "yes": "/jes/",
        "wet": "/wet/",
        "measure": "/\u02c8me\u0292\u0259/",
        "thought": "/\u03b8\u0254\u02d0t/",
        "three": "/\u03b8\u0279i\u02d0/",
        "father": "/\u02c8f\u0251\u02d0\u00f0\u0259/",
        "mother": "/\u02c8m\u028c\u00f0\u0259/",
        "water": "/\u02c8w\u0254\u02d0t\u0259/",
        "butter": "/\u02c8b\u028ct\u0259/",
        "teacher": "/\u02c8ti\u02d0t\u0283\u0259/",
        "student": "/\u02c8stju\u02d0d\u0259nt/",
        "language": "/\u02c8l\u00e6\u014b\u0261w\u026ad\u0292/",
        "pronunciation": "/p\u0279\u0259\u02ccn\u028cns\u026a\u02c8e\u026a\u0283\u0259n/",
    }

    def __init__(self) -> None:
        self._phoneme_list = list(self.PHONEMES.values())

    def get_phoneme(self, ipa: str) -> Phoneme | None:
        """Look up a phoneme by IPA symbol."""
        return self.PHONEMES.get(ipa)

    def get_pronunciation(self, word: str) -> WordPronunciation | None:
        """Get the IPA pronunciation for a word."""
        word_lower = word.lower().strip()
        ipa = self.WORD_IPA.get(word_lower)
        if ipa is None:
            return None

        phonemes = self._extract_phonemes(ipa)
        syllables = max(1, ipa.count("\u02c8") + ipa.count("\u02cc") + 1) if "\u02c8" in ipa else 1

        return WordPronunciation(
            word=word_lower,
            ipa=ipa,
            phonemes=phonemes,
            syllable_count=syllables,
        )

    def _extract_phonemes(self, ipa: str) -> list[str]:
        """Extract individual phoneme symbols from an IPA transcription."""
        # Remove slashes and stress marks
        cleaned = ipa.strip("/").replace("\u02c8", "").replace("\u02cc", "")
        phonemes: list[str] = []
        i = 0
        while i < len(cleaned):
            # Try two-character phonemes first (affricates, diphthongs, long vowels)
            if i + 1 < len(cleaned):
                digraph = cleaned[i : i + 2]
                if digraph in self.PHONEMES:
                    phonemes.append(digraph)
                    i += 2
                    continue
            # Single character
            ch = cleaned[i]
            if ch in self.PHONEMES:
                phonemes.append(ch)
            i += 1
        return phonemes

    def all_phonemes(self, category: PhonemeCategory | None = None) -> list[Phoneme]:
        """List all phonemes, optionally filtered by category."""
        if category is None:
            return list(self._phoneme_list)
        return [p for p in self._phoneme_list if p.category == category]

    def phoneme_count(self) -> int:
        """Return total number of phonemes in the chart."""
        return len(self.PHONEMES)
