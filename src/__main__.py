"""CLI for accentcoach."""
import sys, json, argparse
from .core import Accentcoach

def main():
    parser = argparse.ArgumentParser(description="AccentCoach — AI Pronunciation Trainer. Accent reduction and pronunciation improvement with speech analysis.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Accentcoach()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.learn(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"accentcoach v0.1.0 — AccentCoach — AI Pronunciation Trainer. Accent reduction and pronunciation improvement with speech analysis.")

if __name__ == "__main__":
    main()
