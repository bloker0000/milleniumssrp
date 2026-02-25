import re

with open(r"c:\Users\noahl\OneDrive - Grafisch Lyceum Rotterdam\Documents\projects\roblox\SCPRP\MergedGUI\Main.luau", "r", encoding="utf-8") as f:
    lines = f.readlines()

depth = 0
min_depth = 0
issues = []
keywords_open = re.compile(r'\b(function|if|for|while|do|repeat)\b')
keywords_close = re.compile(r'\b(end|until)\b')
elseif_re = re.compile(r'\belseif\b')
string_re = re.compile(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|\[(=*)\[.*?\]\2\])')

for i, raw_line in enumerate(lines, 1):
    line = raw_line.strip()
    if line.startswith("--"):
        continue
    cleaned = string_re.sub('""', line)
    cleaned = re.sub(r'--.*$', '', cleaned)
    
    opens = len(keywords_open.findall(cleaned))
    closes = len(keywords_close.findall(cleaned))
    
    elseifs = len(elseif_re.findall(cleaned))
    if_count = len(re.findall(r'\bif\b', cleaned))
    net_ifs = if_count - elseifs
    
    do_count = len(re.findall(r'\bdo\b', cleaned))
    for_count = len(re.findall(r'\bfor\b', cleaned))
    while_count = len(re.findall(r'\bwhile\b', cleaned))
    loop_do = for_count + while_count
    standalone_do = do_count - loop_do
    if standalone_do < 0:
        standalone_do = 0
    
    func_count = len(re.findall(r'\bfunction\b', cleaned))
    repeat_count = len(re.findall(r'\brepeat\b', cleaned))
    
    actual_opens = func_count + net_ifs + do_count + repeat_count
    if actual_opens < 0:
        actual_opens = 0
    
    old_depth = depth
    depth += actual_opens - closes
    
    if depth < 0:
        issues.append(f"  Line {i}: depth went negative ({depth}): {line[:80]}")
    if depth < min_depth:
        min_depth = depth

if issues:
    print("ISSUES FOUND:")
    for issue in issues[:20]:
        print(issue)
else:
    print("No negative depth issues found")
print(f"\nFinal depth: {depth}")
print(f"Min depth: {min_depth}")
if depth == 0:
    print("BALANCED: All blocks properly closed")
elif depth > 0:
    print(f"UNBALANCED: {depth} unclosed block(s)")
else:
    print(f"UNBALANCED: {abs(depth)} extra end(s)")
