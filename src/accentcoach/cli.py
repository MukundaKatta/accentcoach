"""CLI interface for AccentCoach."""

from __future__ import annotations

import click
from rich.console import Console

from accentcoach.analyzer.comparison import PronunciationComparator
from accentcoach.analyzer.difficulty import DifficultyRanker
from accentcoach.analyzer.phoneme import PhonemeAnalyzer
from accentcoach.exercises.drills import PronunciationDrill
from accentcoach.exercises.words import ProblemWordDatabase
from accentcoach.models import NativeLanguage, PhonemeCategory
from accentcoach.report import (
    print_comparison,
    print_difficulty_profile,
    print_drill,
    print_phoneme_chart,
)

console = Console()


@click.group()
@click.version_option(package_name="accentcoach")
def cli() -> None:
    """AccentCoach - AI Pronunciation Trainer."""


@cli.command()
@click.option("-c", "--category", type=click.Choice(["vowel", "consonant", "diphthong"]), default=None)
def phonemes(category: str | None) -> None:
    """Display the IPA phoneme chart."""
    analyzer = PhonemeAnalyzer()
    cat = PhonemeCategory(category) if category else None
    chart = analyzer.all_phonemes(cat)
    print_phoneme_chart(chart, console)
    console.print(f"\nTotal: {len(chart)} phonemes")


@cli.command()
@click.argument("word")
def lookup(word: str) -> None:
    """Look up pronunciation of a word."""
    analyzer = PhonemeAnalyzer()
    db = ProblemWordDatabase()

    pron = analyzer.get_pronunciation(word)
    if pron:
        console.print(f"[bold]{word}[/]: [cyan]{pron.ipa}[/]  phonemes: {pron.phonemes}")
        return

    entry = db.get(word)
    if entry:
        console.print(f"[bold]{word}[/]: [cyan]{entry.ipa}[/]  syllables: {entry.syllable_count}")
        if entry.common_errors:
            console.print(f"  Common errors: {', '.join(entry.common_errors)}")
        return

    console.print(f"[yellow]Word '{word}' not found in dictionary.[/]")


@cli.command()
@click.argument("word")
@click.argument("user_ipa")
def compare(word: str, user_ipa: str) -> None:
    """Compare your pronunciation against the reference."""
    comparator = PronunciationComparator()
    result = comparator.compare_ipa_string(word, user_ipa)
    print_comparison(result, console)


@cli.command()
@click.argument("language", type=click.Choice([l.value for l in NativeLanguage]))
def difficulty(language: str) -> None:
    """Show difficulty profile for your native language."""
    ranker = DifficultyRanker()
    profile = ranker.get_profile(NativeLanguage(language))
    print_difficulty_profile(profile, console)


@cli.command()
@click.option("-c", "--contrast", default=None, help="Phoneme contrast (e.g. 'i:/I')")
@click.option("-l", "--language", type=click.Choice([l.value for l in NativeLanguage]), default=None)
def drill(contrast: str | None, language: str | None) -> None:
    """Run a pronunciation drill."""
    drills_gen = PronunciationDrill()

    if contrast:
        d = drills_gen.minimal_pair_drill(contrast)
        if d:
            print_drill(d, console)
        else:
            console.print(f"[yellow]No minimal pairs found for '{contrast}'.[/]")
            console.print(f"Available contrasts: {', '.join(drills_gen.list_contrasts())}")
        return

    if language:
        exercises = drills_gen.drills_for_language(NativeLanguage(language))
        for d in exercises:
            print_drill(d, console)
        return

    # Default: show a tongue twister drill
    d = drills_gen.tongue_twister_drill()
    print_drill(d, console)


@cli.command()
@click.option("--prefix", default=None, help="Filter by prefix")
def words(prefix: str | None) -> None:
    """Browse the problem word database."""
    db = ProblemWordDatabase()
    if prefix:
        results = db.search(prefix)
    else:
        results = db.all_words()

    console.print(f"[bold]{len(results)} words[/]\n")
    for wp in results[:30]:
        errors = f"  (common errors: {', '.join(wp.common_errors)})" if wp.common_errors else ""
        console.print(f"  [cyan]{wp.word:<20}[/] {wp.ipa:<30} syllables={wp.syllable_count}{errors}")

    if len(results) > 30:
        console.print(f"\n  ... and {len(results) - 30} more. Use --prefix to filter.")


@cli.command()
def contrasts() -> None:
    """List available minimal pair contrasts."""
    drills = PronunciationDrill()
    for c in drills.list_contrasts():
        pairs = PronunciationDrill.MINIMAL_PAIRS[c]
        console.print(f"  [cyan]{c:<12}[/] {len(pairs)} pairs  e.g. {pairs[0][0]} / {pairs[0][1]}")


if __name__ == "__main__":
    cli()
