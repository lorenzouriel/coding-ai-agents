from crewai import Agent

class PricingAgent(Agent):
    def __init__(self, name="pricing-agent", tools=None):
        super().__init__(
            name=name,
            role="pricing-specialist",
            goal="Calculate and return price quotations",
            backstory="This agent calculates pricing for requested products based on rules or existing price lists."
        )
        self.tools = tools or []

    def run(self, query: str):
        if not self.tools:
            return "Pricing not available"
        return self.tools[0].get_price(query)
