import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# 1. Configuração da Página
st.set_page_config(page_title="iFood Review Insight (Gemini Edition)", page_icon="🚀")

st.title("🚀 iFood Review Insight")
st.write("Transformando feedback de clientes em ação estratégica para restaurantes.")

# 2. Captura da Chave de API (Sidebar)
api_key = st.sidebar.text_input("Cole sua Google API Key aqui:", type="password")

# 3. Entrada de Dados
review_text = st.text_area(
    "Cole o comentário do cliente:",
    height=150,
    placeholder="Ex: Gostei do lanche mas demorou para chegar.",
)

# 4. Botão de Ação
if st.button("Analisar com Gemini"):
    if not api_key:
        st.warning("⚠️ Por favor, insira sua chave de API do Google na barra lateral.")
        st.stop()

    if not review_text:
        st.warning("⚠️ Por favor, escreva um comentário para analisar.")
        st.stop()

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash", google_api_key=api_key, temperature=0.7
        )

        template = """
        Você é um especialista em Customer Experience (CX) do iFood.
        Analise o seguinte review de um cliente:
        
        "{review}"
        
        Gere uma saída estruturada contendo:
        1. **Sentimento:** (Positivo, Negativo ou Neutro)
        2. **Sugestão de Resposta:** Uma resposta empática, profissional e curta para o dono do restaurante enviar.
        3. **Ação Recomendada:** Uma ação prática para o time operacional do restaurante melhorar o serviço.
        
        Tenha um tom profissional e consultivo.
        """

        prompt = PromptTemplate.from_template(template)

        chain = prompt | llm

        with st.spinner("Consultando o cérebro do Google..."):
            resposta = chain.invoke({"review": review_text})

        # 5. Exibindo o Resultado
        st.success("Análise Concluída!")
        st.markdown(resposta.content)

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
