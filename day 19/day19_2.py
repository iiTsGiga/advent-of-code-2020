import re

rules_inp, messages_inp = ''.join(open('day19_input.txt').readlines()).split('\n\n')
messages = messages_inp.split('\n')
rules = dict()
for rule in rules_inp.split('\n'):
    i, r = rule.split(': ')
    rules[int(i)] = r.strip('\"')

def evaluate(i):
    rule = rules[i]
    if rule in 'ab':
        return rule
    parts = rule.split(' | ')
    for j, p in enumerate(parts):
        r = p.split()
        for x, n in enumerate(r):
            r[x] = evaluate(int(n))
        parts[j] = '(' + ''.join(r) + ')'
    return '(' + '|'.join(parts) + ')'

c1, c2 = 0, -1
i = 2
while c1 != c2:
    rules[8] = '42' + (' |' if i > 2 else '') + ' |'.join(' 42'*j for j in range(2, i))
    rules[11] = '42 31' + (' |' if i > 2 else '') + ' |'.join(' 42'*j + ' 31'*j for j in range(2, i))
    expr = evaluate(0)
    counter = 0
    for msg in messages:
        if re.match(f'^{expr}$', msg):
            counter += 1
    c2 = c1
    c1 = counter
    i += 1
print(c1)
