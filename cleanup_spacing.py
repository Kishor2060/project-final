#!/usr/bin/env python3
"""
Clean up excessive vertical spacing in LaTeX chapter files.
Rules:
- Remove more than 1 consecutive blank line
- Keep single blank lines between paragraphs for readability
- Keep proper spacing after sections/subsections
"""

import os
import re

CHAPTERS_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTER_FILES = [
    "chapter1.tex",
    "chapter2.tex", 
    "chapter3.tex",
    "chapter4.tex",
    "chapter5.tex",
    "chapter6.tex"
]

def clean_file(filepath):
    """Remove excessive blank lines from a LaTeX file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace 3+ consecutive blank lines with 2 blank lines (= 1 blank line in output)
    cleaned = re.sub(r'\n\n\n+', '\n\n', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print(f"✓ Cleaned: {os.path.basename(filepath)}")

if __name__ == "__main__":
    print("Cleaning up excessive spacing in chapter files...\n")
    for chapter_file in CHAPTER_FILES:
        filepath = os.path.join(CHAPTERS_DIR, chapter_file)
        if os.path.exists(filepath):
            clean_file(filepath)
        else:
            print(f"⚠ Not found: {chapter_file}")
    print("\nDone!")
