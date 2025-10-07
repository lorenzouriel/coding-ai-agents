from crewai import Agent

class CatalogAgent(Agent):
    def __init__(self, name="catalog-agent", tools=None):
        super().__init__(
            name=name,
            role="catalog-expert",
            goal="Provide information about available products",
            backstory="This agent is responsible for searching the catalog and providing product details to users."
        )
        self.tools = tools or []

    def run(self, query: str):
        if not self.tools:
            return "Catalog not available"
        return self.tools[0].search_catalog(query)
