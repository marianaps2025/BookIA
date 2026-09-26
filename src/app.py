
import streamlit as st
import pandas as pd
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Carregar variáveis do arquivo .env
pasta_projeto = Path(__file__).resolve().parent.parent
load_dotenv(pasta_projeto / ".env")

# Configuração da página
st.set_page_config(
    page_title="BookIA",
    page_icon="📚"
)

# Configuração da API Gemini
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    st.success("🤖 Inteligência Artificial conectada!")
    cliente = genai.Client(api_key=api_key)
else:
    st.error("❌ GEMINI_API_KEY não foi encontrada.")
    cliente = None

# Caminhos dos arquivos
caminho_livros = pasta_projeto / "data" / "livros.csv"
caminho_biblioteca = pasta_projeto / "data" / "biblioteca.json"

# Leitura da base de livros
livros = pd.read_csv(caminho_livros)

# Leitura das informações da estante
with open(caminho_biblioteca, "r", encoding="utf-8") as arquivo:
    biblioteca = json.load(arquivo)

# Título
st.title("📚 BookIA")
st.subheader("Seu assistente inteligente de biblioteca")

st.write(
    "Olá! Eu sou o BookIA. "
    "Vou ajudar você a organizar sua biblioteca "
    "e seu histórico de leitura."
)

st.divider()

# Informações dos livros
total_livros = len(livros)
livros_lidos = (livros["status"] == "Lido").sum()
livros_nao_lidos = (livros["status"] == "Nao lido").sum()

# Informações da estante
capacidade_estante = biblioteca["capacidade_estante"]
quantidade_atual = biblioteca["quantidade_atual"]
espaco_disponivel = capacidade_estante - quantidade_atual

# Exibição das informações
st.write(f"📚 Livros na biblioteca: **{total_livros}**")
st.write(f"📖 Livros lidos: **{livros_lidos}**")
st.write(f"📕 Livros não lidos: **{livros_nao_lidos}**")
st.write(f"🏠 Espaço disponível na estante: **{espaco_disponivel} livros**")

st.divider()

# Biblioteca
st.write("### 📋 Minha biblioteca")
st.dataframe(livros)

st.divider()

# Verificar compras
st.write("### 🛒 Verificar novas compras")

quantidade_compra = st.number_input(
    "Quantos livros você pretende comprar?",
    min_value=0,
    step=1
)

if st.button("Verificar espaço"):
    if quantidade_compra <= espaco_disponivel:
        espaco_restante = espaco_disponivel - quantidade_compra

        st.success(
            f"Sim! Cabem mais {quantidade_compra} livros. "
            f"Depois da compra, ainda sobrariam {espaco_restante} espaços."
        )
    else:
        falta = quantidade_compra - espaco_disponivel

        st.error(
            f"Não cabem todos os {quantidade_compra} livros. "
            f"Você tem espaço para mais {espaco_disponivel} livros "
            f"e faltariam {falta} espaços."
        )

st.divider()

# Assistente com LLM
st.write("### 🤖 Converse com o BookIA")

pergunta = st.text_input(
    "Faça uma pergunta sobre sua biblioteca:",
    placeholder="Ex.: Quais livros eu ainda não li?"
)

if st.button("Perguntar à IA"):
    if not pergunta:
        st.warning("Digite uma pergunta primeiro.")
    elif cliente is None:
        st.error("A IA não está conectada. Verifique a GEMINI_API_KEY.")
    else:
        # Transformar os dados da biblioteca em texto
        dados_livros = livros.to_string(index=False)

        contexto = f"""
Você é o BookIA, um assistente inteligente de biblioteca.

Sua função é responder perguntas sobre a biblioteca do usuário
usando EXCLUSIVAMENTE os dados fornecidos abaixo.

REGRAS:
1. Nunca invente informações.
2. Nunca invente livros, autores, datas, páginas ou quantidades.
3. Se a informação não estiver nos dados, diga claramente
   que não encontrou essa informação.
4. Considere como "Lido" somente os livros cujo status seja "Lido".
5. Considere como "Não lido" somente os livros cujo status seja "Nao lido".
6. Considere como doado somente os livros cujo campo "doado"
   seja "Sim".
7. Para calcular o tempo de leitura, use a diferença entre
   data_inicio e data_fim.
8. Para informações sobre a estante, use os valores fornecidos
   de capacidade, quantidade atual e espaço disponível.
9. Faça os cálculos necessários usando somente os dados fornecidos.
10. Responda em português, de forma clara e objetiva.
11. Se não houver dados suficientes para responder, não adivinhe.

DADOS DOS LIVROS:
{dados_livros}

INFORMAÇÕES DA ESTANTE:
- Capacidade: {capacidade_estante} livros
- Quantidade atual: {quantidade_atual} livros
- Espaço disponível: {espaco_disponivel} livros

PERGUNTA DO USUÁRIO:
{pergunta}
"""

        try:
            resposta = cliente.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=contexto
            )

            st.write("### 💬 Resposta do BookIA")
            st.write(resposta.text)

        except Exception as erro:
            mensagem_erro = str(erro)

            if "503" in mensagem_erro or "UNAVAILABLE" in mensagem_erro:
                st.warning(
                    "🤖 O serviço de IA está temporariamente indisponível. "
                    "Tente novamente em alguns instantes."
                )
            else:
                st.error(
                    "❌ Não foi possível consultar a IA no momento."
                )

