class Vertex: #✔
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def __str__(self):
        return f"Vertex {self.name} with neighbours {self.neighbours}."

    def add_neighbour(self, neighbour):
        if isinstance(neighbour, Vertex):
            self.neighbours.append(neighbour.name)
            neighbour.neighbours.append(self.name)

class Graph: #✔
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
        if vertex_name1 == vertex_name2:
            return
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



class Bipartite_Graph(Graph): #✔
    def __init__(self):
        super().__init__()
        self.partition_A = []
        self.partition_B = []

    def __str__(self): #✔
        num_partition_A = len(self.partition_A)
        num_partition_B = len(self.partition_B)     
        return f"Bipartite graph with {num_partition_A} vertices in A, {num_partition_B} vertices in B and {self.num_edges} edges."

    def add_vertices(self, vertex_names, partition = None): #✔
        for name in vertex_names:
            if partition == 'A':
                if name not in self.partition_A:
                    self.partition_A.append(name)                   
            elif partition == 'B':
                if name not in self.partition_B:
                    self.partition_B.append(name)
        super().add_vertices(vertex_names)

    def add_edge(self, vertex_nameA, vertex_nameB):
        if vertex_nameA not in self.partition_A and vertex_nameA not in self.partition_B:
            self.partition_A.append(vertex_nameA)
        if vertex_nameB not in self.partition_B and vertex_nameB not in self.partition_A:
            self.partition_B.append(vertex_nameB)
        self.add_vertices([vertex_nameA])
        self.add_vertices([vertex_nameB])

        if vertex_nameA in self.partition_B or vertex_nameB in self.partition_A:                   
            return #if its the case then it will return nothing

        super().add_edge(vertex_nameA, vertex_nameB)

"""
B = Bipartite_Graph()
B.add_vertices(['a0', 'a1', 'a2', 'a3', 'a4'],"A")
B.add_vertices(['b0', 'b1', 'b2', 'b3', 'b4', 'b5'],"B")
B.add_edge("a4","b5")
B.add_edge("a3","b4")
B.add_edge("a2","b3")
B.add_edge("a3","a3")
B.add_edge("a0","a1")
print(B)
#Erwarteter Output: Bipartite graph with 5 vertices in A, 6 vertices in B and 3 edges.
for i in B: print(i)
#Vertex a0 with neighbours [].
#Vertex a1 with neighbours [].
#Vertex a2 with neighbours ['b3'].
#Vertex a3 with neighbours ['b4'].
#Vertex a4 with neighbours ['b5'].
#Vertex b0 with neighbours [].
#Vertex b1 with neighbours [].
#Vertex b2 with neighbours [].
#Vertex b3 with neighbours ['a2'].
#Vertex b4 with neighbours ['a3'].
#Vertex b5 with neighbours ['a4'].
print(B.get_max_degree())
#1


B = Bipartite_Graph()
B.add_vertices(['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'],"A")
B.add_edge("a4","b3")
B.add_edge("a6","b0")
B.add_edge("a1","b0")
B.add_edge("a2","b0")
B.add_edge("a5","b0")
B.add_edge("a2","b2")
B.add_edge("a6","b3")
B.add_edge("a1","b2")
B.add_edge("a5","b5")
B.add_edge("a6","b5")
print(B)
#Bipartite graph with 7 vertices in A, 4 vertices in B and 10 edges.
for i in B: print(i)
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
B.get_max_degree()
#4
"""