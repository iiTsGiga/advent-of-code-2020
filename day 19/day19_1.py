import re

rules_inp, messages_inp = ''.join(open("day19_input.txt").readlines()).split("\n\n")
rules = dict()
for rule in rules_inp.split("\n"):
    i, r = rule.split(": ")
    rules[int(i)] = r.strip('"')
messages = messages_inp.split("\n")

def evaluate(i):
    rule = rules[i]
    if rule in "ab":
        return rule
    parts = rule.split(" | ")
    for j, p in enumerate(parts):
        r = p.split()
        for x, n in enumerate(r):
            ev = evaluate(int(n))
            if ev in "ab":
                r[x] = ev
            else:
                r[x] = '(' + ev + ')'
        parts[j] = '(' + ''.join(r) + ')'
    return '(' + '|'.join(parts) + ')'

expr = evaluate(0)
counter = 0
for msg in messages:
    if re.match(f"^{expr}$", msg):
        counter += 1
print(counter)



