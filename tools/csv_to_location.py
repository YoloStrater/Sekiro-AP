import csv
import sys

TEMPLATE = """# Auto-generated locations
sekiro_locations = [
{items}
]
"""

ROW_TMPL = "    {{'name': {name!r}, 'address': {addr}, 'region': {region!r}, 'weight': {weight}}},"

def convert(csv_path, out_py):
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        addr = 1000
        for r in reader:
            name = r['check_name']
            region = r.get('region', 'Unknown')
            weight = r.get('weight', '1')
            rows.append(ROW_TMPL.format(name=name, addr=addr, region=region, weight=weight))
            addr += 1
    content = TEMPLATE.format(items="\n".join(rows))
    with open(out_py, 'w', encoding='utf-8') as out:
        out.write(content)
    print(f"Wrote {out_py} with {len(rows)} locations")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python csv_to_locations.py checks.csv ../worlds/sekiro/locations.py")
    else:
        convert(sys.argv[1], sys.argv[2])
