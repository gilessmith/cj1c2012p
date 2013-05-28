import codejam.utils.codejamrunner as cjr
import itertools
import networkx as nx

class Dynam(object):pass


def find_root_classes(graph):
    return [n for n in graph.nodes() if not graph.predecessors(n)]

    
def solve(data):

    root_classes = find_root_classes(data.g)
    #import pdb;pdb.set_trace()
    for root in root_classes:
        existing_nodes = set([])
        nodes_to_search = data.g.successors(root)
        while nodes_to_search:
            n = nodes_to_search.pop()
            if n in existing_nodes:
                return 'Yes'
            existing_nodes.add(n)
            nodes_to_search += data.g.successors(n)

    return 'No'

def builder(f):
    data = Dynam()
    data.class_count = f.get_int()
    data.g = nx.DiGraph()
    data.g.add_nodes_from(range(1, data.class_count + 1))
    data.edges = 0

    for node in data.g.nodes():
        edges = f.get_ints()[1:]
        data.edges += len(edges)
        for edge_target in edges:
            data.g.add_edge(node, edge_target)
         
    return data

    



cjr = cjr.CodeJamRunner()
cjr.run(builder, solve, problem_name = "A", problem_size='large-practice')
