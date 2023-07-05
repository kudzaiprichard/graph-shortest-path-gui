import math
import graph

class Bellman_ford:
    def __init__(self, G, w, start_vertex, end_vertex):
        '''
            Constructor Inputs:
            [G]: graph.Graph object of graph representation
            [w]: weight mapping of edges
            [start_vertex]: the beginning source to which shortest paths will be computed
                            its a graph.Vertex instance of G.
            [end_vertex]:   the end source to which shortest paths will be computed
                            its a graph.Vertex instance of G.
        '''
        
        #mapping of vertices to the length of the shortest path with start_vertex as source i.e. = d(start_vertex, v)
        self.distance_est = {vertex: math.inf for vertex in G.vertices()}
        #mapping of vertices to their predecessor in the shortest path tree with root start_vertex
        self.spt_predecessor = {vertex: None for vertex in G.vertices()}
        
        self.distance_est[start_vertex] = 0
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.n = G.vertex_count()
        self.G = G
        self.w = w

    def execute(self):
        '''
        Function for computing the shortest path 
        '''

        #looping through the count of total number of vertex
        for i in range(1, self.n):
            #looping through the count of total number of edge
            for edge in self.G.edges():
                source, destination = edge.endPoints()
                # edge relaxation
                if self.distance_est[destination] > self.distance_est[source] + self.w[edge]:
                    self.distance_est[destination] = self.distance_est[source] + self.w[edge]
                    self.spt_predecessor[destination] = source

        #looping through the count of total number of edge
        for edge in self.G.edges():
            source, destination = edge.endPoints()
            if self.distance_est[destination] > self.distance_est[source] + self.w[edge]:
                return None, None
    
    def get_results(self):
        '''
        For printing the result(s)
        '''
        #Gets shortest path from start vertex to all other vertex
        for key in self.spt_predecessor:
            #filters and displays the results of the specified end vertex
            if(key.element() == self.end_vertex.element()):  
                if self.start_vertex.element() == key.element():
                    x = key.element() + ' is the start vertex'
                    y = ""
                    return x, y
                else:
                    path = [key]
                    vertex = self.spt_predecessor[key]
                    while not (vertex is None):
                        path.insert(0, vertex)
                        vertex = self.spt_predecessor[vertex]
                    elements = [vertex.element() for vertex in path]
                    y = 'Shortest path from ' + self.start_vertex.element() + ' to ' + key.element() + ' with value: ' + str(self.distance_est[key])+ ' km '
                    x = '->'.join(elements)
                    return x, y
