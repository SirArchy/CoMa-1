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
    def __init__(self, vertices_A, vertices_B):
        super().__init__()
        self.vertices_A = vertices_A
        self.vertices_B = vertices_B

    def __str__(self):
        num_vertices_A = len(self.vertices_A)
        num_vertices_B = len(self.vertices_B)
        num_edges = super().get_num_edges()
        return f"Bipartite graph with {num_vertices_A} vertices in A, {num_vertices_B} vertices in B and {num_edges} edges."

    def add_vertices(self, vertex_names, partition):
        for name in vertex_names:
            if name in self.vertices_A or name in self.vertices_B:
                continue # skip if vertex already exists
            vertex = Vertex(name)
            self.vertices[name] = vertex
            if partition == "A":
                self.vertices_A.append(name)
            elif partition == "B":
                self.vertices_B.append(name)

    def add_edge(self, vertex_nameA, vertex_nameB):
        if vertex_nameA in self.vertices_B or vertex_nameB in self.vertices_A:
            return # skip if vertices not in correct partition
        super().add_edge(vertex_nameA, vertex_nameB)

u = Vertex('u')
v = Vertex('v')
w = Vertex('w')
u.add_neighbour(v)
u.add_neighbour(w)
print(u)
#Vertex u with neighbours ['v', 'w']
print(v)
#Vertex v with neighbours []

"""
G = Graph()
G.add_vertices(['u','v','w'])
G.add_edge('u','v')
G.add_edge('u','w')
print(G)
#Graph with 3 vertices and 2 edges.
for i in G:
    print(i)
#Vertex u with neighbours ['v', 'w'].
#Vertex v with neighbours ['u'].
#Vertex w with neighbours ['u'].
print(G.get_max_degree())
#2


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
print(B.get_max_degree())
#2
"""