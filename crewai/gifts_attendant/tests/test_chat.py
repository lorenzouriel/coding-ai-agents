import requests

def test_webhook():
    msg = {
        "sender": "test_user",
        "text": "Show me the catalog of mugs",
        "channel": "web"
    }
    r = requests.post("http://localhost:8000/webhook", json=msg)
    print(r.json())

if __name__ == "__main__":
    test_webhook()
