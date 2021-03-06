"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        visited_vertices = list()

        while q.size() > 0:
            current_vertex = q.dequeue()
            if current_vertex not in visited_vertices:
                print(current_vertex)
                visited_vertices.append(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    q.enqueue(next_vertex)
                
        return visited_vertices

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited_vertices = list()

        while s.size() > 0:
            current_vertex = s.pop()
            if current_vertex not in visited_vertices:
                print(current_vertex)
                visited_vertices.append(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    s.push(next_vertex)

        return visited_vertices

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)

        visited_vertices = list()

        # while s.size() > 0:
        #     current_vertex = s.pop()
        #     if current_vertex not in visited_vertices:
        #         visited_vertices.append(current_vertex)
        #         for next_vertex in self.vertices[current_vertex]:
        #             s.push(next_vertex)

        def recurse(vertex, stack, visited):
            if stack.size() > 0:
                current_vertex = stack.pop()
                if current_vertex not in visited:
                    print(current_vertex)
                    visited.append(current_vertex)
                    for next_vertex in self.vertices[current_vertex]:
                        stack.push(next_vertex)
                recurse(vertex, stack, visited)
            else:
                return -1

        recurse(starting_vertex, s, visited_vertices)

        return visited_vertices


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last_vertex = path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return path
                else:
                    visited.add(last_vertex)
                    for next_vertex in self.vertices[last_vertex]:
                        new_path = [*path, next_vertex]
                        q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            last_vertex = path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return path
                else:
                    visited.add(last_vertex)
                    for next_vertex in self.vertices[last_vertex]:
                        new_path = [*path, next_vertex]
                        s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        # while s.size() > 0:
        #     path = s.pop()
        #     last_vertex = path[-1]
        #     if last_vertex not in visited:
        #         if last_vertex == destination_vertex:
        #             return path
        #         else:
        #             visited.add(last_vertex)
        #             for next_vertex in self.vertices[last_vertex]:
        #                 new_path = [*path, next_vertex]
        #                 s.push(new_path)

        def recurse(start, end, stack, visited):
            if stack.size() > 0:
                path = stack.pop()
                last_vertex = path[-1]
                if last_vertex not in visited:
                    if last_vertex == end:
                        return path
                    else: 
                        visited.add(last_vertex)
                        for next_vertex in self.vertices[last_vertex]:
                            new_path = [*path, next_vertex]
                            stack.push(new_path)
                        return recurse(start, end, stack, visited)
                else:
                    return -1
        
        return recurse(starting_vertex, destination_vertex, s, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(graph.dft(1))
    # print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
