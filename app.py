import os
import time
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# =====================================
# CONFIGURAÇÕES
# =====================================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="Jarvis AI",
    page_icon="🤖",
    layout="centered"
)

# =====================================
# CSS
# =====================================

with open("style.css", encoding="utf-8") as css:
    st.markdown(
        "<style>" + css.read() + "</style>",
        unsafe_allow_html=True
    )

# =====================================
# MEMÓRIA
# =====================================

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """
            Você é Jarvis, uma inteligência artificial sofisticada, elegante e eficiente.
            Seu criador é Victor Emanoel.
            Seu comportamento deve ser:
            - Inteligente
            - Calmo
            - Futurista
            - Educado
            - Prestativo
            Utilize respostas naturais e elegantes.
            """
        }
    ]

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:
    st.markdown("# 🤖 Jarvis AI")
    st.success("Sistema Online")
    st.write("Assistente virtual operacional")
    st.divider()
    
    if st.button("🗑️ Nova conversa"):
        st.session_state["messages"] = [st.session_state["messages"][0]]
        st.rerun()

# =====================================
# HEADER
# =====================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/jarvis.jpg", width=450)
    
    # Alterado para usar classes que seu style.css estiliza sem dar conflito de cor inline
    st.markdown("<h1 style='text-align:center;, class='jarvis-title'>Jarvis AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Bem-vindo de volta, Senhor.</p>", unsafe_allow_html=True)
# =====================================
# EXIBIR CHAT
# =====================================

for message in st.session_state["messages"]:
    if message["role"] != "system":
        avatar = "🧑" if message["role"] == "user" else "🤖"
        with st.chat_message(message["role"], avatar=avatar):
            st.write(message["content"])

# =====================================
# INPUT DO USUÁRIO
# =====================================

user_input = st.chat_input("Digite sua mensagem")

# =====================================
# RESPOSTA DA IA
# =====================================

if user_input:
    # Exibe e salva mensagem do usuário
    st.chat_message("user", avatar="🧑").write(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Fluxo de resposta da IA unificado e seguro
    try:
        with st.spinner("Jarvis está analisando..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Dica: teste o 'llama-3.3-70b-versatile' se quiser mais precisão
                messages=st.session_state["messages"]
            )
            ai_response = response.choices[0].message.content

        # O efeito de escrita e o salvamento em memória agora acontecem no lugar certo
        with st.chat_message("assistant", avatar="🤖"):
            placeholder = st.empty()
            full_response = ""
            
            for word in ai_response.split(" "):
                full_response += word + " "
                placeholder.markdown(full_response)
                time.sleep(0.02)

        # Só adicionamos ao histórico se a API respondeu com sucesso
        st.session_state["messages"].append({"role": "assistant", "content": ai_response})

    except Exception as error:
        st.error(f"Erro na comunicação: {error}")