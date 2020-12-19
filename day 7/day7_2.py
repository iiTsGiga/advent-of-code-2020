rules = [line.replace("\n", "") for line in open("day7_input.txt")]

class Bag:
    def __init__(self, color):
        self.children = set()
        self.color = color

    def add_children(self, child):
        self.children.add(child)

bags = dict()

for rule in rules:
    parent, children = rule.split(" bags contain ")
    if parent not in bags.keys():
        bags[parent] = Bag(parent)
    children = children.split(", ")
    for child in children:
        child = child.split()
        if child[0] == "no":
            break
        amount = int(child[0])
        child = child[1] + " " + child[2]
        bags[parent].add_children((child, amount))

def deep_search(bag: str, count: int = 0) -> int:
    if len(bags[bag].children) == 0:
        return 0
    own_sum = 0
    for child in bags[bag].children:
        count += child[1] * deep_search(child[0])
        own_sum += child[1]
    return count + own_sum

print(deep_search("shiny gold"))
