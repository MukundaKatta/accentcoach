"""Pronunciation drills with minimal pairs and tongue twisters."""

from __future__ import annotations

from accentcoach.models import Drill, DrillType, NativeLanguage


class PronunciationDrill:
    """Generate targeted pronunciation drills."""

    # Minimal pairs organised by target phoneme contrast
    MINIMAL_PAIRS: dict[str, list[tuple[str, str]]] = {
        # Vowel contrasts
        "i\u02d0/\u026a": [("sheep", "ship"), ("beat", "bit"), ("seat", "sit"), ("feel", "fill"),
                  ("heat", "hit"), ("meal", "mill"), ("peel", "pill"), ("steal", "still")],
        "e/\u00e6": [("bed", "bad"), ("pen", "pan"), ("men", "man"), ("set", "sat"),
                ("bet", "bat"), ("head", "had"), ("lend", "land"), ("send", "sand")],
        "\u028a/u\u02d0": [("full", "fool"), ("pull", "pool"), ("look", "Luke"), ("should", "shooed"),
                  ("wood", "wooed"), ("good", "gooed"), ("foot", "food"), ("book", "boo")],
        "\u028c/\u0251\u02d0": [("cup", "cop"), ("hut", "hot"), ("but", "bot"), ("luck", "lock"),
                   ("nut", "not"), ("cut", "cot"), ("bun", "bon"), ("duck", "dock")],
        # Consonant contrasts
        "p/b": [("pat", "bat"), ("pin", "bin"), ("pet", "bet"), ("pig", "big"),
                ("pack", "back"), ("pear", "bear"), ("pull", "bull"), ("pie", "buy")],
        "t/d": [("ten", "den"), ("tie", "die"), ("tip", "dip"), ("tear", "dear"),
                ("time", "dime"), ("town", "down"), ("try", "dry"), ("train", "drain")],
        "f/v": [("fan", "van"), ("fine", "vine"), ("fast", "vast"), ("few", "view"),
                ("ferry", "very"), ("leaf", "leave"), ("half", "halve"), ("safe", "save")],
        "\u03b8/\u00f0": [("think", "this"), ("thought", "though"), ("three", "there"),
                 ("thin", "then"), ("thigh", "thy"), ("teeth", "teethe"), ("breath", "breathe")],
        "\u03b8/s": [("think", "sink"), ("thick", "sick"), ("thumb", "sum"), ("path", "pass"),
                ("thought", "sought"), ("thing", "sing"), ("thaw", "saw")],
        "s/z": [("sip", "zip"), ("sue", "zoo"), ("bus", "buzz"), ("ice", "eyes"),
                ("race", "raise"), ("lace", "laze"), ("price", "prize"), ("peace", "peas")],
        "\u0283/t\u0283": [("ship", "chip"), ("share", "chair"), ("shoe", "chew"),
                  ("wash", "watch"), ("mash", "match"), ("wish", "witch"), ("cash", "catch")],
        "\u0279/l": [("right", "light"), ("rain", "lane"), ("red", "led"), ("rock", "lock"),
                ("run", "lun"), ("road", "load"), ("rip", "lip"), ("rest", "lest")],
        "w/v": [("west", "vest"), ("wine", "vine"), ("wet", "vet"), ("wail", "veil"),
                ("while", "vile"), ("worse", "verse"), ("wary", "vary")],
        "n/\u014b": [("sin", "sing"), ("thin", "thing"), ("ban", "bang"), ("ran", "rang"),
                ("win", "wing"), ("kin", "king"), ("ton", "tongue"), ("sun", "sung")],
    }

    TONGUE_TWISTERS: list[dict[str, str | list[str]]] = [
        {"text": "She sells seashells by the seashore.", "phonemes": ["s", "\u0283"]},
        {"text": "The thirty-three thieves thought that they thrilled the throne.", "phonemes": ["\u03b8", "\u00f0"]},
        {"text": "Red lorry, yellow lorry.", "phonemes": ["\u0279", "l"]},
        {"text": "Peter Piper picked a peck of pickled peppers.", "phonemes": ["p"]},
        {"text": "Betty Botter bought some butter.", "phonemes": ["b", "t"]},
        {"text": "How much wood would a woodchuck chuck?", "phonemes": ["w", "\u028a"]},
        {"text": "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair.", "phonemes": ["z", "f", "w"]},
        {"text": "Unique New York, you know you need unique New York.", "phonemes": ["j", "n", "u\u02d0"]},
        {"text": "The sixth sick sheik's sixth sheep's sick.", "phonemes": ["s", "\u0283", "k"]},
        {"text": "I scream, you scream, we all scream for ice cream.", "phonemes": ["s", "k", "\u0279"]},
        {"text": "Lesser leather never weathered wetter weather better.", "phonemes": ["\u00f0", "l", "w", "e"]},
        {"text": "Toy boat, toy boat, toy boat.", "phonemes": ["t", "b", "\u0254\u026a"]},
        {"text": "A proper copper coffee pot.", "phonemes": ["p", "k", "\u0252"]},
        {"text": "Flash message, flash message.", "phonemes": ["f", "l", "\u00e6", "\u0283"]},
        {"text": "Three free throws.", "phonemes": ["\u03b8", "\u0279", "f"]},
        {"text": "Thin sticks, thick bricks.", "phonemes": ["\u03b8", "s", "k"]},
        {"text": "I thought a thought but the thought I thought wasn't the thought I thought I thought.", "phonemes": ["\u03b8", "\u0254\u02d0", "t"]},
        {"text": "Whether the weather is warm, whether the weather is hot, we have to put up with the weather whether we like it or not.", "phonemes": ["w", "\u00f0", "e"]},
    ]

    def minimal_pair_drill(self, phoneme_contrast: str) -> Drill | None:
        """Get a minimal pair drill for a specific phoneme contrast."""
        pairs = self.MINIMAL_PAIRS.get(phoneme_contrast)
        if pairs is None:
            return None
        items = [f"{a} / {b}" for a, b in pairs]
        phonemes = phoneme_contrast.split("/")
        return Drill(
            drill_type=DrillType.MINIMAL_PAIR,
            target_phonemes=phonemes,
            items=items,
            instructions=f"Listen and repeat each pair, focusing on the difference between /{phonemes[0]}/ and /{phonemes[1]}/.",
            difficulty=0.5,
        )

    def tongue_twister_drill(self, target_phonemes: list[str] | None = None) -> Drill:
        """Get tongue twisters targeting specific phonemes (or all)."""
        if target_phonemes:
            target_set = set(target_phonemes)
            selected = [
                tt["text"] for tt in self.TONGUE_TWISTERS
                if target_set & set(tt["phonemes"])  # type: ignore[arg-type]
            ]
        else:
            selected = [tt["text"] for tt in self.TONGUE_TWISTERS]

        return Drill(
            drill_type=DrillType.TONGUE_TWISTER,
            target_phonemes=target_phonemes or [],
            items=selected[:10],
            instructions="Read each tongue twister slowly, then gradually speed up. Repeat 3 times each.",
            difficulty=0.7,
        )

    def drills_for_language(self, native_language: NativeLanguage) -> list[Drill]:
        """Generate a set of drills tailored for a native language's difficult sounds."""
        from accentcoach.analyzer.difficulty import DifficultyRanker

        ranker = DifficultyRanker()
        profile = ranker.get_profile(native_language)
        drills: list[Drill] = []

        # Create minimal pair drills for confusion pairs
        for expected, actual in profile.confusion_pairs:
            key1 = f"{expected}/{actual}"
            key2 = f"{actual}/{expected}"
            drill = self.minimal_pair_drill(key1) or self.minimal_pair_drill(key2)
            if drill:
                drills.append(drill)

        # Add a tongue twister drill for difficult phonemes
        twister_drill = self.tongue_twister_drill(profile.difficult_phonemes)
        if twister_drill.items:
            drills.append(twister_drill)

        return drills

    def list_contrasts(self) -> list[str]:
        """List all available minimal pair contrasts."""
        return list(self.MINIMAL_PAIRS.keys())
