from nose import with_setup
from nose.tools import nottest, raises
from dag import DAG


@nottest
def blank_setup():
    global dag
    dag = DAG()


@nottest
@with_setup(blank_setup)
def start_with_graph():
    dag.from_dict({
        'a':['b','c'],
        'b':['d'],
        'c':['d'],
        'e':['d'],
        'd':[]})


@with_setup(blank_setup)
def test_add_node():
    dag.add_node('a')
    dag.add_node('b')
    assert dag.graph == {'a': set(), 'b': set()}


@with_setup(blank_setup)
def test_add_edge():
    dag.add_node('a')
    dag.add_node('b')
    dag.add_edge('a','b')
    assert dag.graph == {'a': set('b'), 'b': set()}


@with_setup(blank_setup)
def test_from_dict():
    dag.from_dict({
        'a':['b','c'],
        'b':['d'],
        'c':['d'],
        'd':[]})
    assert dag.graph == {'a': set(['b','c']), 'b': set('d'), 'c': set('d'), 'd': set()}


@with_setup(blank_setup)
def test_reset_graph():
    test_from_dict()
    dag.reset_graph()
    assert dag.graph == {}


@with_setup(start_with_graph)
def test_ind_nodes():
    assert dag.ind_nodes(dag.graph) == ['a','e']


