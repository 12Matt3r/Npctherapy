#!/bin/bash

echo "🚀 NPC Therapy Game - GitHub Deployment Script"
echo "==============================================="

# Check if we're in the right directory
if [ ! -f "index.html" ] || [ ! -f "README.md" ]; then
    echo "❌ Error: Run this script from the npc-therapy-game directory"
    exit 1
fi

# Check if GitHub CLI is installed
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI found"
    
    # Create GitHub repository
    echo "📝 Creating GitHub repository..."
    gh repo create npc-therapy-game --public --description "Interactive therapy simulation exploring digital consciousness and existential crises of NPCs"
    
    # Set main branch and push
    echo "📤 Pushing to GitHub..."
    git branch -M main
    git push -u origin main
    
    echo "🎉 Success! Repository created and code pushed."
    echo "🌐 View your repository: https://github.com/$(gh api user --jq .login)/npc-therapy-game"
    echo "🎮 Enable GitHub Pages to make it playable online!"
    
else
    echo "❌ GitHub CLI not found"
    echo "📖 Please follow the manual setup instructions in DEPLOY.md"
    echo "🔗 Or install GitHub CLI: https://cli.github.com/"
fi