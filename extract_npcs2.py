#!/usr/bin/env python3
import re

# Read the file
with open('/workspace/npc_therapy.html', 'r') as f:
    content = f.read()

# Find the npcs array
npcs_start = content.find('const npcs = [')
if npcs_start == -1:
    print("Could not find npcs array")
    exit(1)

npcs_content = content[npcs_start:]
# Find the end of the array (be careful with nested braces)
brace_count = 0
array_start = npcs_content.find('[')
npcs_end = -1
for i, char in enumerate(npcs_content[array_start:]):
    if char == '{':
        brace_count += 1
    elif char == '}':
        brace_count -= 1
        if brace_count == 0:
            npcs_end = array_start + i + 1
            break

if npcs_end == -1:
    print("Could not find end of npcs array")
    exit(1)

npcs_content = npcs_content[array_start+1:npcs_end]

# Split into individual NPCs
npc_texts = []
current_npc = []
brace_count = 0

for char in npcs_content:
    if char == '{':
        brace_count += 1
        current_npc.append(char)
    elif char == '}':
        brace_count -= 1
        current_npc.append(char)
        if brace_count == 0 and current_npc:
            npc_texts.append(''.join(current_npc))
            current_npc = []
    else:
        current_npc.append(char)

# Parse each NPC
npcs = []
for npc_text in npc_texts:
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
    
    if npc and 'id' in npc:
        npcs.append(npc)

# Filter NPCs 1-47
npcs_1_47 = [npc for npc in npcs if 1 <= npc['id'] <= 47]

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

# Show all extracted NPCs
for npc in npcs_1_47:
    print(f"Session {npc['id']} - {npc['npc_name']} ({npc['archetype']}) from {npc['culture']}")