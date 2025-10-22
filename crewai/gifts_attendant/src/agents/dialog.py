from crewai import Agent

class DialogAgent(Agent):
    def __init__(self, name="dialog-agent"):
        super().__init__(
            name=name,
            role="dialog-manager",
            goal="Handle customer messages and delegate tasks",
            backstory="This agent is responsible for understanding user messages and delegating them to the proper assistant (catalog, pricing, etc)."
        )

    def handle_message(self, message: str) -> str:
        if "price" in message.lower():
            return "pricing"
        elif "catalog" in message.lower():
            return "catalog"
        else:
            return "general"
