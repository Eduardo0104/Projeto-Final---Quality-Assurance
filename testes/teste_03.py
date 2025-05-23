# Teste 03 - Verificação de erro 404 ao buscar usuário inexistente
# Objetivo: Testar se a API retorna erro 404 quando um ID de usuário inválido é consultado

import requests

def test_usuario_inexistente():
    url = "https://reqres.in/api/users/9999"  # ID inexistente
    resposta = requests.get(url)

    # Esperamos que a resposta tenha o código 404
    assert resposta.status_code == 404, f"Status esperado: 404, recebido: {resposta.status_code}"

if __name__ == "__main__":
    test_usuario_inexistente()
    print("✅ Teste 03 executado com sucesso")
