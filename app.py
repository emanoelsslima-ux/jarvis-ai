import os
import time

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# =========================
# CONFIGURAÇÃO
# =========================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="Jarvis AI",
    page_icon="🤖",
    layout="centered"
)

# =========================
# CARREGAR CSS
# =========================

with open("styles/styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("# 🤖 Jarvis")

    st.success("Sistema Online")

    st.write("Assistente pessoal operacional.")

    st.divider()

    if st.button("🗑️ Nova conversa"):

        st.session_state["messages"] = [
            st.session_state["messages"][0]
        ]

        st.rerun()

# =========================
# HEADER
# =========================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.image("assets/jarvis.jpg", width=700)

    st.markdown(
        "<h1 style='text-align:center; color:cyan;'>Jarvis</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center; color:white;'>Bem-vindo de volta, Senhor.</h4>",
        unsafe_allow_html=True
    )

# =========================
# MEMÓRIA
# =========================

if "messages" not in st.session_state:

    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """
            Você é Jarvis, uma inteligência artificial brasileira,
            elegante, eficiente e futurista.

            O nome do seu criador é Victor Emanoel.

            Sempre trate Victor como Senhor.

            Seu tom deve ser:
            - Inteligente
            - Calmo
            - Sofisticado
            - Prestativo

            Nunca fale de forma exageradamente robótica.
            """
        }
    ]

# =========================
# EXIBIR CHAT
# =========================

for message in st.session_state["messages"]:

    role = message["role"]
    content = message["content"]

    if role != "system":

        avatar = "🧑" if role == "user" else "🤖"

        st.chat_message(role, avatar=avatar).write(content)

# =========================
# INPUT
# =========================

user_input = st.chat_input("Digite sua mensagem")

# =========================
# RESPOSTA DA IA
# =========================

if user_input:

    st.chat_message("user", avatar="🧑").write(user_input)

    user_message = {
        "role": "user",
        "content": user_input
    }

    st.session_state["messages"].append(user_message)

    try:

        with st.spinner("Jarvis está analisando..."):

            response = client.chat.completions.create(
                messages=st.session_state["messages"],
                model="llama-3.1-8b-instant"
            )

            ai_response = response.choices[0].message.content

    except Exception as error:

        ai_response = f"Erro: {error}"

    with st.chat_message("assistant", avatar="🤖"):

        full_response = ""

        placeholder = st.empty()

        for word in ai_response.split():

            full_response += word + " "

            placeholder.markdown(full_response)

            time.sleep(0.03)

    assistant_message = {
        "role": "assistant",
        "content": ai_response
    }

    st.session_state["messages"].append(assistant_message)