from pathlib import Path
from typing import Any

def write_text(directory: Path, filename: str, content: str) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / filename
    with path.open("w", encoding="utf-8") as f:
        f.write(content)
    return path

def read_json(path: Path):
    import json
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)