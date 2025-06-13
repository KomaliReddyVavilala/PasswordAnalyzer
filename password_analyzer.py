import zxcvbn

def analyze_password(password):
    result = zxcvbn.zxcvbn(password)
    print("\n--- Password Analysis ---")
    print(f"Password: {password}")
    print(f"Strength Score (0-4): {result['score']}")
    print(f"Guesses Needed: {result['guesses']}")
    print(f"Warning: {result['feedback']['warning'] or 'None'}")
    print(f"Suggestions: {result['feedback']['suggestions'] or 'None'}")

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    analyze_password(password)
