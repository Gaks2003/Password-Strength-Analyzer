# 🔐 Enhanced Password Strength Analyzer

A sophisticated web-based password strength analyzer that uses advanced algorithms to evaluate password security and provide detailed recommendations.

![Password Analyzer Demo](https://img.shields.io/badge/demo-live-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

## ✨ Features

- **Real-time Password Analysis** - Instant feedback as you type
- **Advanced Entropy Calculation** - Shannon and NIST entropy algorithms
- **Pattern Detection** - Identifies keyboard patterns, repetitions, and common sequences
- **Security Assessment** - Comprehensive security issue identification
- **Crack Time Estimation** - Realistic time estimates for different attack scenarios
- **AI-Powered Recommendations** - Smart suggestions for password improvement
- **Password Generator** - Generate secure passwords and passphrases
- **Matrix-Style UI** - Cyberpunk-themed interface with animated background
- **Export Results** - Download analysis results as JSON
- **Mobile Responsive** - Works seamlessly on all devices

## 🚀 Live Demo

[View Live Demo](https://gaks2003.github.io/Password-Strength-Analyzer/)

## 📊 Analysis Features

### Entropy Analysis
- **Shannon Entropy**: Measures randomness and unpredictability
- **NIST Entropy**: Government standard entropy calculation
- **Character Set Analysis**: Evaluates character diversity
- **Uniqueness Score**: Percentage of unique characters

### Pattern Detection
- ✅ Keyboard patterns (qwerty, asdf, etc.)
- ✅ Repeated character sequences
- ✅ Sequential patterns (abc, 123, etc.)
- ✅ Date patterns and years
- ✅ Leet speak detection
- ✅ Dictionary word identification
- ✅ Personal information heuristics

### Security Assessment
- **Crack Time Estimates**: Online, offline CPU, and GPU cluster scenarios
- **Vulnerability Detection**: Common password lists, weak patterns
- **Strength Scoring**: 0-100 scale with detailed breakdown
- **Risk Classification**: Very Weak to Very Strong ratings

## 🛠️ Installation

### Option 1: Direct Download
1. Clone or download this repository
2. Open `index.html` in your web browser
3. Start analyzing passwords!

### Option 2: Local Server
```bash
# Clone the repository
git clone https://github.com/your-username/password-strength-analyzer.git

# Navigate to project directory
cd password-strength-analyzer

# Start a local server (Python 3)
python -m http.server 8000

# Or using Node.js
npx serve .

# Open http://localhost:8000 in your browser
```

### Option 3: GitHub Pages
1. Fork this repository
2. Go to Settings > Pages
3. Select source branch (main/master)
4. Your analyzer will be available at `https://your-username.github.io/password-strength-analyzer`

## 📱 Usage

1. **Enter Password**: Type or paste your password in the input field
2. **Toggle Visibility**: Click the eye icon to show/hide password
3. **Enable Detailed Analysis**: Check the box for comprehensive analysis
4. **Analyze**: Click "Analyze Password" or press Enter
5. **Review Results**: View strength score, patterns, and recommendations
6. **Generate Secure Password**: Use built-in generators for strong passwords
7. **Export Results**: Download analysis data for record-keeping

## 🔧 Technical Details

### Algorithms Used
- **Shannon Entropy**: `H(X) = -Σ p(x) log₂ p(x)`
- **NIST Entropy**: Based on character set size and length
- **Pattern Matching**: Regular expressions and heuristic analysis
- **Strength Calculation**: Multi-factor weighted scoring system

### Security Features
- **No Data Transmission**: All analysis happens locally in your browser
- **Privacy First**: Passwords never leave your device
- **No Storage**: No passwords are saved or logged
- **Client-Side Only**: Pure JavaScript implementation

### Browser Compatibility
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+
- ✅ Mobile browsers

## 🎨 Customization

### Themes
The analyzer uses a Matrix-inspired cyberpunk theme. You can customize colors in `styles.css`:

```css
:root {
  --primary-color: #00ff00;
  --background-color: #0f0f0f;
  --accent-color: #00ff41;
}
```

### Adding Custom Patterns
Extend pattern detection in `script.js`:

```javascript
this.commonPatterns = {
  // Add your custom patterns here
  customPattern: /your-regex-here/i,
  // ...existing patterns
};
```

## 📈 Performance

- **Lightweight**: ~50KB total size
- **Fast Analysis**: <100ms for most passwords
- **Memory Efficient**: Minimal RAM usage
- **No Dependencies**: Pure vanilla JavaScript

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -am 'Add feature'`
6. Push: `git push origin feature-name`
7. Submit a Pull Request

### Areas for Contribution
- Additional pattern detection algorithms
- New password generation methods
- UI/UX improvements
- Performance optimizations
- Accessibility enhancements
- Internationalization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security Notice

This tool is designed for educational and personal use. While it provides comprehensive analysis, always follow your organization's password policies and use reputable password managers for storing credentials.

## 📞 Support

If you encounter any issues or have questions:
- Open an [Issue](https://github.com/your-username/password-strength-analyzer/issues)
- Check existing [Discussions](https://github.com/your-username/password-strength-analyzer/discussions)

## 🙏 Acknowledgments

- Inspired by modern cybersecurity best practices
- Matrix-style animation inspired by classic sci-fi aesthetics
- Built with modern web standards and accessibility in mind

---

**⚡ Made with passion for cybersecurity and clean code**
