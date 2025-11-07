#!/bin/bash

echo "========================================"
echo "  Password Strength Analyzer Setup"
echo "========================================"
echo

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed"
    echo "Please install Git first:"
    echo "  Ubuntu/Debian: sudo apt install git"
    echo "  macOS: brew install git"
    echo "  Or visit: https://git-scm.com/"
    exit 1
fi
echo "✓ Git is installed"

# Initialize Git repository
echo
echo "Initializing Git repository..."
if [ ! -d ".git" ]; then
    git init
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already exists"
fi

# Add files to Git
echo
echo "Adding files to Git..."
git add .
git status

echo
echo "========================================"
echo "  Next Steps:"
echo "========================================"
echo "1. Create a new repository on GitHub"
echo "2. Run: git remote add origin https://github.com/YOUR-USERNAME/password-strength-analyzer.git"
echo "3. Run: git commit -m 'Initial commit'"
echo "4. Run: git push -u origin main"
echo "5. Enable GitHub Pages in repository settings"
echo
echo "For detailed instructions, see DEPLOYMENT.md"
echo "========================================"