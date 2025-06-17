## Advanced Password Security Toolkit

A multi-functional Python toolkit for password security analysis, vulnerability testing, and defensive wordlist generation.

## Features

### Password Analysis Module
- **ZXCVBN Algorithm**: Enterprise-grade password strength estimation
- **Detailed Feedback**:
  - Strength score (0-4 scale)
  - Time-to-crack estimation
  - Vulnerability warnings
  - Improvement suggestions
- **Multi-platform**: Works on Windows/macOS/Linux

### Wordlist Generator
- **Custom Patterns**:
  - Leetspeak transformations (e.g., `a` → `@`)
  - Case variations (upper/lower/title case)
  - Year combinations (prefix/suffix)
- **Output Formats**: .txt (Hashcat/John compatible)
- **Performance**: Generates 10,000+ combinations in <1s

### Prerequisites
- Install Python 3.7+
- ```bash
- pip install zxcvbn nltk argparse

