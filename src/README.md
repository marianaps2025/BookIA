## Como utilizar o BookIA

### 1. Instalação

Clone ou baixe o projeto e abra a pasta no VS Code.
Crie e ative um ambiente virtual Python e instale as dependências:
```bash
pip install -r requirements.txt
```

### 2. Configuração da inteligência artificial

Para utilizar a funcionalidade de inteligência artificial, é necessário configurar uma chave de API do Gemini.
Crie um arquivo chamado `.env` na pasta principal do projeto e adicione:

```env
GEMINI_API_KEY=sua_chave_aqui
```

> **Importante:** não compartilhe ou publique sua chave de API. O arquivo `.env` deve permanecer fora do repositório.

### 3. Executar o BookIA

Na pasta principal do projeto, execute: (Windows)

```bash
streamlit run src\app.py
```

Após a execução, o Streamlit abrirá o BookIA no navegador.

### 4. Utilizando a aplicação

Na tela principal, é possível:

* visualizar os livros cadastrados;
* consultar a quantidade de livros lidos e não lidos;
* visualizar o espaço disponível na estante;
* verificar a possibilidade de novas compras;
* fazer perguntas ao BookIA utilizando.

Exemplos de perguntas:

* "Quantos livros eu tenho?"
* "Quais livros ainda não li?"
* "Quais livros eu já li?"
* "Qual livro tem mais páginas?"
* "Esse livro está na minha biblioteca?"

A aplicação utiliza os dados presentes nos arquivos da pasta `data` para responder às perguntas relacionadas à biblioteca.
