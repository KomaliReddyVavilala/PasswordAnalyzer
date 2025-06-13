import argparse
from password_analyzer import analyze_password
from wordlist_generator import generate_wordlist

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer + Wordlist Generator")
    subparsers = parser.add_subparsers(dest="command")

    # Password Analyzer
    analyze_parser = subparsers.add_parser("analyze", help="Analyze password strength")
    analyze_parser.add_argument("password", help="Password to analyze")

    # Wordlist Generator
    wordlist_parser = subparsers.add_parser("generate", help="Generate custom wordlist")
    wordlist_parser.add_argument("-k", "--keywords", nargs="+", required=True, help="Keywords (e.g., name)")
    wordlist_parser.add_argument("-y", "--years", nargs="+", required=True, help="Years (e.g., 1990 2025)")
    wordlist_parser.add_argument("-o", "--output", help="Output file (default: custom_wordlist.txt)")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze_password(args.password)
    elif args.command == "generate":
        generate_wordlist(args.keywords, args.years, args.output)

if __name__ == "__main__":
    main()