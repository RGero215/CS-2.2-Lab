#!python

from graph import Graph, Vertex
import unittest

class VertexTest(unittest.TestCase):

    def test_init(self):
        id = 'Ramon Geronimo'
        vertex = Vertex(id)
        assert vertex.id == id
        self.assertDictEqual(vertex.neighbors, {})

    def test_add_neighbor(self):
        jessie = Vertex('Jessie Pichardo')
        joel =  Vertex('Joel Pichardo')
        jessie.add_neighbor(joel)

        self.assertDictEqual(jessie.neighbors, {joel: 1})
        self.assertDictEqual(joel.neighbors, {})

        ramon = Vertex('Ramon Geronimo')
        jessie.add_neighbor(ramon, 5)
        self.assertDictEqual(jessie.neighbors, {joel: 1, ramon: 5})
        with self.assertRaises(KeyError):
            jessie.add_neighbor(joel)

        ramon.add_neighbor(jessie)
        self.assertDictEqual(ramon.neighbors, {jessie: 1})

    def test_get_neighbors(self):
        ramon = Vertex('Ramon Geronimo')
        jessie = Vertex('Jessie Pichardo')
        joel = Vertex('Joel Pichardo')

        ramon.add_neighbor(jessie)
        ramon.add_neighbor(joel)

        self.assertCountEqual(ramon.get_neighbors(), [jessie, joel])
        self.assertCountEqual(jessie.get_neighbors(), [])

    def test_get_id(self):
        ramon = Vertex('Ramon Geronimo')
        jessie = Vertex('Jessie Pichardo')
        joel = Vertex('Joel Pichardo')

        assert ramon.get_id() == 'Ramon Geronimo'
        assert jessie.get_id() == 'Jessie Pichardo'
        assert joel.get_id() == 'Joel Pichardo'

    def test_get_edge_weight(self):
        ramon = Vertex('Ramon Geronimo')
        jessie = Vertex('Jessie Pichardo')
        joel = Vertex('Joel Pichardo')

        ramon.add_neighbor(jessie, 10)
        ramon.add_neighbor(joel, 5)
        assert ramon.get_edge_weight(jessie) == 10
        assert ramon.get_edge_weight(joel) == 5

class GraphTest(unittest.TestCase):
    def test_init(self):
        graph = Graph()
        self.assertDictEqual(graph.vertex_list, {})
        assert graph.num_vertices == 0

    def test_num_vertices(self):
        graph = Graph()

        graph.add_vertex('Ramon Geronimo')
        graph.add_vertex('Jessie Pichardo')
        graph.add_vertex('Joel Pichardo')

        assert graph.num_vertices == 3

        graph.add_edge('Ramon Geronimo', 'Juan Geronimo')
        assert graph.num_vertices == 4
        graph.add_edge('Eduardo Geronimo', 'Fran Geronimo')
        assert graph.num_vertices == 6

        with self.assertRaises(KeyError):
            graph.add_vertex('Joel Pichardo')

    def test_add_vertex(self):
        graph = Graph()

        ramon = graph.add_vertex('Ramon Geronimo')
        jessie = graph.add_vertex('Jessie Pichardo')
        joel = graph.add_vertex('Joel Pichardo')

        assert graph.num_vertices == 3
        assert graph.get_vertex('Ramon Geronimo') == ramon
        assert graph.get_vertex('Jessie Pichardo') == jessie
        assert graph.get_vertex('Joel Pichardo') == joel

        with self.assertRaises(KeyError):
            graph.add_vertex('Joel Pichardo')

    def test_get_vertex(self):
        graph = Graph()

        ramon = graph.add_vertex('Ramon Geronimo')
        jessie = graph.add_vertex('Jessie Pichardo')
        joel = graph.add_vertex('Joel Pichardo')

        assert graph.get_vertex('Jessie Pichardo') == jessie
        with self.assertRaises(KeyError):
            graph.add_vertex('Joel Pichardo')

    def test_add_edge(self):
        graph = Graph()

        ramon = graph.add_vertex('Ramon Geronimo')
        jessie = graph.add_vertex('Jessie Pichardo')
        joel = graph.add_vertex('Joel Pichardo')

        graph.add_edge('Ramon Geronimo', 'Juan Geronimo')
        graph.add_edge('Eduardo Geronimo', 'Fran Geronimo')
        graph.add_edge('Ramon Geronimo', 'Jessie Pichardo')
        graph.add_edge('Jessie Pichardo', 'Joel Pichardo')
        juan = graph.get_vertex('Juan Geronimo')
        
        assert graph.num_vertices == 6
        
        self.assertCountEqual(jessie.get_neighbors(), [joel])
        self.assertCountEqual(joel.get_neighbors(), [])
        self.assertCountEqual(ramon.get_neighbors(), [juan, jessie])
        self.assertCountEqual(juan.get_neighbors(), [])
        self.assertCountEqual(jessie.get_neighbors(), [joel])

        assert ramon.get_edge_weight(jessie) == 1
        assert jessie.get_edge_weight(joel) == 1
        
        fran = graph.get_vertex('Fran Geronimo')
        graph.add_edge(ramon.id, 'Fran Geronimo', 10)

        assert ramon.get_edge_weight(fran) == 10

    def test_get_vertices(self):
        graph = Graph()

        ramon = graph.add_vertex('Ramon Geronimo')
        jessie = graph.add_vertex('Jessie Pichardo')
        joel = graph.add_vertex('Joel Pichardo')

        graph.add_edge('Ramon Geronimo', 'Juan Geronimo')
        graph.add_edge('Eduardo Geronimo', 'Fran Geronimo')
        graph.add_edge('Ramon Geronimo', 'Jessie Pichardo')
        graph.add_edge('Jessie Pichardo', 'Joel Pichardo')
        juan = graph.get_vertex('Juan Geronimo')
        fran = graph.get_vertex('Fran Geronimo')
        eduardo = graph.get_vertex('Eduardo Geronimo')

        self.assertCountEqual(graph.get_vertices(), [ramon, jessie, joel, juan, eduardo, fran])

    def test_breadth_first_search(self):
        graph = Graph()

        ramon = graph.add_vertex('Ramon Geronimo')
        jessie = graph.add_vertex('Jessie Pichardo')
        joel = graph.add_vertex('Joel Pichardo')

        graph.add_edge('Ramon Geronimo', 'Juan Geronimo')
        graph.add_edge('Eduardo Geronimo', 'Fran Geronimo')
        graph.add_edge('Ramon Geronimo', 'Jessie Pichardo')
        graph.add_edge('Jessie Pichardo', 'Joel Pichardo')
        juan = graph.get_vertex('Juan Geronimo')
        fran = graph.get_vertex('Fran Geronimo')
        eduardo = graph.get_vertex('Eduardo Geronimo')

        mariela = graph.add_vertex('Mariela Caceres')
        elizabeth = graph.add_vertex('Elizabeth Geronimo')
        junior = graph.add_vertex('Junior Dominguez')

        graph.add_edge(juan.id, mariela.id)
        graph.add_edge(juan.id, elizabeth.id)
        graph.add_edge(ramon.id, junior.id)
        graph.add_edge('Danesky Orlandini', 'Jeffrey Orlandini')
        danesky = graph.get_vertex('Danesky Orlandini')
        jeffrey = graph.get_vertex('Jeffrey Orlandini')
        graph.add_edge(jeffrey.id, danesky.id)
        graph.add_edge(fran.id, danesky.id)
        graph.add_edge(fran.id, jeffrey.id)
        graph.add_edge(junior.id, jeffrey.id)
        graph.add_edge(danesky.id, eduardo.id)

        level_1 = graph.breadth_first_search(ramon, 1, new=False)
        self.assertCountEqual(level_1, [juan, jessie, junior])
        level_2 = graph.breadth_first_search(ramon, 2, new=False)
        self.assertCountEqual(level_2, [jeffrey, elizabeth, mariela, joel])
        level_3 = graph.breadth_first_search(ramon, 3, new=False)
        self.assertCountEqual(level_3, [danesky])

        new_level_1 = graph.breadth_first_search(ramon, 1)
        self.assertCountEqual(new_level_1, [juan, jessie, junior])
        new_level_2 = graph.breadth_first_search(ramon, 2)
        self.assertCountEqual(new_level_2, [jeffrey, elizabeth, mariela, joel])
        new_level_3 = graph.breadth_first_search(ramon, 3)
        self.assertCountEqual(new_level_3, [danesky])

    
    def test_find_shortest_path(self):
        graph = Graph()
        # graph_file = 'graph_data.txt'
        # graph.read_graph_from_file(graph_file)

        ramon = graph.add_vertex('Ramon Geronimo')
        jessie = graph.add_vertex('Jessie Pichardo')
        joel = graph.add_vertex('Joel Pichardo')

        graph.add_edge('Ramon Geronimo', 'Juan Geronimo')
        graph.add_edge('Eduardo Geronimo', 'Fran Geronimo')
        graph.add_edge('Ramon Geronimo', 'Jessie Pichardo')
        graph.add_edge('Jessie Pichardo', 'Joel Pichardo')
        juan = graph.get_vertex('Juan Geronimo')
        fran = graph.get_vertex('Fran Geronimo')
        eduardo = graph.get_vertex('Eduardo Geronimo')

        mariela = graph.add_vertex('Mariela Caceres')
        elizabeth = graph.add_vertex('Elizabeth Geronimo')
        junior = graph.add_vertex('Junior Dominguez')

        graph.add_edge(juan.id, mariela.id)
        graph.add_edge(juan.id, elizabeth.id)
        graph.add_edge(ramon.id, junior.id)
        graph.add_edge('Danesky Orlandini', 'Jeffrey Orlandini')
        danesky = graph.get_vertex('Danesky Orlandini')
        jeffrey = graph.get_vertex('Jeffrey Orlandini')
        graph.add_edge(jeffrey.id, danesky.id)
        graph.add_edge(fran.id, danesky.id)
        graph.add_edge(fran.id, jeffrey.id)
        graph.add_edge(junior.id, jeffrey.id)
        graph.add_edge(danesky.id, eduardo.id)

        path_2 = graph.find_shortest_path('Ramon Geronimo', 'Jeffrey Orlandini')
        self.assertEqual(path_2, [ramon, junior, jeffrey]) 
        path_3 = graph.find_shortest_path('Ramon Geronimo', 'Danesky Orlandini')
        self.assertEqual(path_3, [ramon, junior, jeffrey, danesky])

    def test_find_maximal_clique(self):
        graph = Graph()
        graph_file = 'graph_data.txt'
        graph.read_graph_from_file(graph_file)
        possible = []
        # runs 100 time clique and appends to possible clique
        for _ in range(100):
            clique = graph.find_maximal_clique()
            possible.append(clique)
        
        juan = graph.get_vertex('Juan Geronimo')
        jessie = graph.get_vertex('Jessie Pichardo')
        mariela = graph.get_vertex('Mariela Caceres')
        group = set([juan, mariela, jessie])
        # check if group is in the possible solution
        self.assertTrue(group in possible)


if __name__ == "__main__":
    unittest.main()