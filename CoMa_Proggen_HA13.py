class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def __str__(self):
        return f"Vertex {self.name} with neighbours {self.neighbours}"

    def add_neighbour(self, neighbour):
        if isinstance(neighbour, Vertex):
            self.neighbours.append(neighbour.name)
            neighbour.neighbours.append(self.name)

class Graph:
    def __init__(self):
        self.num_vertices = 0
        self.num_edges = 0
        self.vertices = {}

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        return f"Graph with {self.num_vertices} vertices and {self.num_edges} edges."

    def add_vertices(self, vertex_names):
        for name in vertex_names:
            if name not in self.vertices:
                self.vertices[name] = Vertex(name)
                self.num_vertices += 1

    def add_edge(self, vertex_name1, vertex_name2):
        if vertex_name1 not in self.vertices:
            self.add_vertices([vertex_name1])
        if vertex_name2 not in self.vertices:
            self.add_vertices([vertex_name2])

        vertex1 = self.vertices[vertex_name1]
        vertex2 = self.vertices[vertex_name2]

        if vertex1.name not in vertex2.neighbours:
            self.num_edges += 1
            vertex1.add_neighbour(vertex2)

    def get_max_degree(self):
        max_degree = 0
        for vertex in self.vertices.values():
            degree = len(vertex.neighbours)
            if degree > max_degree:
                max_degree = degree
        return max_degree



class Bipartite_Graph(Graph):
    def __init__(self):
        super().__init__()
        self.verticesA = []
        self.verticesB = []

    def __str__(self):
        num_verticesA = len(self.verticesA)
        num_verticesB = len(self.verticesB)
        num_edges = self.num_edges
        return f'Bipartite graph with {num_verticesA} vertices in A, {num_verticesB} vertices in B and {num_edges} edges.'

    def add_vertices(self, vertex_names, partition):
        for name in vertex_names:
            if name in self.vertices:
                continue
            vertex = Vertex(name)
            self.vertices[name] = vertex
            if partition == 'A':
                self.verticesA.append(name)
            elif partition == 'B':
                self.verticesB.append(name)

    def add_edge(self, vertex_nameA, vertex_nameB):
        if vertex_nameA in self.verticesB or vertex_nameB in self.verticesA:
            return
        super().add_edge(vertex_nameA, vertex_nameB)


"""   
u = Vertex('u')
v = Vertex('v')
w = Vertex('w')
u.add_neighbour(v)
u.add_neighbour(w)
print(u)
#Vertex u with neighbours ['v', 'w']
print(v)
#Vertex v with neighbours ['u']
"""

G = Graph()
G.add_vertices(['u','v','w'])
G.add_edge('u','v')
G.add_edge('u','w')
print(G)
#Graph with 3 vertices and 2 edges.
G.add_edge('u','x')
print(G)
#Graph with 3 vertices and 2 edges.
G.add_edge('x','y')
print(G)
#Graph with 3 vertices and 2 edges.
G.add_edge('z','a')
print(G)
#Graph with 3 vertices and 2 edges.

for i in G:
    print(i)
#Vertex u with neighbours ['v', 'w'].
#Vertex v with neighbours ['u'].
#Vertex w with neighbours ['u'].
G.get_max_degree()
#2

"""
B = Bipartite_Graph()
B.add_vertices(['a1','a2'],'A')
B.add_vertices(['b1'],'B')
B.add_edge('a1','b1')
B.add_edge('a2','b1')
print(B)
#Bipartite graph with 2 vertices in A, 1 vertices in B and 2 edges.
B.add_edge('a1','a2')
print(B)
#Bipartite graph with 2 vertices in A, 2 vertices in B and 2 edges.
B.add_edge('a1','a2')
print(B)
#Bipartite graph with 2 vertices in A, 2 vertices in B and 2 edges.
print(B.get_max_degree())
#2


C = Bipartite_Graph()
C.add_vertices(['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'],"A")
C.add_edge("a4","b3")
C.add_edge("a6","b0")
C.add_edge("a1","b0")
C.add_edge("a2","b0")
C.add_edge("a5","b0")
C.add_edge("a2","b2")
C.add_edge("a6","b3")
C.add_edge("a1","b2")
C.add_edge("a5","b5")
C.add_edge("a6","b5")
print(C)
# Bipartite graph with 7 vertices in A, 4 vertices in B and 10 edges.
for i in C: print(i)
#Vertex a0 with neighbours [].
#Vertex a1 with neighbours ['b0', 'b2'].
#Vertex a2 with neighbours ['b0', 'b2'].
#Vertex a3 with neighbours [].
#Vertex a4 with neighbours ['b3'].
#Vertex a5 with neighbours ['b0', 'b5'].
#Vertex a6 with neighbours ['b0', 'b3', 'b5'].
#Vertex b3 with neighbours ['a4', 'a6'].
#Vertex b0 with neighbours ['a6', 'a1', 'a2', 'a5'].
#Vertex b2 with neighbours ['a2', 'a1'].
#Vertex b5 with neighbours ['a5', 'a6'].
C.get_max_degree()
#4
"""
