#!/usr/bin/env python3
"""
Clean up the directories to keep only properly mapped character files
"""

import os
import glob

def cleanup_character_files():
    """Remove unmapped IMG files and keep only properly mapped characters"""
    
    print("="*80)
    print("CLEANING UP CHARACTER FILES")
    print("="*80)
    
    therapy_dir = "/workspace/therapy_office"
    habitats_dir = "/workspace/character_habitats"
    
    # Define what properly mapped files should look like
    def is_mapped_file(filename):
        # Should have either " office.png" or " from [setting].png"
        return " office.png" in filename or " from " in filename
    
    # Clean therapy office directory
    print("\nCleaning therapy_office directory...")
    therapy_files = os.listdir(therapy_dir)
    unmapped_therapy = [f for f in therapy_files if not is_mapped_file(f)]
    
    for file in unmapped_therapy:
        file_path = os.path.join(therapy_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"  ❌ Removed unmapped: {file}")
    
    mapped_therapy = [f for f in therapy_files if is_mapped_file(f)]
    print(f"  ✅ Kept {len(mapped_therapy)} properly mapped therapy files")
    
    # Clean habitats directory
    print("\nCleaning character_habitats directory...")
    habitat_files = os.listdir(habitats_dir)
    unmapped_habitat = [f for f in habitat_files if not is_mapped_file(f)]
    
    for file in unmapped_habitat:
        file_path = os.path.join(habitats_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"  ❌ Removed unmapped: {file}")
    
    mapped_habitat = [f for f in habitat_files if is_mapped_file(f)]
    print(f"  ✅ Kept {len(mapped_habitat)} properly mapped habitat files")
    
    print(f"\n{'='*80}")
    print("FINAL COUNT:")
    print(f"Therapy Office: {len(mapped_therapy)} files")
    print(f"Character Habitats: {len(mapped_habitat)} files") 
    print(f"Total Character Files: {len(mapped_therapy) + len(mapped_habitat)} files")
    print("="*80)
    
    # Verify we have exactly 34 complete matches
    print("\nVERIFYING COMPLETE MATCHES...")
    therapy_names = set()
    habitat_names = set()
    
    for file in mapped_therapy:
        if " office.png" in file:
            char_name = file.replace(" office.png", "")
            therapy_names.add(char_name)
    
    for file in mapped_habitat:
        if " from " in file:
            char_name = file.split(" from ")[0]
            habitat_names.add(char_name)
    
    complete_matches = therapy_names.intersection(habitat_names)
    print(f"Characters with both versions: {len(complete_matches)}")
    print(f"Characters with only therapy: {len(therapy_names - habitat_names)}")
    print(f"Characters with only habitat: {len(habitat_names - therapy_names)}")

if __name__ == "__main__":
    cleanup_character_files()