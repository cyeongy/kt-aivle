import sys, re

s = 10

query = sys.stdin.readline()
query.rstrip()
pattern = re.compile(r"[(\\)(\')(\")]")

query = query.replace("\\", "\\\\")

query = re.sub("[\']", "\\\'", query)
query = re.sub("[\"]", "\\\"", query)

pat = re.compile(r'[369]')
print(len(re.findall(pat, query)))
