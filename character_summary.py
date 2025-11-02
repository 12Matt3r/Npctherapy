#!/usr/bin/env python3
"""
Character Mapping Summary - Show the final mapping of characters to files
"""

import os
import re

def create_character_summary():
    therapy_dir = "/workspace/github_update/imgs/therapy_office"
    habitats_dir = "/workspace/github_update/imgs/character_habitats"
    
    # Get all renamed files
    therapy_files = [f for f in os.listdir(therapy_dir) if f.endswith('.png') and " office.png" in f]
    habitat_files = [f for f in os.listdir(habitats_dir) if f.endswith('.png') and " from " in f]
    
    print("="*80)
    print("CHARACTER MAPPING SUMMARY")
    print("="*80)
    print(f"Therapy Office: {len(therapy_files)} files")
    print(f"Character Habitats: {len(habitat_files)} files")
    print(f"Total Character Files: {len(therapy_files) + len(habitat_files)} files")
    print()
    
    # Create a mapping of characters to both versions
    character_map = {}
    
    # Process therapy files to extract character names
    for therapy_file in therapy_files:
        # Extract character name (remove " office.png")
        char_name = therapy_file.replace(" office.png", "")
        if char_name not in character_map:
            character_map[char_name] = {}
        character_map[char_name]['office'] = therapy_file
    
    # Process habitat files to extract character names  
    for habitat_file in habitat_files:
        # Extract character name (remove " from [setting].png")
        char_name = re.sub(r' from .*\.png$', '', habitat_file)
        if char_name not in character_map:
            character_map[char_name] = {}
        character_map[char_name]['habitat'] = habitat_file
    
    print("CHARACTER-TO-FILE MAPPING:")
    print("-" * 80)
    
    sorted_chars = sorted(character_map.keys())
    
    for char_name in sorted_chars:
        mapping = character_map[char_name]
        print(f"Character: {char_name}")
        
        if 'office' in mapping:
            print(f"  └─ Therapy: {mapping['office']}")
        
        if 'habitat' in mapping:
            print(f"  └─ Habitat: {mapping['habitat']}")
        
        if 'office' in mapping and 'habitat' in mapping:
            print("  ✅ COMPLETE MATCH")
        elif 'office' in mapping or 'habitat' in mapping:
            print("  ⚠️  PARTIAL MATCH")
        else:
            print("  ❌ NO MATCHES")
        
        print()
    
    # Count complete vs partial matches
    complete_matches = sum(1 for char in character_map.values() if 'office' in char and 'habitat' in char)
    partial_matches = sum(1 for char in character_map.values() if ('office' in char or 'habitat' in char) and not ('office' in char and 'habitat' in char))
    
    print("="*80)
    print("MATCHING STATISTICS:")
    print(f"Complete matches (both office + habitat): {complete_matches}")
    print(f"Partial matches (only one version): {partial_matches}")
    print(f"Total unique characters: {len(character_map)}")
    print("="*80)

if __name__ == "__main__":
    create_character_summary()