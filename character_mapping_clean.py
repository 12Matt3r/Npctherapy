#!/usr/bin/env python3
"""
Character Mapping Script - Rename NPC therapy files according to character mapping
"""

import os

def main():
    base_dir = "/workspace/github_update/imgs"
    therapy_dir = os.path.join(base_dir, "therapy_office")
    habitats_dir = os.path.join(base_dir, "character_habitats")
    
    print("Starting character mapping rename process...")
    
    # Therapy office mappings
    therapy_mappings = {
        "IMG_8801.png": "Bishop-47 (Military AI) office.png",
        "IMG_8855.png": "Bishop-47 (Military AI) office.png",
        "IMG_8857.png": "Brother Sebastian Tidecurrent (Underwater Street Preacher) office.png",
        "IMG_8858.png": "Captain Loop (Space Patrol) office.png", 
        "IMG_8860.png": "Captain Marcus (Respawning Soldier) office.png",
        "IMG_8861.png": "Daisy.exe (Android Companion) office.png",
        "IMG_8862.png": "Fex'tara - Ferret-Looking Character in Black Bodysuit office.png",
        "IMG_8863.png": "Fex'tara - Ferret-Looking Character in Black Bodysuit office.png",
        "IMG_8864.png": "Gerald Ironpeak (Tired Quest Giver) office.png",
        "IMG_8866.png": "Gerald Ironpeak (Tired Quest Giver) office.png",
        "IMG_8867.png": "Glitch.exe (Corrupted Program) office.png",
        "IMG_8868.png": "Harmonix 'The Forgotten Melodies' office.png",
        "IMG_8870.png": "Harmonix 'The Forgotten Melodies' office.png",
        "IMG_8871.png": "Jake (Forgotten Platformer Hero) office.png",
        "IMG_8872.png": "Jake (Forgotten Platformer Hero) office.png",
        "IMG_8873.png": "King Lepidoptera IX (Truth-Addicted Ex-Monarch) office.png",
        "IMG_8875.png": "King Lepidoptera IX (Truth-Addicted Ex-Monarch) office.png",
        "IMG_8876.png": "Luna (Heartbroken Rhythm Dancer) office.png",
        "IMG_8878.png": "Luna (Heartbroken Rhythm Dancer) office.png",
        "IMG_8879.png": "NoEmotion Goldmask – Happy Version office.png",
        "IMG_8880.png": "NoEmotion Goldmask – Happy Version office.png",
        "IMG_8881.png": "R0GU3: Rogue AI Companion office.png",
        "IMG_8882.png": "R0GU3: Rogue AI Companion office.png",
        "IMG_8883.png": "Rustjaw (Wasteland Mechanic) office.png",
        "IMG_8884.png": "Rustjaw (Wasteland Mechanic) office.png",
        "IMG_8885.png": "Sarah the Farm Sim Widow office.png",
        "IMG_8886.png": "Sarah the Farm Sim Widow office.png",
        "IMG_8887.png": "Scales 'The Comedian' Crimson office.png",
        "IMG_8888.png": "Scales 'The Comedian' Crimson office.png",
        "IMG_8889.png": "Seraphina 'Heals-A-Lot' Dawnwhisper office.png",
        "IMG_8890.png": "Seraphina 'Heals-A-Lot' Dawnwhisper office.png",
        "IMG_8891.png": "Specter 'Speed' Wraithson office.png",
        "IMG_8895.png": "Specter 'Speed' Wraithson office.png",
        "IMG_8896.png": "The Battle Royale Vendor office.png",
        "IMG_8897.png": "The Battle Royale Vendor office.png",
        "IMG_8898.png": "The Dungeon Chest Mimic office.png",
        "IMG_8899.png": "The Glitched Priest office.png",
        "IMG_8900.png": "The Idle Clicker Manager office.png",
        "IMG_8901.png": "The Idle Clicker Manager office.png",
        "IMG_8902.png": "The Lost Tetris Block office.png",
        "IMG_8903.png": "The Lost Tetris Block office.png",
        "IMG_8904.png": "The Platforming Princess office.png",
        "IMG_8906.png": "The Puzzle Cube office.png",
        "IMG_8907.png": "The Puzzle Cube office.png",
        "IMG_8908.png": "The Silent Couple and Their Ghost office.png",
        "IMG_8909.png": "The Tower Defense Turret office.png",
        "IMG_8910.png": "Tiko the Quest Vendor office.png",
        "IMG_8911.png": "White Rabbit-Human Hybrid office.png",
        "IMG_8912.png": "Worm office.png"
    }
    
    # Character habitats mappings
    habitat_mappings = {
        "IMG_8801.png": "Bishop-47 (Military AI) from Tactical Simulation.png",
        "IMG_8858.png": "Captain Loop (Space Patrol) from Hard Sci-Fi.png",
        "IMG_8860.png": "Captain Marcus (Respawning Soldier) from Military FPS.png",
        "IMG_8862.png": "Fex'tara - Ferret-Looking Character in Black Bodysuit from Meta Horror.png",
        "IMG_8864.png": "Gerald Ironpeak (Tired Quest Giver) from Fantasy RPG.png",
        "IMG_8867.png": "Glitch.exe (Corrupted Program) from Digital Consciousness.png",
        "IMG_8871.png": "Jake (Forgotten Platformer Hero) from Classic Gaming.png",
        "IMG_8872.png": "Jake (Forgotten Platformer Hero) from Classic Gaming.png",
        "IMG_8875.png": "King Lepidoptera IX (Truth-Addicted Ex-Monarch) from Political Satire.png",
        "IMG_8878.png": "Luna (Heartbroken Rhythm Dancer) from Streaming Entertainment.png",
        "IMG_8880.png": "NoEmotion Goldmask – Happy Version from Fantasy Mysticism.png",
        "IMG_8882.png": "R0GU3: Rogue AI Companion from AI Consciousness Revolution.png",
        "IMG_8884.png": "Rustjaw (Wasteland Mechanic) from Post-Apocalyptic.png",
        "IMG_8888.png": "Scales 'The Comedian' Crimson from Classic Animation.png",
        "IMG_8890.png": "Seraphina 'Heals-A-Lot' Dawnwhisper from Online Gaming Community.png",
        "IMG_8895.png": "Specter 'Speed' Wraithson from Racing Simulation.png",
        "IMG_8897.png": "The Battle Royale Vendor from Competitive Gaming.png",
        "IMG_8899.png": "The Glitched Priest from Religious Simulation.png",
        "IMG_8901.png": "The Idle Clicker Manager from Idle Gaming Economy.png",
        "IMG_8902.png": "The Lost Tetris Block from Abstract Puzzle Reality.png",
        "IMG_8903.png": "The Lost Tetris Block from Abstract Puzzle Reality.png",
        "IMG_8906.png": "The Puzzle Cube from Abstract Puzzle Reality.png",
        "IMG_8907.png": "The Puzzle Cube from Abstract Puzzle Reality.png",
        "IMG_8908.png": "The Silent Couple and Their Ghost from Relationship Drama.png",
        "IMG_8909.png": "The Tower Defense Turret from Tower Defense Strategy.png",
        "IMG_8911.png": "White Rabbit-Human Hybrid from Children's Entertainment.png",
        "IMG_8912.png": "Worm from Side-Scroller.png",
        "IMG_8914.png": "Zombie Who Regained Memory from Horror Survival.png",
        "IMG_8917.png": "Zara the Cosmic Merchant from Space Opera.png",
        "IMG_8919.png": "NoEmotion Goldmask - Dual Mood from Psychological Drama.png"
    }
    
    # Process therapy office files
    if os.path.exists(therapy_dir):
        print(f"\nProcessing therapy_office folder...")
        files_renamed = 0
        
        for old_name in os.listdir(therapy_dir):
            if old_name.endswith('.png') and old_name in therapy_mappings:
                old_path = os.path.join(therapy_dir, old_name)
                new_name = therapy_mappings[old_name]
                new_path = os.path.join(therapy_dir, new_name)
                
                print(f"Renaming: {old_name} -> {new_name}")
                os.rename(old_path, new_path)
                files_renamed += 1
        
        print(f"Therapy office: {files_renamed} files renamed")
    
    # Process character habitats files
    if os.path.exists(habitats_dir):
        print(f"\nProcessing character_habitats folder...")
        files_renamed = 0
        
        for old_name in os.listdir(habitats_dir):
            if old_name.endswith('.png') and old_name in habitat_mappings:
                old_path = os.path.join(habitats_dir, old_name)
                new_name = habitat_mappings[old_name]
                new_path = os.path.join(habitats_dir, new_name)
                
                print(f"Renaming: {old_name} -> {new_name}")
                os.rename(old_path, new_path)
                files_renamed += 1
        
        print(f"Character habitats: {files_renamed} files renamed")
    
    print("\nCharacter mapping rename completed!")
    
    # Show summary
    print("\n" + "="*60)
    print("SUMMARY - Character-to-File Mapping")
    print("="*60)
    
    # Create character summary
    therapy_files = [f for f in os.listdir(therapy_dir) if f.endswith('.png')] if os.path.exists(therapy_dir) else []
    habitat_files = [f for f in os.listdir(habitats_dir) if f.endswith('.png')] if os.path.exists(habitats_dir) else []
    
    print(f"Therapy Office: {len(therapy_files)} files")
    print(f"Character Habitats: {len(habitat_files)} files")
    print(f"Total: {len(therapy_files) + len(habitat_files)} files")

if __name__ == "__main__":
    main()