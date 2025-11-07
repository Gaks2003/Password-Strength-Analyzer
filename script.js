class PasswordAnalyzer {
    constructor() {
        this.initializeElements();
        this.bindEvents();
        this.commonPasswords = new Set([
            'password', '123456', '123456789', 'qwerty', 'abc123', 'password123',
            'admin', 'letmein', 'welcome', 'monkey', '1234567890', 'dragon'
        ]);
        this.commonPatterns = {
            keyboard: /qwerty|asdf|zxcv|1234|abcd/i,
            repeated: /(.)\1{2,}/,
            sequential: /(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)/i,
            date: /\b(19|20)\d{2}\b|\b(0?[1-9]|1[0-2])[\/\-](0?[1-9]|[12]\d|3[01])[\/\-](\d{2}|\d{4})\b/,
            leet: /[4@][5$][7!][3e][0o]/i
        };
    }

    initializeElements() {
        this.passwordInput = document.getElementById('passwordInput');
        this.togglePassword = document.getElementById('togglePassword');
        this.breachCheck = document.getElementById('breachCheck');
        this.analyzeBtn = document.getElementById('analyzeBtn');
        this.generateBtn = document.getElementById('generateBtn');
        this.passphraseBtn = document.getElementById('passphraseBtn');
        this.resultsSection = document.getElementById('resultsSection');
        this.loadingSpinner = document.getElementById('loadingSpinner');
        this.exportBtn = document.getElementById('exportBtn');
    }

    bindEvents() {
        this.togglePassword.addEventListener('click', () => this.togglePasswordVisibility());
        this.analyzeBtn.addEventListener('click', () => this.analyzePassword());
        this.generateBtn.addEventListener('click', () => this.generatePassword());
        this.passphraseBtn.addEventListener('click', () => this.generatePassphrase());
        this.exportBtn.addEventListener('click', () => this.exportResults());
        this.passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.analyzePassword();
        });
        this.passwordInput.addEventListener('input', () => this.clearResults());
    }

    togglePasswordVisibility() {
        const type = this.passwordInput.type === 'password' ? 'text' : 'password';
        this.passwordInput.type = type;
        const icon = this.togglePassword.querySelector('i');
        icon.className = type === 'password' ? 'fas fa-eye' : 'fas fa-eye-slash';
    }

    clearResults() {
        this.resultsSection.style.display = 'none';
    }

    async analyzePassword() {
        const password = this.passwordInput.value.trim();
        if (!password) {
            alert('Please enter a password to analyze');
            return;
        }

        this.showLoading(true);
        
        try {
            // Simulate analysis delay
            await new Promise(resolve => setTimeout(resolve, 1500));
            
            const analysis = this.performAnalysis(password);
            this.displayResults(analysis, password);
        } catch (error) {
            console.error('Analysis error:', error);
            alert('An error occurred during analysis');
        } finally {
            this.showLoading(false);
        }
    }

    performAnalysis(password) {
        const entropy = this.calculateEntropy(password);
        const patterns = this.detectPatterns(password);
        const strength = this.calculateStrength(password, entropy, patterns);
        const crackTimes = this.estimateCrackTimes(password, entropy);
        const recommendations = this.generateRecommendations(password, patterns, strength);
        const securityIssues = this.identifySecurityIssues(password, patterns);

        return {
            entropy,
            patterns,
            strength,
            crackTimes,
            recommendations,
            securityIssues,
            score: Math.round(strength.score * 100)
        };
    }

    calculateEntropy(password) {
        const length = password.length;
        let charset = 0;
        
        if (/[a-z]/.test(password)) charset += 26;
        if (/[A-Z]/.test(password)) charset += 26;
        if (/[0-9]/.test(password)) charset += 10;
        if (/[^a-zA-Z0-9]/.test(password)) charset += 32;

        const shannonEntropy = this.calculateShannonEntropy(password);
        const nistEntropy = Math.log2(Math.pow(charset, length));
        
        return {
            shannon: shannonEntropy,
            nist: nistEntropy,
            charset,
            uniqueness: this.calculateUniqueness(password)
        };
    }

    calculateShannonEntropy(password) {
        const freq = {};
        for (let char of password) {
            freq[char] = (freq[char] || 0) + 1;
        }
        
        let entropy = 0;
        const length = password.length;
        
        for (let count of Object.values(freq)) {
            const p = count / length;
            entropy -= p * Math.log2(p);
        }
        
        return entropy * length;
    }

    calculateUniqueness(password) {
        const unique = new Set(password).size;
        return (unique / password.length) * 100;
    }

    detectPatterns(password) {
        const patterns = {
            keyboard: this.commonPatterns.keyboard.test(password),
            repeated: this.commonPatterns.repeated.test(password),
            sequential: this.commonPatterns.sequential.test(password),
            date: this.commonPatterns.date.test(password),
            leet: this.commonPatterns.leet.test(password),
            dictionary: this.commonPasswords.has(password.toLowerCase()),
            personal: this.detectPersonalInfo(password)
        };

        patterns.count = Object.values(patterns).filter(Boolean).length;
        return patterns;
    }

    detectPersonalInfo(password) {
        // Simple heuristics for personal info
        const personalPatterns = [
            /\b(john|jane|mike|sarah|david|mary|james|lisa)\b/i,
            /\b(admin|user|test|demo)\b/i,
            /\b\d{4}\b/ // Years
        ];
        
        return personalPatterns.some(pattern => pattern.test(password));
    }

    calculateStrength(password, entropy, patterns) {
        let score = 0;
        
        // Length contribution (25%)
        score += Math.min(password.length / 20, 1) * 0.25;
        
        // Entropy contribution (30%)
        score += Math.min(entropy.shannon / 50, 1) * 0.30;
        
        // Character diversity (15%)
        const diversity = entropy.charset / 94; // Max possible charset
        score += diversity * 0.15;
        
        // Uniqueness (10%)
        score += (entropy.uniqueness / 100) * 0.10;
        
        // NIST entropy (10%)
        score += Math.min(entropy.nist / 60, 1) * 0.10;
        
        // Base score (10%)
        score += 0.10;
        
        // Pattern penalties
        const patternPenalty = patterns.count * 0.08;
        score = Math.max(0, score - patternPenalty);
        
        // Common password penalty
        if (patterns.dictionary) {
            score *= 0.3;
        }
        
        const level = this.getStrengthLevel(score);
        
        return { score, level, color: this.getStrengthColor(level) };
    }

    getStrengthLevel(score) {
        if (score >= 0.8) return 'Very Strong';
        if (score >= 0.6) return 'Strong';
        if (score >= 0.4) return 'Moderate';
        if (score >= 0.2) return 'Weak';
        return 'Very Weak';
    }

    getStrengthColor(level) {
        const colors = {
            'Very Strong': '#2ed573',
            'Strong': '#5352ed',
            'Moderate': '#f1c40f',
            'Weak': '#ffa502',
            'Very Weak': '#ff4757'
        };
        return colors[level];
    }

    estimateCrackTimes(password, entropy) {
        const guesses = Math.pow(2, entropy.shannon / 2);
        
        return {
            online: this.formatTime(guesses / 1000), // 1000 guesses/sec
            offline_cpu: this.formatTime(guesses / 1000000), // 1M guesses/sec
            offline_gpu: this.formatTime(guesses / 1000000000) // 1B guesses/sec
        };
    }

    formatTime(seconds) {
        if (seconds < 1) return 'Instant';
        if (seconds < 60) return `${Math.round(seconds)} seconds`;
        if (seconds < 3600) return `${Math.round(seconds / 60)} minutes`;
        if (seconds < 86400) return `${Math.round(seconds / 3600)} hours`;
        if (seconds < 31536000) return `${Math.round(seconds / 86400)} days`;
        return `${Math.round(seconds / 31536000)} years`;
    }

    generateRecommendations(password, patterns, strength) {
        const recommendations = [];
        
        if (password.length < 12) {
            recommendations.push('Increase password length to at least 12 characters');
        }
        
        if (!/[a-z]/.test(password)) {
            recommendations.push('Add lowercase letters');
        }
        
        if (!/[A-Z]/.test(password)) {
            recommendations.push('Add uppercase letters');
        }
        
        if (!/[0-9]/.test(password)) {
            recommendations.push('Add numbers');
        }
        
        if (!/[^a-zA-Z0-9]/.test(password)) {
            recommendations.push('Add special characters (!@#$%^&*)');
        }
        
        if (patterns.repeated) {
            recommendations.push('Avoid repeated characters');
        }
        
        if (patterns.sequential) {
            recommendations.push('Avoid sequential patterns');
        }
        
        if (patterns.keyboard) {
            recommendations.push('Avoid keyboard patterns');
        }
        
        if (patterns.dictionary) {
            recommendations.push('Avoid common dictionary words');
        }
        
        if (patterns.date) {
            recommendations.push('Avoid dates and years');
        }
        
        if (recommendations.length === 0) {
            recommendations.push('Excellent password! Consider using a password manager');
        }
        
        return recommendations;
    }

    identifySecurityIssues(password, patterns) {
        const issues = [];
        
        if (patterns.dictionary) {
            issues.push({
                severity: 'high',
                message: 'Password found in common password lists'
            });
        }
        
        if (password.length < 8) {
            issues.push({
                severity: 'high',
                message: 'Password is too short (less than 8 characters)'
            });
        }
        
        if (patterns.repeated) {
            issues.push({
                severity: 'medium',
                message: 'Contains repeated character sequences'
            });
        }
        
        if (patterns.keyboard) {
            issues.push({
                severity: 'medium',
                message: 'Contains keyboard patterns'
            });
        }
        
        if (patterns.personal) {
            issues.push({
                severity: 'medium',
                message: 'May contain personal information'
            });
        }
        
        if (!/[^a-zA-Z0-9]/.test(password)) {
            issues.push({
                severity: 'low',
                message: 'No special characters used'
            });
        }
        
        return issues;
    }

    displayResults(analysis, password) {
        // Update score display
        document.getElementById('scoreValue').textContent = analysis.score;
        document.getElementById('strengthText').textContent = analysis.strength.level;
        document.getElementById('strengthText').style.color = analysis.strength.color;
        
        // Update strength bar
        const strengthBar = document.getElementById('strengthBar');
        strengthBar.style.setProperty('--width', `${analysis.score}%`);
        strengthBar.style.background = `linear-gradient(90deg, ${analysis.strength.color} ${analysis.score}%, #e9ecef ${analysis.score}%)`;
        
        // Show/hide detailed analysis based on breach check setting
        const detailedAnalysis = document.getElementById('detailedAnalysis');
        if (this.breachCheck.checked) {
            // Update detailed analysis
            this.updateEntropyDetails(analysis.entropy, password);
            this.updatePatternDetails(analysis.patterns);
            this.updateCrackTimeDetails(analysis.crackTimes);
            this.updateSecurityIssues(analysis.securityIssues);
            this.updateRecommendations(analysis.recommendations);
            detailedAnalysis.style.display = 'block';
        } else {
            detailedAnalysis.style.display = 'none';
        }
        
        // Store results for export
        this.lastAnalysis = { analysis, password: '***hidden***' };
        
        // Show results
        this.resultsSection.style.display = 'block';
        this.resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    updateEntropyDetails(entropy, password) {
        const container = document.getElementById('entropyDetails');
        container.innerHTML = `
            <div class="metric-item">
                <span class="metric-label">Shannon Entropy:</span>
                <span class="metric-value">${entropy.shannon.toFixed(2)} bits</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">NIST Entropy:</span>
                <span class="metric-value">${entropy.nist.toFixed(2)} bits</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Character Set Size:</span>
                <span class="metric-value">${entropy.charset}</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Uniqueness:</span>
                <span class="metric-value">${entropy.uniqueness.toFixed(1)}%</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Length:</span>
                <span class="metric-value">${password.length} characters</span>
            </div>
        `;
    }

    updatePatternDetails(patterns) {
        const container = document.getElementById('patternDetails');
        const patternList = [
            { key: 'keyboard', label: 'Keyboard Patterns', icon: '⌨️' },
            { key: 'repeated', label: 'Repeated Characters', icon: '🔄' },
            { key: 'sequential', label: 'Sequential Patterns', icon: '📈' },
            { key: 'dictionary', label: 'Dictionary Words', icon: '📖' },
            { key: 'date', label: 'Date Patterns', icon: '📅' },
            { key: 'leet', label: 'Leet Speak', icon: '🔤' },
            { key: 'personal', label: 'Personal Info', icon: '👤' }
        ];

        const html = patternList.map(pattern => `
            <div class="pattern-item">
                <span class="pattern-icon">${pattern.icon}</span>
                <span>${pattern.label}</span>
                <span style="margin-left: auto; color: ${patterns[pattern.key] ? '#ff4757' : '#2ed573'}">
                    ${patterns[pattern.key] ? '❌ Detected' : '✅ Clean'}
                </span>
            </div>
        `).join('');

        container.innerHTML = html;
    }

    updateCrackTimeDetails(crackTimes) {
        const container = document.getElementById('crackTimeDetails');
        container.innerHTML = `
            <div class="metric-item">
                <span class="metric-label">Online Attack:</span>
                <span class="metric-value">${crackTimes.online}</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Offline CPU:</span>
                <span class="metric-value">${crackTimes.offline_cpu}</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Offline GPU Cluster:</span>
                <span class="metric-value">${crackTimes.offline_gpu}</span>
            </div>
        `;
    }

    updateSecurityIssues(issues) {
        const container = document.getElementById('securityIssues');
        
        if (issues.length === 0) {
            container.innerHTML = '<div style="color: #2ed573; text-align: center; padding: 20px;">✅ No security issues detected!</div>';
            return;
        }

        const html = issues.map(issue => `
            <div class="issue-item">
                <span class="issue-severity severity-${issue.severity}">${issue.severity}</span>
                <span>${issue.message}</span>
            </div>
        `).join('');

        container.innerHTML = html;
    }

    updateRecommendations(recommendations) {
        const container = document.getElementById('recommendationsList');
        const html = recommendations.map(rec => `<li>${rec}</li>`).join('');
        container.innerHTML = html;
    }

    generatePassword() {
        const length = prompt('Password length (8-128):', '16');
        const len = Math.max(8, Math.min(128, parseInt(length) || 16));
        
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?';
        let password = '';
        
        for (let i = 0; i < len; i++) {
            password += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        
        this.passwordInput.value = password;
        this.passwordInput.type = 'text';
        this.togglePassword.querySelector('i').className = 'fas fa-eye-slash';
        
        // Auto-analyze
        setTimeout(() => this.analyzePassword(), 500);
    }

    generatePassphrase() {
        const words = ['correct', 'horse', 'battery', 'staple', 'mountain', 'river', 'ocean', 'forest',
                      'sunrise', 'moonlight', 'thunder', 'whisper', 'journey', 'adventure', 'mystery',
                      'dragon', 'phoenix', 'crystal', 'shadow', 'lightning', 'cascade', 'meadow'];
        
        const wordCount = parseInt(prompt('Number of words (3-8):', '5')) || 5;
        const count = Math.max(3, Math.min(8, wordCount));
        
        const selectedWords = [];
        for (let i = 0; i < count; i++) {
            const word = words[Math.floor(Math.random() * words.length)];
            selectedWords.push(word.charAt(0).toUpperCase() + word.slice(1));
        }
        
        const passphrase = selectedWords.join('-') + Math.floor(Math.random() * 100);
        
        this.passwordInput.value = passphrase;
        this.passwordInput.type = 'text';
        this.togglePassword.querySelector('i').className = 'fas fa-eye-slash';
        
        // Auto-analyze
        setTimeout(() => this.analyzePassword(), 500);
    }

    exportResults() {
        if (!this.lastAnalysis) {
            alert('No analysis results to export');
            return;
        }

        const data = {
            timestamp: new Date().toISOString(),
            analysis: this.lastAnalysis.analysis,
            password: this.lastAnalysis.password
        };

        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `password-analysis-${Date.now()}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    showLoading(show) {
        this.loadingSpinner.style.display = show ? 'flex' : 'none';
    }
}

// Matrix background animation
function initMatrix() {
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
    const charArray = chars.split('');
    const fontSize = 14;
    const columns = canvas.width / fontSize;
    const drops = [];
    
    for (let i = 0; i < columns; i++) {
        drops[i] = 1;
    }
    
    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.fillStyle = '#00ff00';
        ctx.font = fontSize + 'px Courier New';
        
        for (let i = 0; i < drops.length; i++) {
            const text = charArray[Math.floor(Math.random() * charArray.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }
    
    setInterval(draw, 35);
    
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    initMatrix();
    new PasswordAnalyzer();
});