from typing import Annotated
from langchain_core.tools import tool
from pathlib import Path
from src.config import OUTPUTS_DIR
from src.utils.file_ops import write_text

@tool
def write_document(content: Annotated[str, "Text content to be written into the document."], file_name: Annotated[str, "File name"] = "Portfolio_Optimization.txt") -> str:
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    path = write_text(OUTPUTS_DIR, file_name, content)
    return f"Document saved to {path}"