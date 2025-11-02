#!/usr/bin/env python3
"""
Create original directory structure and organize all character files properly
"""

import os
import shutil

def create_original_structure():
    """Create the original directory structure and move all files"""
    
    # Create directories in original locations
    therapy_dir = "/workspace/therapy_office"
    habitats_dir = "/workspace/character_habitats"
    
    os.makedirs(therapy_dir, exist_ok=True)
    os.makedirs(habitats_dir, exist_ok=True)
    
    print("="*80)
    print("CREATING ORIGINAL DIRECTORY STRUCTURE")
    print("="*80)
    
    # Copy all therapy files from github_update to original location
    github_therapy = "/workspace/github_update/imgs/therapy_office"
    if os.path.exists(github_therapy):
        print(f"\nCopying therapy files from {github_therapy} to {therapy_dir}")
        for filename in os.listdir(github_therapy):
            src = os.path.join(github_therapy, filename)
            dst = os.path.join(therapy_dir, filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"  ✓ {filename}")
    
    # Copy all habitat files from github_update to original location  
    github_habitats = "/workspace/github_update/imgs/character_habitats"
    if os.path.exists(github_habitats):
        print(f"\nCopying habitat files from {github_habitats} to {habitats_dir}")
        for filename in os.listdir(github_habitats):
            src = os.path.join(github_habitats, filename)
            dst = os.path.join(habitats_dir, filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"  ✓ {filename}")
    
    print(f"\n{'='*80}")
    print("DIRECTORY STRUCTURE CREATED!")
    print(f"Therapy Office: {therapy_dir}")
    print(f"Character Habitats: {habitats_dir}")
    print("="*80)

if __name__ == "__main__":
    create_original_structure()