#!/usr/bin/env python3
import re

def extract_npc_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the npcs array
    npcs_pattern = r'const npcs = \[(.*?)\];'
    npcs_match = re.search(npcs_pattern, content, re.DOTALL)
    
    if not npcs_match:
        print("Could not find npcs array")
        return []
    
    npcs_content = npcs_match.group(1)
    
    # Extract each NPC object
    npc_objects = []
    npc_pattern = r'\{[^}]*(?:\{[^}]*\}[^}]*)*\}'
    matches = re.finditer(npc_pattern, npcs_content, re.MULTILINE | re.DOTALL)
    
    current_npc = {}
    brace_count = 0
    npc_text = ""
    
    for match in matches:
        text = match.group(0)
        # Count braces
        open_braces = text.count('{')
        close_braces = text.count('}')
        brace_count += open_braces - close_braces
        
        npc_text += text
        
        if brace_count == 0 and npc_text.strip():
            # End of NPC object
            current_npc = parse_npc(npc_text)
            if current_npc and 'id' in current_npc:
                npc_objects.append(current_npc)
            npc_text = ""
    
    return npc_objects

def parse_npc(npc_text):
    npc = {}
    
    # Extract id
    id_match = re.search(r'id:\s*(\d+)', npc_text)
    if id_match:
        npc['id'] = int(id_match.group(1))
    
    # Extract npc_name
    name_match = re.search(r'npc_name:\s*"([^"]+)"', npc_text)
    if name_match:
        npc['npc_name'] = name_match.group(1)
    
    # Extract archetype
    archetype_match = re.search(r'archetype:\s*"([^"]+)"', npc_text)
    if archetype_match:
        npc['archetype'] = archetype_match.group(1)
    
    # Extract culture
    culture_match = re.search(r'culture:\s*"([^"]+)"', npc_text)
    if culture_match:
        npc['culture'] = culture_match.group(1)
    
    return npc

def main():
    filename = '/workspace/npc_therapy.html'
    npcs = extract_npc_data(filename)
    
    # Filter NPCs 1-47
    npcs_1_47 = [npc for npc in npcs if 'id' in npc and 1 <= npc['id'] <= 47]
    
    # Sort by ID
    npcs_1_47.sort(key=lambda x: x['id'])
    
    # Write output
    with open('/workspace/npc_list_1_47.txt', 'w') as f:
        f.write("NPC List 1-47\n")
        f.write("=" * 50 + "\n\n")
        
        for npc in npcs_1_47:
            session_num = npc['id']
            name = npc['npc_name']
            archetype = npc['archetype']
            culture = npc['culture']
            
            f.write(f"Session {session_num} - {name} ({archetype}) from {culture}\n")
    
    print(f"Extracted {len(npcs_1_47)} NPCs to npc_list_1_47.txt")
    return npcs_1_47

if __name__ == "__main__":
    main()