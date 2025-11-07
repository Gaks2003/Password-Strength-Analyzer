@echo off
echo ========================================
echo  Password Strength Analyzer Setup
echo ========================================
echo.

echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)
echo ✓ Git is installed

echo.
echo Initializing Git repository...
if not exist .git (
    git init
    echo ✓ Git repository initialized
) else (
    echo ✓ Git repository already exists
)

echo.
echo Adding files to Git...
git add .
git status

echo.
echo ========================================
echo  Next Steps:
echo ========================================
echo 1. Create a new repository on GitHub
echo 2. Run: git remote add origin https://github.com/YOUR-USERNAME/password-strength-analyzer.git
echo 3. Run: git commit -m "Initial commit"
echo 4. Run: git push -u origin main
echo 5. Enable GitHub Pages in repository settings
echo.
echo For detailed instructions, see DEPLOYMENT.md
echo ========================================

pause