from crewai import CrewStructuredTool

class CatalogQueryTool(CrewStructuredTool):
    name = "catalog-tool"
    description = "Query products from catalog"

    def run(self, query: str):
        # implement catalog lookup
        return f"Catalog lookup result for: {query}"
