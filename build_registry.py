import os
import glob
import re

skills_dir = os.path.expanduser("~/.agents/skills")
registry_file = os.path.expanduser("~/.agents/agent_registry.md")

md_files = glob.glob(os.path.join(skills_dir, "*", "SKILL.md"))

registry_content = "# Agent Registry\n\nThis registry contains the names and descriptions of all specialized domain agents available to the Swarm Coordinator.\n\n"

for md_file in sorted(md_files):
    agent_slug = os.path.basename(os.path.dirname(md_file))
    
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get human name from YAML if possible
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    human_name = name_match.group(1).strip(' "\'') if name_match else agent_slug
    
    # Split out the YAML frontmatter
    parts = content.split('---', 2)
    body = parts[2] if len(parts) > 2 else content
    
    # Find the first real paragraph of markdown
    paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]
    desc = "Specialized domain agent."
    
    for p in paragraphs:
        # Ignore markdown headers, html tags, code blocks, blockquotes
        if p.startswith('#') or p.startswith('<') or p.startswith('```') or p.startswith('>'):
            continue
        
        # Clean newlines into spaces
        p = re.sub(r'\s+', ' ', p)
        
        if len(p) > 25:
            desc = p
            break
            
    # Fallback to YAML description if markdown parsing failed
    if desc == "Specialized domain agent.":
        desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
        if desc_match:
            d = desc_match.group(1).strip(' "\'')
            if d not in ['>', '>-', '|', '|-']:
                desc = d
                
    # Truncate if insanely long
    if len(desc) > 300:
        desc = desc[:297] + "..."
        
    registry_content += f"- **{agent_slug}**: {desc}\n"

with open(registry_file, "w", encoding="utf-8") as f:
    f.write(registry_content)

print(f"Successfully generated accurate agent registry at {registry_file}")
