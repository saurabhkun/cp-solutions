import os

def count_files(folder):
    count = 0
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder):
            for f in files:
                if f.endswith(".cpp") or f.endswith(".java"):
                    count += 1
    return count

leetcode = count_files("leetcode")
gfg = count_files("gfg")
cf = count_files("codeforces")
total = leetcode + gfg + cf

new_block = f"""<!-- AUTO-UPDATED BY GITHUB ACTIONS — DO NOT EDIT THIS SECTION MANUALLY -->
| Platform   | Problems Solved |
|------------|-----------------|
| LeetCode   | {leetcode}               |
| GFG        | {gfg}               |
| Codeforces | {cf}               |
| **Total**  | **{total}**           |
<!-- END STATS -->"""

with open("README.md", "r") as f:
    content = f.read()

start = content.index("<!-- AUTO-UPDATED BY GITHUB ACTIONS")
end = content.index("<!-- END STATS -->") + len("<!-- END STATS -->")
content = content[:start] + new_block + content[end:]

with open("README.md", "w") as f:
    f.write(content)

print(f"Updated: LC={leetcode}, GFG={gfg}, CF={cf}, Total={total}") 