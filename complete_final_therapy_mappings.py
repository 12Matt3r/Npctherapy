#!/usr/bin/env python3
"""
Complete the final 2 character mappings with their therapy office versions
"""

import os
import shutil

def complete_final_therapy_mappings():
    """Map the final 2 characters with their therapy office versions"""
    
    # Define the final therapy mappings
    final_mappings = [
        {
            'source_file': '/workspace/user_input_files/IMG_8868.png',
            'dest_file': '/workspace/github_update/imgs/therapy_office/Zara the Cosmic Merchant office.png',
            'character': 'Zara the Cosmic Merchant',
            'description': 'Alien merchant with holographic displays in therapy office'
        },
        {
            'source_file': '/workspace/user_input_files/IMG_8866.png',
            'dest_file': '/workspace/github_update/imgs/therapy_office/Zombie Who Regained Memory office.png',
            'character': 'Zombie Who Regained Memory',
            'description': 'Zombie remembering past life in therapy office'
        }
    ]
    
    print("="*80)
    print("COMPLETING FINAL 2 THERAPY OFFICE MAPPINGS")
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
    print(f"FINAL THERAPY MAPPINGS COMPLETE!")
    print(f"Successfully mapped {success_count}/2 final therapy office versions")
    print("All characters should now have BOTH therapy office AND habitat versions!")
    print("="*80)
    
    return success_count

if __name__ == "__main__":
    complete_final_therapy_mappings()