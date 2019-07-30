from graph import Graph
import sys

def graph_path_data(path):
    '''Prints the data of the graph'''
    print(path)
    for index in range(len(path)):
        path[index] = path[index].id

    print(f'Vertices in shortest path: {path}')
    print(f'Number of edges in shortest path: {len(path) - 1}')

def main():
    '''Run path from graph file name'''
    # if len(sys.argv) < 4:
    #     raise RuntimeError('Expecting file name, start vertex and end vertex')
    graph_file = sys.argv[1]
    start_vertex = str(sys.argv[2])
    end_vertex = str(sys.argv[3])

    graph = Graph()
    graph.read_graph_from_file(graph_file)
    print("Graph Vertices: \n", graph.get_vertices())
    print('\n===========================================\n')

    print("Graph edges: \n", graph.get_edge_list())
    print('\n===========================================\n')
    
    vertex = graph.get_vertex(start_vertex)
    print(f"Neighbors of {start_vertex}: \n", vertex.get_neighbors())
    print('\n===========================================\n')
    
    print(f'Shortest Path from {start_vertex} to {end_vertex}')
    shortest_path = graph.find_shortest_path(start_vertex, end_vertex)
    graph_path_data(shortest_path)
    print('\n===========================================\n')

    print('Find Maximal Clique', graph.find_maximal_clique())
    print('\n===========================================\n')
    
    # print(graph.depth_first_search(1, 5))

if __name__ == "__main__":
    main()