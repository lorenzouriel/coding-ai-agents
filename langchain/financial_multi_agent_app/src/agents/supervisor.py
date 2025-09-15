from typing import Literal
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage
from langgraph.types import Command

from langgraph.graph import MessagesState

class State(MessagesState):
    next: str

def make_supervisor_node(llm, members: list[str]) -> callable:
    options = ["FINISH"] + members
    system_prompt = (
        "You are a supervisor tasked with managing a conversation between the"
        f" following workers: {members}. Given the following user request,"
        " respond with the worker to act next. Each worker will perform a"
        " task and respond with their results and status. When finished,"
        " respond with FINISH."
    )

    class Router(TypedDict):
        next: Literal[*options]

    def supervisor_node(state: State) -> Command[Literal[*members, "__end__"]]:
        messages = [
            {"role": "system", "content": system_prompt},
        ] + state["messages"]
        # Using the LLM's structured output to decide next worker
        response = llm.with_structured_output(Router).invoke(messages)
        goto = response["next"]
        if goto == "FINISH":
            from langgraph.graph import END

            goto = END

        return Command(goto=goto, update={"next": goto})

    return supervisor_node