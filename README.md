# Projeto Final - Quality Assurance

## 1. Apresentação

**Nome completo:** Eduardo Siqueira Pinheiro
**Curso e semestre:** Tecnologia em Gestão da Informação – 5º semestre  

Durante essa disciplina, tive meu primeiro contato mais aprofundado com o universo de testes em software. Consegui entender, de forma prática, como os testes são essenciais para garantir a estabilidade e confiança em um sistema. Usar ferramentas como o Google Colab e o GitHub me ajudou a visualizar melhor como o QA se encaixa no ciclo de desenvolvimento.

---

## 2. O que é Quality Assurance (QA)?

Quality Assurance, ou simplesmente QA, é a prática de garantir que um sistema funcione da forma esperada, antes de chegar ao usuário final. O QA ajuda a encontrar erros e falhas, evitando que um software com defeitos seja lançado. É como revisar um trabalho antes de entregar, garantindo que esteja tudo certo e que as pessoas vão conseguir usar sem problemas.

---

## 3. Conceitos Aprendidos Durante o Semestre

Neste semestre, aprendi que qualidade em software não se resume a "funcionar" — envolve segurança, bom desempenho, facilidade de uso e confiabilidade. Conheci vários tipos de testes, como:

- **Testes unitários**, que avaliam partes isoladas do código
- **Testes de integração**, que verificam se as partes funcionam bem juntas
- **Testes de sistema e aceitação**, que simulam situações reais
- **Testes de regressão e exploratórios**, usados para garantir que tudo continue funcionando mesmo após mudanças

Também aprendemos a planejar os testes com critérios claros, desenvolver planos e escrever casos de teste.  
Utilizamos ferramentas como o Google Colab, GitHub e APIs públicas como a ReqRes para praticar.  
Descobri como a automação com Python ajuda muito no processo, inclusive podendo ser integrada a pipelines de CI/CD.  
Por fim, entendi como usar métricas, rastrear bugs e acompanhar o comportamento do sistema com observabilidade para manter a qualidade a longo prazo.

---

## 4. Ferramentas e Sites Utilizados

- https://reqres.in/  
- https://colab.research.google.com/  
- https://github.com/  
- https://uptimerobot.com/  

Outras ferramentas que usei em alguns momentos de prática:  
- https://jsonplaceholder.typicode.com/  
- https://httpbin.org/

---

## 5. Explicação dos Testes Entregues

✅ **Teste 01 – Verificação de status da API ReqRes**  
**Biblioteca:** requests  
**Objetivo:** Verificar se o endpoint retorna status HTTP 200  
**Resultado esperado:** Teste passa com sucesso se o status for 200  
**Arquivo:** testes/teste_01.py

---

✅ **Teste 02 – Verificação de nome de usuário retornado pela API**  
**Biblioteca:** requests  
**Objetivo:** Conferir se o nome retornado pela requisição é "Janet"  
**Resultado esperado:** Nome igual a "Janet"  
**Arquivo:** testes/teste_02.py

---

✅ **Teste 03 – Verificação de erro ao buscar usuário inexistente**  
**Biblioteca:** requests  
**Objetivo:** Checar se a API responde com erro 404 quando o usuário não é encontrado  
**Resultado esperado:** Código de status HTTP 404  
**Arquivo:** testes/teste_03.py

---

## 6. Conclusão Final

O que mais aprendi foi que o QA é essencial para entregar software com qualidade real, não apenas funcionando, mas também seguro, rápido e confiável. No futuro, me vejo trabalhando com automação de testes, especialmente em ambientes de integração contínua. A ferramenta que mais me chamou atenção foi o uso de **Python com requisições HTTP**, por ser muito prática e poderosa para criar testes que simulam o uso real da aplicação. A disciplina ampliou minha visão sobre o papel estratégico do QA dentro de uma equipe de tecnologia.

