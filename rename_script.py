#!/usr/bin/env python3
import os
import subprocess
import re
from pathlib import Path

def get_sorted_png_files(directory):
    """Get all PNG files in directory, sorted by filename"""
    files = []
    for file in os.listdir(directory):
        if file.endswith('.png'):
            files.append(file)
    return sorted(files)

def rename_files_to_npc_list(directory, max_files=None):
    """Rename files to npc_list_001.png format"""
    print(f"\n=== Processing {directory} ===")
    
    # Get sorted PNG files
    png_files = get_sorted_png_files(directory)
    
    if max_files:
        png_files = png_files[:max_files]
    
    print(f"Found {len(png_files)} PNG files to rename")
    
    # Create git add -A first to stage all changes
    print("Staging existing files for removal...")
    subprocess.run(['git', 'add', '-A'], cwd='/workspace/Npctherapy')
    
    # Remove all PNG files from git tracking first
    print("Removing files from git tracking...")
    subprocess.run(['git', 'rm', '-r', '--cached', f'{directory}/*.png'], cwd='/workspace/Npctherapy', check=False)
    
    # Rename files sequentially
    for i, old_name in enumerate(png_files, 1):
        old_path = os.path.join(directory, old_name)
        new_name = f"npc_list_{i:03d}.png"
        new_path = os.path.join(directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} → {new_name}")
        except FileNotFoundError:
            print(f"File not found: {old_path}")
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")
    
    print(f"Successfully renamed {len(png_files)} files in {directory}")

def main():
    os.chdir('/workspace/Npctherapy')
    
    # Rename files in both directories
    rename_files_to_npc_list('imgs/therapy_office')
    rename_files_to_npc_list('imgs/character_habitats')
    
    # Add renamed files to git
    print("\n=== Adding renamed files to git ===")
    subprocess.run(['git', 'add', 'imgs/'], cwd='/workspace/Npctherapy')
    
    # Check git status
    result = subprocess.run(['git', 'status', '--porcelain'], cwd='/workspace/Npctherapy', capture_output=True, text=True)
    print(f"Git status:\n{result.stdout}")
    
    # Commit changes
    print("\n=== Committing changes ===")
    commit_result = subprocess.run([
        'git', 'commit', '-m', 
        'Rename NPC therapy images: IMG_#### → npc_list_### format'
    ], cwd='/workspace/Npctherapy', capture_output=True, text=True)
    
    if commit_result.returncode == 0:
        print(f"Commit successful: {commit_result.stdout}")
    else:
        print(f"Commit failed: {commit_result.stderr}")
    
    # Show final status
    final_status = subprocess.run(['git', 'status'], cwd='/workspace/Npctherapy', capture_output=True, text=True)
    print(f"\nFinal git status:\n{final_status.stdout}")

if __name__ == "__main__":
    main()