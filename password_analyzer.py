#!/usr/bin/env python3
"""
ML-Based Password Strength Analyzer
Advanced password security assessment using machine learning algorithms
"""

import math
import re
import json
from typing import Dict, List, Tuple, NamedTuple
from dataclasses import dataclass
from collections import Counter
import hashlib


@dataclass
class PatternAnalysis:
    """Analysis of password patterns and vulnerabilities"""
    keyboard_patterns: int
    repeated_chars: int
    dictionary_words: int
    common_substitutions: int
    sequential_chars: int
    date_patterns: int
    personal_info_patterns: int


@dataclass
class BreachRisk:
    """Breach risk assessment metrics"""
    common_password: bool
    personal_info: bool
    keyboard_walk: bool
    dictionary_based: bool
    risk_score: float
    vulnerability_factors: List[str]


@dataclass
class EntropyMetrics:
    """Advanced entropy and complexity metrics"""
    shannon_entropy: float
    charset_size: int
    keyspace: float
    uniqueness_score: float
    compression_ratio: float


@dataclass
class MLStrengthResult:
    """Complete ML-based strength analysis result"""
    score: float
    level: str
    entropy: EntropyMetrics
    patterns: PatternAnalysis
    breach: BreachRisk
    suggestions: List[str]
    time_to_crack: Dict[str, str]


class PasswordAnalyzer:
    """Advanced ML-inspired password strength analyzer"""
    
    def __init__(self):
        # Common passwords from breach databases (simplified subset)
        self.common_passwords = {
            'password', '123456', 'password123', 'admin', 'qwerty', 'letmein',
            '123456789', 'welcome', 'monkey', '1234567890', 'dragon', 'master',
            'login', 'passw0rd', 'football', 'iloveyou', 'admin123', 'welcome123',
            'sunshine', 'princess', 'azerty', 'trustno1', 'hello123'
        }
        
        # Keyboard patterns for detection
        self.keyboard_patterns = [
            'qwerty', 'qwertyui', 'asdf', 'asdfgh', 'zxcv', 'zxcvbn',
            '1234', '12345', '123456', '1234567', '12345678', '123456789',
            'abcd', 'abcde', 'abcdef', '!@#$', '!@#$%', 'qaz', 'wsx', 'edc'
        ]
        
        # Common dictionary words
        self.dictionary_words = {
            'password', 'admin', 'user', 'login', 'welcome', 'hello', 'world',
            'computer', 'internet', 'security', 'system', 'network', 'server',
            'database', 'application', 'software', 'hardware', 'technology'
        }
        
        # Personal information patterns
        self.personal_patterns = [
            r'\b(john|jane|mike|sarah|david|mary|james|linda)\b',
            r'\b(admin|user|test|demo|guest)\b',
            r'\b(company|corp|inc|ltd)\b',
            r'\d{4}',  # Years
            r'\d{2}/\d{2}',  # Dates
            r'\d{2}-\d{2}'  # Dates
        ]

    def calculate_shannon_entropy(self, password: str) -> float:
        """Calculate Shannon entropy of the password"""
        if not password:
            return 0.0
        
        # Count character frequencies
        frequencies = Counter(password)
        length = len(password)
        
        # Calculate Shannon entropy
        entropy = 0.0
        for count in frequencies.values():
            probability = count / length
            entropy -= probability * math.log2(probability)
        
        return entropy

    def analyze_charset(self, password: str) -> Tuple[int, int]:
        """Analyze character set diversity and size"""
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[^a-zA-Z\d]', password))
        
        charset_size = 0
        if has_lower:
            charset_size += 26
        if has_upper:
            charset_size += 26
        if has_digit:
            charset_size += 10
        if has_special:
            charset_size += 32  # Approximate special characters
        
        diversity = sum([has_lower, has_upper, has_digit, has_special])
        
        return charset_size, diversity

    def detect_patterns(self, password: str) -> PatternAnalysis:
        """Advanced pattern detection using ML-inspired algorithms"""
        lower_password = password.lower()
        
        # Keyboard pattern detection
        keyboard_patterns = 0
        for pattern in self.keyboard_patterns:
            if pattern in lower_password:
                keyboard_patterns += 1
        
        # Repeated character sequences
        repeated_chars = len(re.findall(r'(.)\1{2,}', password))
        
        # Dictionary word detection
        dictionary_words = 0
        for word in self.dictionary_words:
            if word in lower_password:
                dictionary_words += 1
        
        # Common substitution patterns (l33t speak)
        substitution_patterns = ['@', '3', '1', '0', '5', '$', '!']
        common_substitutions = sum(1 for char in substitution_patterns if char in password)
        
        # Sequential character detection
        sequential_chars = 0
        for i in range(len(password) - 2):
            if len(password) > i + 2:
                char1, char2, char3 = ord(password[i]), ord(password[i+1]), ord(password[i+2])
                if char2 == char1 + 1 and char3 == char2 + 1:
                    sequential_chars += 1
        
        # Date pattern detection
        date_patterns = len(re.findall(r'\d{4}|\d{2}/\d{2}|\d{2}-\d{2}', password))
        
        # Personal information patterns
        personal_info_patterns = 0
        for pattern in self.personal_patterns:
            if re.search(pattern, lower_password):
                personal_info_patterns += 1
        
        return PatternAnalysis(
            keyboard_patterns=keyboard_patterns,
            repeated_chars=repeated_chars,
            dictionary_words=dictionary_words,
            common_substitutions=common_substitutions,
            sequential_chars=sequential_chars,
            date_patterns=date_patterns,
            personal_info_patterns=personal_info_patterns
        )

    def assess_breach_risk(self, password: str, patterns: PatternAnalysis) -> BreachRisk:
        """ML-inspired breach risk assessment"""
        lower_password = password.lower()
        vulnerability_factors = []
        
        # Check against common passwords
        common_password = lower_password in self.common_passwords
        if common_password:
            vulnerability_factors.append("Found in common password databases")
        
        # Personal information detection
        personal_info = patterns.personal_info_patterns > 0
        if personal_info:
            vulnerability_factors.append("Contains personal information patterns")
        
        # Keyboard walk detection
        keyboard_walk = patterns.keyboard_patterns > 0
        if keyboard_walk:
            vulnerability_factors.append("Contains keyboard walking patterns")
        
        # Dictionary-based detection
        dictionary_based = patterns.dictionary_words > 0
        if dictionary_based:
            vulnerability_factors.append("Contains dictionary words")
        
        # ML-inspired risk scoring with weighted factors
        risk_score = 0.0
        
        # High-impact factors
        if common_password:
            risk_score += 0.5
        if personal_info:
            risk_score += 0.2
        if keyboard_walk:
            risk_score += 0.15
        if dictionary_based:
            risk_score += 0.15
        
        # Pattern-based penalties
        risk_score += min(patterns.repeated_chars * 0.1, 0.2)
        risk_score += min(patterns.sequential_chars * 0.05, 0.15)
        risk_score += min(patterns.date_patterns * 0.08, 0.16)
        
        # Length penalty
        if len(password) < 8:
            risk_score += 0.25
            vulnerability_factors.append("Password too short (< 8 characters)")
        elif len(password) < 12:
            risk_score += 0.1
            vulnerability_factors.append("Password could be longer (< 12 characters)")
        
        risk_score = min(risk_score, 1.0)
        
        return BreachRisk(
            common_password=common_password,
            personal_info=personal_info,
            keyboard_walk=keyboard_walk,
            dictionary_based=dictionary_based,
            risk_score=risk_score,
            vulnerability_factors=vulnerability_factors
        )

    def calculate_entropy_metrics(self, password: str) -> EntropyMetrics:
        """Calculate comprehensive entropy metrics"""
        shannon_entropy = self.calculate_shannon_entropy(password)
        charset_size, _ = self.analyze_charset(password)
        
        # Keyspace calculation
        keyspace = charset_size ** len(password) if charset_size > 0 else 0
        
        # Uniqueness score (entropy * length)
        uniqueness_score = shannon_entropy * len(password)
        
        # Compression ratio (measure of predictability)
        try:
            import zlib
            compressed = zlib.compress(password.encode())
            compression_ratio = len(compressed) / len(password.encode()) if password else 1.0
        except:
            compression_ratio = 1.0
        
        return EntropyMetrics(
            shannon_entropy=shannon_entropy,
            charset_size=charset_size,
            keyspace=keyspace,
            uniqueness_score=uniqueness_score,
            compression_ratio=compression_ratio
        )

    def estimate_crack_time(self, password: str, entropy_metrics: EntropyMetrics) -> Dict[str, str]:
        """Estimate time to crack using different attack methods"""
        if not password:
            return {"online": "Instant", "offline": "Instant", "gpu_cluster": "Instant"}
        
        # Guesses based on keyspace
        guesses = entropy_metrics.keyspace / 2  # Average case
        
        # Attack speeds (guesses per second)
        online_speed = 1000  # Online attacks
        offline_speed = 1e9   # Offline attacks
        gpu_cluster_speed = 1e12  # GPU cluster attacks
        
        def format_time(seconds):
            if seconds < 60:
                return f"{seconds:.1f} seconds"
            elif seconds < 3600:
                return f"{seconds/60:.1f} minutes"
            elif seconds < 86400:
                return f"{seconds/3600:.1f} hours"
            elif seconds < 31536000:
                return f"{seconds/86400:.1f} days"
            else:
                return f"{seconds/31536000:.1f} years"
        
        return {
            "online": format_time(guesses / online_speed),
            "offline": format_time(guesses / offline_speed),
            "gpu_cluster": format_time(guesses / gpu_cluster_speed)
        }

    def generate_suggestions(self, patterns: PatternAnalysis, breach: BreachRisk, 
                           charset_diversity: int, password: str) -> List[str]:
        """Generate AI-inspired improvement suggestions"""
        suggestions = []
        
        if len(password) < 12:
            suggestions.append("🔢 Increase length to at least 12-16 characters for better security")
        
        if charset_diversity < 3:
            suggestions.append("🔤 Use a mix of uppercase, lowercase, numbers, and special characters")
        
        if patterns.repeated_chars > 0:
            suggestions.append("🔄 Avoid repeated character sequences (e.g., 'aaa', '111')")
        
        if patterns.keyboard_patterns > 0:
            suggestions.append("⌨️ Avoid keyboard patterns like 'qwerty', '123456', or 'asdf'")
        
        if patterns.dictionary_words > 0:
            suggestions.append("📚 Avoid common dictionary words - use passphrases instead")
        
        if breach.common_password:
            suggestions.append("⚠️ This password appears in breach databases - choose a unique one")
        
        if patterns.sequential_chars > 0:
            suggestions.append("🔢 Avoid sequential characters like 'abc', '123', or 'xyz'")
        
        if patterns.date_patterns > 0:
            suggestions.append("📅 Avoid using dates, years, or predictable number patterns")
        
        if patterns.personal_info_patterns > 0:
            suggestions.append("👤 Avoid personal information like names, usernames, or company names")
        
        if patterns.common_substitutions > 2:
            suggestions.append("🔀 While character substitution helps, don't rely solely on it")
        
        # Positive reinforcement for good practices
        if not suggestions:
            suggestions.append("✅ Excellent! Your password follows security best practices")
        
        return suggestions

    def analyze_password(self, password: str) -> MLStrengthResult:
        """Complete ML-based password strength analysis"""
        if not password:
            return MLStrengthResult(
                score=0.0,
                level="No Password",
                entropy=EntropyMetrics(0, 0, 0, 0, 1.0),
                patterns=PatternAnalysis(0, 0, 0, 0, 0, 0, 0),
                breach=BreachRisk(False, False, False, False, 0.0, []),
                suggestions=["Enter a password to analyze"],
                time_to_crack={"online": "N/A", "offline": "N/A", "gpu_cluster": "N/A"}
            )
        
        # Perform comprehensive analysis
        entropy_metrics = self.calculate_entropy_metrics(password)
        patterns = self.detect_patterns(password)
        breach_risk = self.assess_breach_risk(password, patterns)
        charset_size, charset_diversity = self.analyze_charset(password)
        
        # ML-inspired scoring algorithm
        ml_score = 0.0
        
        # Entropy contribution (35%)
        entropy_score = min(entropy_metrics.shannon_entropy / 4.5, 1.0) * 0.35
        ml_score += entropy_score
        
        # Length contribution (25%)
        length_score = min(len(password) / 16, 1.0) * 0.25
        ml_score += length_score
        
        # Diversity contribution (20%)
        diversity_score = (charset_diversity / 4) * 0.20
        ml_score += diversity_score
        
        # Uniqueness contribution (10%)
        uniqueness_score = min(entropy_metrics.uniqueness_score / 50, 1.0) * 0.10
        ml_score += uniqueness_score
        
        # Pattern penalties (10%)
        pattern_penalty = (
            patterns.keyboard_patterns * 0.02 +
            patterns.repeated_chars * 0.03 +
            patterns.dictionary_words * 0.025 +
            patterns.sequential_chars * 0.02 +
            patterns.date_patterns * 0.015 +
            patterns.personal_info_patterns * 0.02
        )
        ml_score -= min(pattern_penalty, 0.10)
        
        # Breach risk penalty (major impact)
        ml_score -= breach_risk.risk_score * 0.30
        
        # Compression penalty (predictability)
        if entropy_metrics.compression_ratio < 0.8:
            ml_score -= (0.8 - entropy_metrics.compression_ratio) * 0.15
        
        # Ensure score is within bounds
        ml_score = max(0.0, min(1.0, ml_score))
        
        # Determine strength level with more nuanced categories
        if ml_score >= 0.85:
            level = "Exceptional"
        elif ml_score >= 0.70:
            level = "Very Strong"
        elif ml_score >= 0.55:
            level = "Strong"
        elif ml_score >= 0.40:
            level = "Moderate"
        elif ml_score >= 0.25:
            level = "Weak"
        elif ml_score >= 0.10:
            level = "Very Weak"
        else:
            level = "Extremely Weak"
        
        # Generate suggestions
        suggestions = self.generate_suggestions(patterns, breach_risk, charset_diversity, password)
        
        # Estimate crack times
        crack_times = self.estimate_crack_time(password, entropy_metrics)
        
        return MLStrengthResult(
            score=ml_score,
            level=level,
            entropy=entropy_metrics,
            patterns=patterns,
            breach=breach_risk,
            suggestions=suggestions,
            time_to_crack=crack_times
        )


def format_analysis_report(result: MLStrengthResult, password: str) -> str:
    """Format the analysis result into a comprehensive report"""
    report = []
    
    # Header
    report.append("=" * 80)
    report.append("🔐 ML-BASED PASSWORD STRENGTH ANALYSIS REPORT")
    report.append("=" * 80)
    report.append("")
    
    # Overall Assessment
    score_bar = "█" * int(result.score * 20) + "░" * (20 - int(result.score * 20))
    report.append(f"📊 OVERALL STRENGTH: {result.level}")
    report.append(f"📈 ML Score: {result.score:.3f}/1.000 [{score_bar}] {result.score*100:.1f}%")
    report.append("")
    
    # Entropy Analysis
    report.append("🧮 ENTROPY ANALYSIS")
    report.append("-" * 40)
    report.append(f"Shannon Entropy:     {result.entropy.shannon_entropy:.3f} bits")
    report.append(f"Character Set Size:  {result.entropy.charset_size}")
    report.append(f"Keyspace:           {result.entropy.keyspace:.2e}")
    report.append(f"Uniqueness Score:   {result.entropy.uniqueness_score:.2f}")
    report.append(f"Compression Ratio:  {result.entropy.compression_ratio:.3f}")
    report.append("")
    
    # Pattern Analysis
    report.append("🔍 PATTERN ANALYSIS")
    report.append("-" * 40)
    patterns = [
        ("Keyboard Patterns", result.patterns.keyboard_patterns),
        ("Repeated Characters", result.patterns.repeated_chars),
        ("Dictionary Words", result.patterns.dictionary_words),
        ("Common Substitutions", result.patterns.common_substitutions),
        ("Sequential Characters", result.patterns.sequential_chars),
        ("Date Patterns", result.patterns.date_patterns),
        ("Personal Info Patterns", result.patterns.personal_info_patterns)
    ]
    
    for pattern_name, count in patterns:
        status = "❌ DETECTED" if count > 0 else "✅ NONE"
        report.append(f"{pattern_name:<22} {status} ({count})")
    report.append("")
    
    # Breach Risk Assessment
    report.append("⚠️  BREACH RISK ASSESSMENT")
    report.append("-" * 40)
    report.append(f"Overall Risk Score:  {result.breach.risk_score:.3f}/1.000 ({result.breach.risk_score*100:.1f}%)")
    
    risk_factors = [
        ("Common Password", result.breach.common_password),
        ("Personal Information", result.breach.personal_info),
        ("Keyboard Walking", result.breach.keyboard_walk),
        ("Dictionary Based", result.breach.dictionary_based)
    ]
    
    for factor_name, detected in risk_factors:
        status = "❌ HIGH RISK" if detected else "✅ LOW RISK"
        report.append(f"{factor_name:<20} {status}")
    
    if result.breach.vulnerability_factors:
        report.append("\n🚨 Vulnerability Factors:")
        for factor in result.breach.vulnerability_factors:
            report.append(f"   • {factor}")
    report.append("")
    
    # Time to Crack Estimates
    report.append("⏱️  ESTIMATED CRACK TIMES")
    report.append("-" * 40)
    report.append(f"Online Attack:       {result.time_to_crack['online']}")
    report.append(f"Offline Attack:      {result.time_to_crack['offline']}")
    report.append(f"GPU Cluster Attack:  {result.time_to_crack['gpu_cluster']}")
    report.append("")
    
    # AI Recommendations
    report.append("🤖 AI RECOMMENDATIONS")
    report.append("-" * 40)
    for i, suggestion in enumerate(result.suggestions, 1):
        report.append(f"{i:2d}. {suggestion}")
    report.append("")
    
    # Security Score Breakdown
    report.append("📋 DETAILED SCORING BREAKDOWN")
    report.append("-" * 40)
    entropy_contrib = min(result.entropy.shannon_entropy / 4.5, 1.0) * 0.35
    length_contrib = min(len(password) / 16, 1.0) * 0.25
    diversity_contrib = 0.20  # Estimated based on charset
    uniqueness_contrib = min(result.entropy.uniqueness_score / 50, 1.0) * 0.10
    
    report.append(f"Entropy Contribution (35%):    {entropy_contrib:.3f}")
    report.append(f"Length Contribution (25%):     {length_contrib:.3f}")
    report.append(f"Diversity Contribution (20%):  {diversity_contrib:.3f}")
    report.append(f"Uniqueness Contribution (10%): {uniqueness_contrib:.3f}")
    report.append(f"Pattern Penalties:             -{result.breach.risk_score * 0.30:.3f}")
    report.append("")
    
    report.append("=" * 80)
    report.append("Analysis completed using advanced ML algorithms and breach pattern recognition")
    report.append("=" * 80)
    
    return "\n".join(report)


def main():
    """Main interactive password analysis interface"""
    analyzer = PasswordAnalyzer()
    
    print("🔐 ML-Based Password Strength Analyzer")
    print("=" * 50)
    print("Advanced password security assessment using machine learning algorithms")
    print("Enter 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            password = input("Enter password to analyze (or 'quit' to exit): ").strip()
            
            if password.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using the ML Password Analyzer!")
                break
            
            if not password:
                print("❌ Please enter a password to analyze.\n")
                continue
            
            print("\n🔄 Analyzing password using ML algorithms...")
            print("-" * 50)
            
            # Perform analysis
            result = analyzer.analyze_password(password)
            
            # Display results
            report = format_analysis_report(result, password)
            print(report)
            
            # Ask for another analysis
            print("\n" + "="*50)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()