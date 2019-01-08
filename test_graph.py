"""
lattice ==>
    number of nodes total
    interacte by type then collection
    concept of time?
    max number of neighbors
    number of target nodes of each node
    collection of target nodes of each node
    interact with cells directly
    collection of nodes
"""
import io
import unittest

import graph
import point

"""
/* Cell Lattice */
struct lattice_t {
    int *n_Target_Nodes[N_CELL_TYPES]; //2nd dim size: n_Nbrs_Max+1
struct node_t *** target_Nodes[N_CELL_TYPES]; //size:[4][n_Nbrs_Max+1][n_Nodes]
                                                     //[SOURCE_Type][#target neighbors][cell addy]

                                                         int n_Cells[N_CELL_TYPES]; // Number of each TYPE of Cell
struct node_t ** cells[N_CELL_TYPES]; //size: [n_Nodes];

struct node_t * first_Node;  //Head of node linked list
double  time;
int    n_Nbrs_Max;
int    n_Nodes;
char*  coord_Filename;
};

/* Cell */
   struct node_t {
    enum nodeType_t type;
int n_Nbrs[N_CELL_TYPES]; //Number of neighbors of type
struct node_t ** neighbors; //Array size: n_Nbrs_Max
int n_Neighbors;
int x;
int y;
int z;

struct node_t * next_Node; //in Linked List containing all nodes in lattice
int targets_Idx[N_CELL_TYPES]; // Locations(s) in target_Nodes (-1 == not present)
int list_Idx;         // Cell's location in cells[this.type] array -1 if empty

enum visited_t visited;
int distance;
void * predecessor;
};
"""


class TestNode(unittest.TestCase):
    def test_add_neighbor(self):
        node = graph.Vertex()
        node2 = graph.Vertex()
        node.add_neighbor(node2)

        self.assertEqual(len(node.neighbors), 1)

    def test_type_attribute(self):
        node = graph.Vertex()
        node.type = 'Normal'
        self.assertEqual(node.type, 'Normal')

    def test_point(self):
        node = graph.Vertex()
        node.point = point.Point(coords=[0, 0])

        self.assertEqual(node.point.x, 0)


class TestGraph(unittest.TestCase):
    def test_from_adjacency_list(self):
        list_string = """
                     2,  5
                1,   3,  6
                2,   4,  7
                3,       8
            1,       6,  9
            2,  5,   7, 10
            3,  6,   8, 11
            4,  7,      12
            5,      10, 13
            6,  9,  11, 14
            7,  10, 12, 15
            8,  11,     16
            9,      14,
            10, 13, 15,
            11, 14, 16,
            12, 15, 
            """

        stream = io.StringIO(list_string)
        g = graph.Graph()
        g.from_adjacency_list(stream)

        self.assertEqual(len(g), 16)
