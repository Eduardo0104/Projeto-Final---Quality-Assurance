# Teste 02 - Verificação do nome de usuário retornado pela API
# Objetivo: Verificar se o nome do usuário de ID 2 é "Janet"

import requests

def test_nome_usuario():
    url = "https://reqres.in/api/users/2"
    resposta = requests.get(url)
    dados = resposta.json()

    nome = dados["data"]["first_name"]

    # Esperamos que o nome seja "Janet"
    assert nome == "Janet", f"Nome esperado: Janet, recebido: {nome}"

if __name__ == "__main__":
    test_nome_usuario()
    print("✅ Teste 02 executado com sucesso")
