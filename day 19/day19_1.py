import re

rules_inp, messages_inp = ''.join(open("day19_input.txt").readlines()).split("\n\n")
rules = dict()
for rule in rules_inp.split("\n"):
    i, r = rule.split(": ")
    rules[int(i)] = r.strip('"')
messages = messages_inp.split("\n")

def evaluate(i):
    if rules[i] in "ab":
        return rules[i]
    parts = rules[i].split(" | ")
    for j, p in enumerate(parts):
        parts[j] = '(' + ''.join(evaluate(int(n)) for n in p.split()) + ')'
    return '(' + '|'.join(parts) + ')'

expr = evaluate(0)
counter = 0
for msg in messages:
    if re.match(f"^{expr}$", msg):
        counter += 1
print(counter)



