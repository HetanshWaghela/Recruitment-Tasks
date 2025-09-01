# Okay so the unstructured to structured that I have selected is markdown to json

import re
import json

def markdown_to_json(markdown_text):
    content = {"Title": None, "Sections": []}
    current_section = None
    
    for line in markdown_text.splitlines():
        line = line.strip()
        
        if line.startswith("# "):
            content["Title"] = line[2:].strip()
        
        elif line.startswith("## "):
            if current_section:
                content["Sections"].append(current_section)
            
            current_section = {"Heading": line[3:].strip(), "Points": []}
        
        elif line.startswith("- "):
            if current_section:
                current_section["Points"].append(line[2:].strip())
    
    if current_section:
        content["Sections"].append(current_section)
    
    return content

markdown_text = """
# MY LIST

## Things i need to buy
- Chocolate
- Veggies
- Milk

## THings i need to learn
- Machine Learning
- Deep Learning
- Reinforcement Learning
"""

structured_data = markdown_to_json(markdown_text)
print(json.dumps(structured_data, indent=2))
