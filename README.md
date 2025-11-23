## Análise de Comentários Ifood

POC (Prova de Conceito) desenvolvida para demonstrar a aplicação prática de LLMs na análise de feedback de clientes (Customer Experience).

O objetivo é automatizar a triagem de avaliações de restaurantes, gerando não apenas a classificação do sentimento, mas respostas personalizadas e insights operacionais acionáveis para o parceiro.

## A Solução

A ferramenta recebe um comentário de um cliente e utiliza Inteligência Artificial para processar três saídas simultâneas:

1.  **Análise de Sentimento:** Classificação automática (Positivo/Neutro/Negativo).
2.  **Resposta ao Cliente:** Sugestão de texto empático para o restaurante responder rápido.
3.  **Ação Sugerida:** Dica prática para a operação (ex: "verificar tempo da entrega").

## Tecnologias Utilizadas

- **Python**
- **Streamlit:** Para interface frontend rápida.
- **LangChain:** Framework de orquestração e engenharia de prompt.
- **Google Gemini (2.0 Flash):**

Estrutura do Prompt
O projeto utiliza PromptTemplates do LangChain para garantir que o modelo atue com a persona de um especialista em CX do iFood. A estrutura força uma saída organizada, evitando alucinações e mantendo o tom de voz da marca.

## Como rodar o projeto

### Pré-requisitos

- Ter o [uv](https://github.com/astral-sh/uv) instalado.
- Uma API Key do Google AI Studio (Gemini).

### Passo a passo

1. Clone este repositório:
   bash
   git clone [https://github.com/nicholascrispimsilva/Analise-Comentarios-Ifood.git](https://github.com/nicholascrispimsilva/Analise-Comentarios-Ifood.git)
   cd ifood-review-insight

2. Sincronize as dependências (o uv criará o ambiente virtual automaticamente):
   bash
   uv sync

3. Execute a aplicação:
   bash
   uv run streamlit run app.py

4. Insira sua chave de API na barra lateral da aplicação.

Projeto desenvolvido como parte do processo seletivo para o Estágio em GenIA do iFood.
