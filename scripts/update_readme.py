#!/usr/bin/env python3
"""Automatically update the robot model table in README.md from model.json files."""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_ROOT = REPO_ROOT / "library"
README_PATH = REPO_ROOT / "README.md"

START_MARKER = "<!-- ROBOT_TABLE_START -->"
END_MARKER = "<!-- ROBOT_TABLE_END -->"

def get_robot_data():
    robots = []
    # Use rglob to find all model.json 
    for model_path in LIBRARY_ROOT.rglob("model.json"):
        # We only want model.json in library/vendor/model/
        if len(model_path.relative_to(LIBRARY_ROOT).parts) != 3:
            continue
        
        try:
            with open(model_path, "r") as f:
                data = json.load(f)
                robots.append({
                    "vendor": data.get("vendor", "Unknown"),
                    "id": data.get("id", "Unknown"),
                    "author": data.get("author", "Unknown"),
                    "source": data.get("source", "").split('/')[-1] if "/" in data.get("source", "") else data.get("source", "Unknown")
                })
        except Exception as e:
            print(f"Error reading {model_path}: {e}")
            
    # Sort robots by vendor, then id
    robots.sort(key=lambda x: (x["vendor"].lower(), x["id"].lower()))
    return robots

def generate_markdown_table(robots):
    lines = [
        "| 出廠 | ID | Author | Source |",
        "|------|----|--------|--------|"
    ]
    for r in robots:
        source = r["source"].replace(".git", "")
        lines.append(f"| {r['vendor']} | `{r['id']}` | {r['author']} | {source} |")
    return "\n".join(lines)

def update_readme():
    if not README_PATH.exists():
        print(f"Error: {README_PATH} not found.")
        return

    robots = get_robot_data()
    table_md = generate_markdown_table(robots)
    
    content = README_PATH.read_text()
    
    pattern = re.compile(
        f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL
    )
    
    new_content = pattern.sub(
        f"{START_MARKER}\n{table_md}\n{END_MARKER}",
        content
    )
    
    if content != new_content:
        README_PATH.write_text(new_content)
        print(f"Successfully updated robot table in {README_PATH.name} with {len(robots)} entries.")
    else:
        print("No changes needed in README.md.")

if __name__ == "__main__":
    update_readme()
