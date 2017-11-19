import queue

class node:
    def __init__(self, name):
        self.nodes = []
        self.color = 'white'
        self.name = name
    
    def add(self, neigh):
        self.nodes.append(neigh)
        neigh.nodes.append(self)

class graph:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)


friends = graph()

mike = node('Michael')
emily = node('Emily')
sahl = node('Sahl')
arielle = node('Arielle')
nick = node('Nick')
sakib = node('Sakib')
david = node('David')
brian = node('Brian')
aakash = node('Aakash')

mike.add(david)
mike.add(aakash)
aakash.add(nick)
nick.add(sakib)
sakib.add(emily)
sakib.add(sahl)
sahl.add(brian)
brian.add(arielle)

friends.add(sakib)

def can_split(graph):
    qu = queue.Queue()
    color = 'red'
    for node in graph.nodes:
        node.color = color
        color = switch(color)
        qu.put(node)

    while not qu.empty():
        node = qu.get()
        for n in node.nodes:
            if n.color == 'white':
                n.color = switch(node.color)
                qu.put(n)
            elif n.color == node.color:
                return False

    return True

def switch(color):
    if color == 'red':
        return 'black'
    return 'red'

print(can_split(friends))