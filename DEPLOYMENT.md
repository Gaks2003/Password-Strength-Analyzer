# 🚀 Deployment Guide

This guide covers various deployment options for the Password Strength Analyzer.

## 📋 Prerequisites

- Git installed on your system
- GitHub account
- Basic knowledge of Git commands

## 🌐 GitHub Pages (Recommended)

### Automatic Deployment
1. Fork this repository
2. Go to your repository settings
3. Navigate to "Pages" section
4. Select source: "GitHub Actions"
5. The workflow will automatically deploy on push to main/master

### Manual Deployment
1. Fork/clone the repository
2. Go to Settings > Pages
3. Select source branch (main/master)
4. Select folder: `/ (root)`
5. Click Save
6. Your site will be available at: `https://your-username.github.io/password-strength-analyzer`

## 🔧 Local Development

### Using Python
```bash
# Navigate to project directory
cd password-strength-analyzer

# Start local server
python -m http.server 8000

# Open http://localhost:8000
```

### Using Node.js
```bash
# Install serve globally
npm install -g serve

# Start server
serve .

# Or use npx (no global install)
npx serve .
```

## ☁️ Cloud Platforms

### Netlify
1. Connect your GitHub repository
2. Build settings:
   - Build command: (leave empty)
   - Publish directory: `/`
3. Deploy automatically on git push

### Vercel
1. Import your GitHub repository
2. Framework preset: Other
3. Build settings:
   - Build command: (leave empty)
   - Output directory: `./`
4. Deploy

## 🔒 Security Considerations

### HTTPS
- Always use HTTPS in production
- GitHub Pages provides HTTPS automatically
- Configure SSL certificates for custom domains

### Content Security Policy
Add to your HTML `<head>`:
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; font-src 'self' https://cdnjs.cloudflare.com; script-src 'self';">
```

## 🌍 Custom Domain

### GitHub Pages
1. Add CNAME file with your domain
2. Configure DNS records:
   - CNAME: `your-username.github.io`
   - Or A records: GitHub Pages IPs
3. Enable HTTPS in repository settings

## 📞 Support

If you encounter deployment issues:
1. Check the Issues page
2. Review deployment logs
3. Verify all files are uploaded correctly
4. Test locally first