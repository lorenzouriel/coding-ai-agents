from crewai import Crew, Agent
from src.agents.dialog import DialogAgent
from src.agents.catalog import CatalogAgent
from src.agents.pricing import PricingAgent
from src.tools.catalog_tool import CatalogQueryTool
from src.tools.pricing_tool import PricingTool
from src.config import settings

def create_crew() -> Crew:
    catalog_tool = CatalogQueryTool(catalog_path=settings.CATALOG_INDEX)
    pricing_tool = PricingTool(pricing_rules_path=settings.PRICING_RULES_JSON)

    dialog_agent = DialogAgent(name="dialog-agent")
    catalog_agent = CatalogAgent(name="catalog-agent", tools=[catalog_tool])
    pricing_agent = PricingAgent(name="pricing-agent", tools=[pricing_tool])

    crew = Crew(
        agents=[dialog_agent, catalog_agent, pricing_agent],
        verbose=settings.DEBUG
    )
    return crew
