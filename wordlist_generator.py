import argparse
import itertools

def generate_wordlist(keywords, years, output_file="custom_wordlist.txt"):
    variations = []
    for word in keywords:
        # Basic variations (lowercase, uppercase, leetspeak)
        leet = word.replace('e', '3').replace('a', '@').replace('o', '0')
        variations.extend([word, word.lower(), word.upper(), leet])
    
    # Combine with years
    wordlist = []
    for word in variations:
        for year in years:
            wordlist.append(f"{word}{year}")
            wordlist.append(f"{year}{word}")
    
    # Save to file
    with open(output_file, 'w') as f:
        f.write('\n'.join(wordlist))
    
    print(f"[+] Generated {len(wordlist)} words in {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Wordlist Generator")
    parser.add_argument("-k", "--keywords", nargs="+", help="Keywords (e.g., name, pet)")
    parser.add_argument("-y", "--years", nargs="+", help="Years (e.g., 1990 2025)")
    parser.add_argument("-o", "--output", help="Output file (default: custom_wordlist.txt)")
    args = parser.parse_args()

    generate_wordlist(args.keywords, args.years, args.output or "custom_wordlist.txt")