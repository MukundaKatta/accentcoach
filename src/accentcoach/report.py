"""Rich console reporting for AccentCoach."""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from accentcoach.models import (
    DifficultyProfile,
    Drill,
    DrillType,
    Phoneme,
    PracticeSession,
    PronunciationComparison,
)


def print_phoneme_chart(phonemes: list[Phoneme], console: Console | None = None) -> None:
    """Print the IPA phoneme chart."""
    console = console or Console()

    table = Table(title="English IPA Phoneme Chart (44 phonemes)")
    table.add_column("IPA", style="bold cyan", width=6)
    table.add_column("Category")
    table.add_column("Example")
    table.add_column("Description")
    table.add_column("Voiced", width=7)

    for p in phonemes:
        table.add_row(
            p.ipa, p.category.value, p.example_word,
            p.description, "Yes" if p.voice else "No",
        )
    console.print(table)


def print_comparison(comp: PronunciationComparison, console: Console | None = None) -> None:
    """Print a pronunciation comparison result."""
    console = console or Console()

    color = "green" if comp.accuracy >= 0.8 else "yellow" if comp.accuracy >= 0.5 else "red"
    console.print(Panel(
        f"Word: [bold]{comp.word}[/]\n"
        f"Reference: [cyan]{comp.reference_ipa}[/]\n"
        f"Your input: [yellow]{comp.user_ipa}[/]\n"
        f"Accuracy: [{color}]{comp.accuracy:.0%}[/{color}]\n"
        f"Matching: {', '.join(comp.matching_phonemes) or 'none'}\n"
        f"Mismatched: {', '.join(f'{e}->{a}' for e, a in comp.mismatched_phonemes) or 'none'}",
        title="Pronunciation Comparison",
    ))
    for fb in comp.feedback:
        console.print(f"  [dim]{fb}[/]")


def print_drill(drill: Drill, console: Console | None = None) -> None:
    """Print a pronunciation drill."""
    console = console or Console()

    title = f"{drill.drill_type.value.replace('_', ' ').title()} Drill"
    if drill.target_phonemes:
        title += f" (/{'/'.join(drill.target_phonemes)}/)"

    console.print(f"\n[bold]{title}[/]")
    console.print(f"[dim]{drill.instructions}[/]\n")

    for i, item in enumerate(drill.items, 1):
        console.print(f"  {i:2d}. {item}")


def print_difficulty_profile(profile: DifficultyProfile, console: Console | None = None) -> None:
    """Print a difficulty profile for a native language."""
    console = console or Console()

    console.print(Panel(
        f"[bold]Difficult phonemes:[/] {', '.join(f'/{p}/' for p in profile.difficult_phonemes)}\n\n"
        f"[bold]Confusion pairs:[/]\n"
        + "\n".join(f"  /{a}/ confused with /{b}/" for a, b in profile.confusion_pairs)
        + "\n\n[bold]Tips:[/]\n"
        + "\n".join(f"  - {t}" for t in profile.tips),
        title=f"Difficulty Profile: {profile.native_language.value.title()} speakers",
    ))


def print_session_summary(session: PracticeSession, console: Console | None = None) -> None:
    """Print a practice session summary."""
    console = console or Console()

    console.rule("[bold]Practice Session Summary[/]")
    console.print(f"Words practiced: [bold]{session.words_practiced}[/]")
    console.print(f"Drills completed: [bold]{session.drills_completed}[/]")
    console.print(f"Average accuracy: [bold]{session.average_accuracy:.0%}[/]")
    if session.problem_phonemes:
        console.print(f"Problem phonemes: [red]{', '.join(f'/{p}/' for p in session.problem_phonemes)}[/]")
