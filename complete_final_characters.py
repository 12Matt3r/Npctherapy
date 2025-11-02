#!/usr/bin/env python3
"""
Complete the final 5 character mappings
"""

import os
import shutil

def complete_final_characters():
    """Map the final 5 characters with their habitat versions"""
    
    # Define the final character mappings
    final_mappings = [
        {
            'source_file': '/workspace/user_input_files/IMG_8899.png',
            'dest_file': '/workspace/github_update/imgs/character_habitats/The Platforming Princess from Platformer Adventure.png',
            'character': 'The Platforming Princess',
            'description': 'Princess in castle setting'
        },
        {
            'source_file': '/workspace/user_input_files/IMG_8940.png', 
            'dest_file': '/workspace/github_update/imgs/character_habitats/Tiko the Quest Vendor from Fantasy Village.png',
            'character': 'Tiko the Quest Vendor',
            'description': 'Quest giver with scroll in village'
        },
        {
            'source_file': '/workspace/user_input_files/IMG_8880.png',
            'dest_file': '/workspace/github_update/imgs/character_habitats/The Dungeon Chest Mimic from Fantasy Dungeon.png',
            'character': 'The Dungeon Chest Mimic',
            'description': 'Mimic chest wanting hugs'
        },
        {
            'source_file': '/workspace/user_input_files/IMG_8874.png',
            'dest_file': '/workspace/github_update/imgs/character_habitats/Zombie Who Regained Memory from Post-Apocalyptic.png',
            'character': 'Zombie Who Regained Memory',
            'description': 'Zombie with remember-eat-forget-repeat cycle'
        },
        {
            'source_file': '/workspace/user_input_files/IMG_8869.png',
            'dest_file': '/workspace/github_update/imgs/character_habitats/Zara the Cosmic Merchant from Space Trading.png',
            'character': 'Zara the Cosmic Merchant',
            'description': 'Cosmic merchant with economy rich life poor message'
        }
    ]
    
    print("="*80)
    print("COMPLETING FINAL 5 CHARACTER MAPPINGS")
    print("="*80)
    
    success_count = 0
    
    for mapping in final_mappings:
        print(f"\nMapping: {mapping['character']}")
        print(f"Description: {mapping['description']}")
        print(f"Source: {mapping['source_file']}")
        print(f"Destination: {mapping['dest_file']}")
        
        # Check if source file exists
        if not os.path.exists(mapping['source_file']):
            print(f"❌ Source file not found: {mapping['source_file']}")
            continue
            
        # Create destination directory if needed
        dest_dir = os.path.dirname(mapping['dest_file'])
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copy the file
        try:
            shutil.copy2(mapping['source_file'], mapping['dest_file'])
            print(f"✅ Successfully copied to: {mapping['dest_file']}")
            success_count += 1
        except Exception as e:
            print(f"❌ Error copying file: {e}")
    
    print(f"\n{'='*80}")
    print(f"FINAL MAPPING COMPLETE!")
    print(f"Successfully mapped {success_count}/5 final characters")
    print("All characters should now have both therapy office and habitat versions!")
    print("="*80)
    
    return success_count

if __name__ == "__main__":
    complete_final_characters()