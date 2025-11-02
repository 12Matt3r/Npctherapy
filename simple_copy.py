#!/usr/bin/env python3
"""
Simple directory and file operations without bash
"""

import os
import shutil

# Create directories
os.makedirs("/workspace/therapy_office", exist_ok=True)
os.makedirs("/workspace/character_habitats", exist_ok=True)

# Copy therapy files
therapy_src = "/workspace/github_update/imgs/therapy_office"
if os.path.exists(therapy_src):
    for file in os.listdir(therapy_src):
        src = os.path.join(therapy_src, file)
        dst = os.path.join("/workspace/therapy_office", file)
        if os.path.isfile(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"Copied: {file}")

# Copy habitat files  
habitat_src = "/workspace/github_update/imgs/character_habitats"
if os.path.exists(habitat_src):
    for file in os.listdir(habitat_src):
        src = os.path.join(habitat_src, file)
        dst = os.path.join("/workspace/character_habitats", file)
        if os.path.isfile(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"Copied: {file}")

print("Original directory structure created!")