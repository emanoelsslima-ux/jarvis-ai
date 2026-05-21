# 🤖 Jarvis AI

Assistente virtual futurista desenvolvido com Python, Streamlit e integração com IA generativa utilizando a Groq API.  
O projeto simula um assistente pessoal inteligente com memória conversacional, interface moderna e respostas em tempo real através de modelos LLM.

---

## Tecnologias utilizadas

- Python
- Streamlit
- Groq API
- HTML/CSS
- Python Dotenv
- IA Generativa

---

## Estrutura do projeto

```txt
jarvis-ai
 ┣ assets
 ┃ ┗ jarvis.jpg
 ┃
 ┣ images
 ┃ ┗ preview.png
 ┃
 ┣ app.py
 ┣ style.css
 ┣ requirements.txt
 ┣ .gitignore
 ┣ .env.example
 ┗ README.md
```

---

## Funcionalidades

✔ Chat inteligente em tempo real  
✔ Integração com IA generativa  
✔ Memória conversacional  
✔ Interface futurista personalizada  
✔ Efeito de digitação da IA  
✔ Sidebar interativa  
✔ Layout responsivo  
✔ Sistema de nova conversa  
✔ Customização visual com CSS  

---

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=SUA_CHAVE_AQUI
```

---

## Preview

### Interface principal

<p align="center">
  <img src="assets/preview.png" width="800"/>
</p>

---

### Demonstração do projeto

<p align="center">
  <img src="assets/DemoJarvis.gif" width="800"/>
</p>

---

## Principais funcionalidades

### Memória conversacional

O projeto utiliza `st.session_state` para manter o histórico das conversas durante a sessão.

---

### Integração com IA Generativa

As respostas são geradas utilizando modelos LLM através da Groq API.

---

### Interface futurista personalizada

O Streamlit foi customizado utilizando CSS para criar uma experiência visual moderna inspirada em assistentes virtuais futuristas.

---

### Efeito de digitação

As respostas da IA são exibidas gradualmente para simular uma conversa natural em tempo real.

---

## Objetivo do projeto

Projeto desenvolvido para praticar e demonstrar conhecimentos em:

- Integração com APIs de IA
- Desenvolvimento de aplicações com Streamlit
- IA Generativa
- Engenharia de prompts
- Gerenciamento de estado
- Desenvolvimento frontend com CSS
- Experiência do usuário (UX)
- Construção de chatbots inteligentes
- Arquitetura de aplicações interativas

---

## Melhorias futuras

- Reconhecimento de voz
- Respostas por áudio
- Upload de arquivos
- Integração com banco de dados
- Memória persistente
- Autenticação de usuários
- Geração de imagens
- Multi-agentes

---

## Autor

Victor Emanoel

GitHub:
https://github.com/emanoelsslima-ux

LinkedIn:
https://www.linkedin.com/in/victorlimapy