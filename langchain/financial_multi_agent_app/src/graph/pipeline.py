from langgraph.graph import StateGraph, START
from src.graph.supervisor import make_supervisor_node
from src.agents.portfolio_reader import read_sample_portfolio
from src.agents.report_writer import write_document
from src.agents.web_search import create_tavily_tool
from src.llm import create_llm
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage


def build_graph():
    llm = create_llm()
    tavily_tool = create_tavily_tool(max_results=5)

    search_agent = create_react_agent(llm, tools=[tavily_tool])
    read_agent = create_react_agent(llm, tools=[read_sample_portfolio])
    doc_writer = create_react_agent(llm, tools=[write_document])

    supervisor_node = make_supervisor_node(llm, ["search", "read_portfolio", "doc_writer"])

    builder = StateGraph()
    builder.add_node("supervisor", supervisor_node)

    def search_node(state):
        result = search_agent.invoke(state)
        return {
            "goto": "supervisor",
            "update": {"messages": [HumanMessage(content=result["messages"][-1].content, name="search")]} ,
        }

    def read_portfolio_node(state):
        result = read_agent.invoke(state)
        return {
            "goto": "supervisor",
            "update": {"messages": [HumanMessage(content=result["messages"][-1].content, name="read_portfolio")]},
        }

    def doc_writing_node(state):
        result = doc_writer.invoke(state)
        return {
            "goto": "supervisor",
            "update": {"messages": [HumanMessage(content=result["messages"][-1].content, name="doc_writer")]},
        }

    builder.add_node("search", search_node)
    builder.add_node("read_portfolio", read_portfolio_node)
    builder.add_node("doc_writer", doc_writing_node)

    builder.add_edge(START, "supervisor")
    graph = builder.compile()
    return graph


def run_graph(graph, user_prompt: str):
    for s in graph.stream({"messages": [("user", user_prompt)]}, {"recursion_limit": 150}):
        print(s)