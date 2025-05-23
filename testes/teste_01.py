# Teste 01 - Verificação de status da API ReqRes
# Objetivo: Confirmar que o endpoint básico da API está respondendo corretamente

import requests

def test_status_code():
    url = "https://reqres.in/api/users"
    resposta = requests.get(url)

    # Esperamos que a resposta tenha o código HTTP 200
    assert resposta.status_code == 200, f"Status esperado: 200, recebido: {resposta.status_code}"

# Execução do teste (somente se o arquivo for executado diretamente)
if __name__ == "__main__":
    test_status_code()
    print("✅ Teste 01 executado com sucesso")
