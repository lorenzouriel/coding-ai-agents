import logging
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from src.config import settings
from src.crew import create_crew

# -----------------------------------------------------------------------------
# Logging setup
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("crewai-brindes")

# -----------------------------------------------------------------------------
# FastAPI initialization
# -----------------------------------------------------------------------------
app = FastAPI(
    title="CrewAI Brindes Chatbot",
    version="1.0.0",
    description="CrewAI-based assistant to handle brinde catalog and pricing inquiries."
)

crew = create_crew()

# -----------------------------------------------------------------------------
# Pydantic model
# -----------------------------------------------------------------------------
class IncomingMessage(BaseModel):
    sender: str
    text: str
    channel: str = "whatsapp"


# -----------------------------------------------------------------------------
# Webhook endpoint
# -----------------------------------------------------------------------------
@app.post("/webhook")
async def webhook(msg: IncomingMessage):
    logger.info(f"📩 Incoming message: {msg.sender} -> {msg.text}")

    try:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, crew.kickoff, msg.text)
        logger.info(f"✅ CrewAI result: {result}")
        return {"ok": True, "result": result}
    except Exception as e:
        logger.exception("❌ Error processing task")
        return {"ok": False, "error": str(e)}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings.ENV,
        "model": settings.MODEL_NAME,
    }


@app.on_event("startup")
async def startup_event():
    logger.info("🚀 CrewAI Brindes API starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 CrewAI Brindes API shutting down...")
