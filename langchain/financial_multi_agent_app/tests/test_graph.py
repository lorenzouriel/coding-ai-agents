# Basic smoke test for building the graph
from src.graph.pipeline import build_graph

def test_build_graph():
    graph = build_graph()
    assert graph is not None