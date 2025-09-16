import requests

def test_ollama_api():
    url = "http://127.0.0.1:11434/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "model": "mistral",
        "messages": [
            {"role": "user", "content": "Olá, Ollama!"}
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    assert response.status_code == 200, f"Erro na API: {response.status_code}"
    result = response.json()
    print("Resposta da API:", result)

    assert "choices" in result, "Resposta inesperada"

if __name__ == "__main__":
    test_ollama_api()
