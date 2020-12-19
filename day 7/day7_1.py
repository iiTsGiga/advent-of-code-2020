rules = [line.replace("\n", "") for line in open("day7_input.txt")]

class Bag:
    def __init__(self, color):
        self.parents = set()
        self.color = color

    def add_parent(self, parent):
        self.parents.add(parent)

bags = dict()

for rule in rules:
    parent, children = rule.split(" bags contain ")
    children = children.split(", ")
    for child in children:
        child = child.split()
        child = child[1] + " " + child[2]
        if child not in bags.keys():
            bags[child] = Bag(child)
        bags[child].add_parent(parent)

def deep_search(bag: str):
    if bag not in bags.keys():
        return
    for parent in bags[bag].parents:
        contain_shiny_gold.add(parent)
        deep_search(parent)

contain_shiny_gold = set()
deep_search("shiny gold")
print(len(contain_shiny_gold))
