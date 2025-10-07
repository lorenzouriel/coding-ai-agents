# Gifts Attedant

### `.env`
```python
OPENAI_API_KEY=sk-yourkey
ENV=development
MODEL_NAME=gpt-4o-mini
LOG_LEVEL=INFO
CATALOG_INDEX=data/catalog.csv
PRICING_RULES_JSON=data/pricing_rules.json
```

### Run it locally
```python
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the API
uvicorn src.main:app --reload --port 8000

# 3. Test it
curl -X POST http://localhost:8000/webhook \
     -H "Content-Type: application/json" \
     -d '{"sender": "user1", "text": "I want a pen", "channel": "whatsapp"}'
```

