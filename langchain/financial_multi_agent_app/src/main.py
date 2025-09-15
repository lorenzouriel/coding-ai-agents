from .graph.pipeline import build_graph, run_graph
from .agents.research import generate_portfolio, SAMPLE_ASSETS

def main():
    generate_portfolio(SAMPLE_ASSETS)

    graph = build_graph()
    run_graph(graph, "Generate a well structured report on how to improve my portfolio given the market landscape in Q4 2025.")

if __name__ == "__main__":
    main()