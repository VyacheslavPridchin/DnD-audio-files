import os
import json

root_dir = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.basename(__file__)
allowed_exts = {'.mp3', '.wav'}

result = []

for current_dir, _, files in os.walk(root_dir):
    for file in files:
        if file == script_name:
            continue
        if os.path.splitext(file)[1].lower() in allowed_exts:
            full_path = os.path.join(current_dir, file)
            rel_path = os.path.relpath(full_path, root_dir)
            print(rel_path)
            result.append(rel_path.replace('\\', '/'))

with open(os.path.join(root_dir, 'index.json'), 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
