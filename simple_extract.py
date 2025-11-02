#!/usr/bin/env python3
import re

# Read the file
with open('/workspace/npc_therapy.html', 'r') as f:
    content = f.read()

# Find all NPCs with IDs 1-47
npc_data = []

for npc_id in range(1, 48):
    # Find the NPC with this ID
    pattern = rf'id:\s*{npc_id},'
    match = re.search(pattern, content)
    
    if match:
        # Find the start of this NPC object
        start = match.start()
        
        # Find the end by looking for the closing brace that matches the opening brace
        # We need to count braces
        brace_count = 0
        in_string = False
        escaped = False
        i = start
        
        # Find the opening brace
        while i >= 0 and content[i] != '{':
            i -= 1
        
        if i >= 0:
            start = i
        
        # Now count braces to find the end
        i = start
        while i < len(content):
            char = content[i]
            
            if not in_string:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # End of this NPC
                        npc_text = content[start:i+1]
                        break
            elif char == '\\':
                escaped = not escaped
            elif char == '"' and not escaped:
                in_string = not in_string
            elif char != '\\':
                escaped = False
            
            i += 1
        
        # Extract the data
        name_match = re.search(r'npc_name:\s*"([^"]+)"', npc_text)
        archetype_match = re.search(r'archetype:\s*"([^"]+)"', npc_text)
        culture_match = re.search(r'culture:\s*"([^"]+)"', npc_text)
        
        if name_match and archetype_match and culture_match:
            npc_data.append({
                'id': npc_id,
                'name': name_match.group(1),
                'archetype': archetype_match.group(1),
                'culture': culture_match.group(1)
            })

# Write output
with open('/workspace/npc_list_1_47.txt', 'w') as f:
    f.write("NPC List 1-47\n")
    f.write("=" * 50 + "\n\n")
    
    for npc in npc_data:
        f.write(f"Session {npc['id']} - {npc['name']} ({npc['archetype']}) from {npc['culture']}\n")

print(f"Extracted {len(npc_data)} NPCs")
for npc in npc_data:
    print(f"Session {npc['id']}: {npc['name']} ({npc['archetype']}) from {npc['culture']}")
