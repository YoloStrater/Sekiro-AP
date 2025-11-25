import json, sys

TMPL = """# Auto-generated items
sekiro_items = [
{items}
]
"""

ITEM_TMPL = "    {{'name': {name!r}, 'id': {id}, 'classification': {classif!r}, 'weight': {weight}}},"

def convert(json_path, out_py):
    with open(json_path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)  
    rows = []
    next_id = 1000
    for i in data:
        rows.append(ITEM_TMPL.format(name=i['name'], id=next_id, classif=i.get('classification','Progression'), weight=i.get('weight',1)))
        next_id += 1
    with open(out_py, 'w', encoding='utf-8') as out:
        out.write(TMPL.format(items="\n".join(rows)))
    print(f"Wrote {out_py}")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
