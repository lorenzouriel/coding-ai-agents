from crewai import CrewStructuredTool

class PricingTool(CrewStructuredTool):
    name = "pricing-tool"
    description = "Calculate pricing"

    def run(self, product_name: str):
        # implement pricing logic
        return f"Price for {product_name} is $X"
