# ML-Based Password Strength Analyzer

An advanced password security assessment tool that leverages machine learning algorithms to evaluate password vulnerability based on real-world breach patterns and entropy metrics.

## Features

### 🧠 Machine Learning Algorithms
- **Shannon Entropy Calculation**: Measures password randomness and unpredictability
- **Pattern Recognition**: Detects keyboard sequences, dictionary words, and common substitutions
- **Breach Pattern Analysis**: Assesses vulnerability based on real-world attack data
- **ML-Inspired Scoring**: Weighted algorithms that mimic machine learning approaches

### 🔍 Advanced Analysis
- **Comprehensive Pattern Detection**: 
  - Keyboard walking patterns (qwerty, 123456, etc.)
  - Repeated character sequences
  - Dictionary word detection
  - Sequential character patterns
  - Date and personal information patterns
  - Common l33t speak substitutions

- **Entropy Metrics**:
  - Shannon entropy calculation
  - Character set diversity analysis
  - Keyspace estimation
  - Uniqueness scoring
  - Compression ratio analysis

- **Breach Risk Assessment**:
  - Common password database checking
  - Personal information detection
  - Vulnerability factor identification
  - Risk scoring with weighted factors

### 📊 Detailed Reporting
- **Strength Levels**: Exceptional, Very Strong, Strong, Moderate, Weak, Very Weak, Extremely Weak
- **Time-to-Crack Estimates**: Online, offline, and GPU cluster attack scenarios
- **AI-Powered Recommendations**: Personalized suggestions for improvement
- **Comprehensive Scoring Breakdown**: Detailed analysis of all contributing factors

## Installation

1. Clone or download the password analyzer:
```bash
# No installation required - uses Python standard library only
python3 password_analyzer.py
```

2. Optional: Install enhanced dependencies for future features:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode
```bash
python3 password_analyzer.py
```

### Programmatic Usage
```python
from password_analyzer import PasswordAnalyzer

analyzer = PasswordAnalyzer()
result = analyzer.analyze_password("your_password_here")

print(f"Strength: {result.level}")
print(f"Score: {result.score:.3f}")
print(f"Entropy: {result.entropy.shannon_entropy:.3f} bits")
```

## Algorithm Details

### ML-Inspired Scoring System
The analyzer uses a sophisticated scoring algorithm that combines multiple factors:

1. **Entropy Contribution (35%)**: Based on Shannon entropy calculation
2. **Length Contribution (25%)**: Password length with diminishing returns
3. **Diversity Contribution (20%)**: Character set variety (lowercase, uppercase, digits, symbols)
4. **Uniqueness Contribution (10%)**: Entropy × length for uniqueness scoring
5. **Pattern Penalties (10%)**: Deductions for detected vulnerability patterns
6. **Breach Risk Penalty**: Major deductions based on breach database analysis

### Pattern Recognition Algorithms
- **Keyboard Pattern Detection**: Identifies common typing patterns
- **Sequential Analysis**: Detects ascending/descending character sequences
- **Dictionary Matching**: Checks against common word databases
- **Substitution Recognition**: Identifies l33t speak and common character replacements
- **Personal Information Detection**: Flags names, dates, and personal data patterns

### Entropy Analysis
- **Shannon Entropy**: Measures information content and randomness
- **Character Set Analysis**: Evaluates the diversity of character types used
- **Keyspace Calculation**: Estimates the total possible password combinations
- **Compression Ratio**: Assesses predictability through compression algorithms

## Security Features

### Breach Database Analysis
- Checks against common password databases from real breaches
- Identifies passwords that have appeared in security incidents
- Assesses vulnerability to dictionary and brute-force attacks

### Time-to-Crack Estimation
- **Online Attacks**: Assumes 1,000 guesses/second (rate-limited)
- **Offline Attacks**: Assumes 1 billion guesses/second (hash cracking)
- **GPU Cluster Attacks**: Assumes 1 trillion guesses/second (advanced hardware)

### Privacy Protection
- All analysis is performed locally
- No passwords are transmitted or stored
- No network connections required

## Example Analysis

```
🔐 ML-BASED PASSWORD STRENGTH ANALYSIS REPORT
================================================================================

📊 OVERALL STRENGTH: Strong
📈 ML Score: 0.742/1.000 [██████████████░░░░░░] 74.2%

🧮 ENTROPY ANALYSIS
----------------------------------------
Shannon Entropy:     3.459 bits
Character Set Size:  94
Keyspace:           2.51e+19
Uniqueness Score:   41.51
Compression Ratio:  0.923

🔍 PATTERN ANALYSIS
----------------------------------------
Keyboard Patterns      ✅ NONE (0)
Repeated Characters    ✅ NONE (0)
Dictionary Words       ❌ DETECTED (1)
Common Substitutions   ✅ NONE (0)
Sequential Characters  ✅ NONE (0)
Date Patterns         ✅ NONE (0)
Personal Info Patterns ✅ NONE (0)

⚠️  BREACH RISK ASSESSMENT
----------------------------------------
Overall Risk Score:  0.150/1.000 (15.0%)
Common Password      ✅ LOW RISK
Personal Information ✅ LOW RISK
Keyboard Walking     ✅ LOW RISK
Dictionary Based     ❌ HIGH RISK

🤖 AI RECOMMENDATIONS
----------------------------------------
 1. 📚 Avoid common dictionary words - use passphrases instead
 2. 🔢 Increase length to at least 12-16 characters for better security
```

## Technical Implementation

### Core Components
- **PasswordAnalyzer**: Main analysis engine with ML algorithms
- **Pattern Detection**: Advanced regex and algorithmic pattern recognition
- **Entropy Calculation**: Mathematical entropy and complexity analysis
- **Risk Assessment**: Breach database and vulnerability analysis
- **Reporting System**: Comprehensive analysis formatting and display

### Data Structures
- **PatternAnalysis**: Structured pattern detection results
- **BreachRisk**: Security vulnerability assessment
- **EntropyMetrics**: Mathematical complexity measurements
- **MLStrengthResult**: Complete analysis results

## Contributing

This project uses advanced algorithms for password security analysis. Contributions are welcome for:
- Enhanced pattern recognition algorithms
- Additional breach database integration
- Machine learning model improvements
- Visualization and reporting features

## License

This project is designed for educational and security assessment purposes. Use responsibly and in accordance with applicable security policies.

## Disclaimer

This tool is for educational and security assessment purposes only. Always follow your organization's password policies and security guidelines. The analysis provided is based on current security research and may not reflect all possible attack vectors.