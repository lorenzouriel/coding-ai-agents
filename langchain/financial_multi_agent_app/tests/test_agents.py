from src.agents.research import generate_portfolio, SAMPLE_ASSETS
from pathlib import Path

def test_generate_portfolio(tmp_path: Path):
    out = tmp_path / "sample.json"
    path = generate_portfolio(SAMPLE_ASSETS, out_path=out)
    assert path.exists()
    data = path.read_text()
    assert "symbol" in data