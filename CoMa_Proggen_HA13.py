class Vertex(object): #FERTIG
    def __init__(self, name):  
        self.name = name
        self.neighbours = []
    
    def __str__(self) -> str:
        return(f'Vertex {self.name} with neighbours {self.neighbours}.')

    def add_neighbour(self, neighbour):
        if isinstance(neighbour, Vertex):
            self.neighbours.append(neighbour.name)
        return self.neighbours


class Graph(object): #UNFERTIG
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.dictionary = {Vertex.name: Vertex} # Knoten des Graphen speichern, Key ist Name des Knoten und Wert ist Objekt aus Vertex

    def __iter__(self):
        return self.dictionary.values()            

    def __str__(self) -> str:
        return str(f'Graph with {self.vertices} vertices and {self.edges} edges.')

    def add_vertices(self, vertex_names):
        #Knoten zum Graph hinzufügen
        #für jeden Eintrag in vertex_names, Vertex Objekt in self.dictionary hinzufügen
        #Knoten bereits vorhanden? Nicht hinzufügen
        
        return

    def add_edge(self, vertex_name1, vertex_name2):
        #fügt Knoten zwischen vertex_name1 und vertex_name2 hinzu
        #wenn Knoten noch nicht in Dictionary, dann hinzufügen
        return

    def get_max_degree(self):
        return max(self.dictionary.values()) #max Knotengrad zurückgeben



class Bipartite_Graph(object): #UNFERTIG
    def __init__(self):
        verticesA = []
        verticesB = []
        return verticesA, verticesB
    
    def __str__(self) -> str:
        return str(f'Bipartite Graph with {len(self.vertices)} vertices and {len(self.edges)} edges.')

    def add_vertices(self, vertex_names, partition):
        #Knoten zum Graph hinzufügen
        #partition ist entweder A oder B, sagt zu welcher Menge die Knoten gehören
        return

    def add_edge(self, vertex_nameA, vertex_nameB):
        #stellt sicher dass vertex_nameA nicht in Partition B und vertex_nameB nicht in Partition A sind
        return




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
B.get_max_degree()
#2
"""