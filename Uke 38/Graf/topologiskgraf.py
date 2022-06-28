import graphviz

def buildgraph1(lines):
    V = set()   #Noder
    E = set()   #Kanter

    for line in lines:
        course, *dependencies = line.strip().split()
        V.add(course)
        for dep in deps:
            E.add((dep, course))
    return V, E

class Vertex:
    def __init__(self,elem):
        self.elem = elem
        self.ni = set()
        self.tuo = set()

def buildgraph(lines):
    graph = dict()

    for line in lines:
        course = line.strip().split()[0]
        graph[course] = Vertex(course)

    for line in lines:
        course, *deps = line.strip().split()
        v = graph(course)
        graph[course] = v
        for dep in deps:
            if dep not in graph:
                continue
            w = graph[dep]
            v.ni.add(w)
            w.tuo.add(v)
    return graph

def topsort(graph):
    V = graph.values()
    stack = []
    result = []

    for v in V:
        if len(v.ni) == 0:
            stack.append(v)

    while len(stack) > 0:
        v = stack.pop()
        result.append(v.elem)
        for w in v.tuo:
            w.ni.discard(v)
            if len(w.ni) == 0:
                stack.append(w)
    return result
 
# def drawgraph(G):
   # dot = graphviz.Digraph()
    # dot.edges(E)
    # dot.render('g')

with open('graph', 'r') as f:
    lines = f.readlines()
    graph = buildgraph(lines)
    print(topsort(graph))