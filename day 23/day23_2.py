class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def containsInTheNext3(self, item):
        return self.value == item or self.next.value == item or self.next.next.value == item

class CircularList:
    def __init__(self, items):
        self.start = Node(items[0])
        self.nodesDict = {items[0]: self.start}
        self.maxValue = max(items)
        node = self.start
        for i in items[1:]:
            node.next = Node(i)
            node = node.next
            self.nodesDict[i] = node
        node.next = self.start

    def move3(self, node=None):
        if not node:
            node = self.start
        pickup = node.next
        node.next = pickup.next.next.next
        destCup = node.value - 1
        if destCup == 0:
            destCup = self.maxValue
        while pickup.containsInTheNext3(destCup):
            destCup -= 1
            if destCup == 0:
                destCup = self.maxValue
        destNode = self.nodesDict[destCup]
        pickup.next.next.next = destNode.next
        destNode.next = pickup
        return node.next

    def get(self):
        yield self.start.value
        node = self.start.next
        while node != self.start:
            yield node.value
            node = node.next

cups = [int(x) for x in open("day23_input.txt").read()]
cups = cups + [x for x in range(max(cups)+1, 1000001)]
l = CircularList(cups)
i = 0
tmp = None
while i < 10000000:
    tmp = l.move3(tmp)
    i += 1
print(l.nodesDict[1].next.value * l.nodesDict[1].next.next.value)
