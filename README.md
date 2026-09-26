# BookIA — Assistente Inteligente de Biblioteca Pessoal
dio-lab-bia-do-futuro-main/
│
├── assets/
├── data/
│   ├── biblioteca.json
│   ├── livros.csv
│   └── outros arquivos...
│
├── docs/
├── examples/
├── src/
│   └── app.py
│
├── .env
├── README.md

## 1. Descrição do projeto

O BookIA é um assistente inteligente desenvolvido para auxiliar na organização e consulta de uma biblioteca pessoal. A aplicação permite visualizar os livros cadastrados, acompanhar a quantidade de livros lidos e não lidos, verificar o espaço disponível na estante e consultar informações da biblioteca por meio de perguntas específicas. Assim, um leitor pode utilizar deste "serviço" para facilitar a administração da sua biblioteca. Quis realizar um projeto assim (já que o tema não era obrigatório), justamente por ser um assistente que todos podem utilizar e testar, e não somente um mercado específico.

A aplicação foi desenvolvida utilizando Python e Streamlit, com integração a um modelo de linguagem da família Gemini para realizar as consultas.

A base de dados principal do projeto é composta pelos arquivos `livros.csv` e `biblioteca.json`.

---

## 2. Objetivo Principal do BookIA

O objetivo do BookIA é facilitar o gerenciamento de uma biblioteca pessoal por meio de uma interface simples e de um assistente baseado em inteligência artificial.

O sistema busca permitir que o usuário consulte informações como:

- quantidade total de livros;
- livros já lidos;
- livros ainda não lidos;
- livros doados (ainda em melhor desenvolvimento);
- informações sobre autores, gêneros e páginas;
- datas de início e término das leituras (ainda em melhor desenvolvimento);
- espaço disponível na estante;
- possibilidade de realizar novas compras.

Além disso, o agente deve utilizar os dados disponíveis na biblioteca para responder às perguntas e evitar inventar informações que não estejam presentes na base.

---

## 3. Público-alvo

O BookIA é destinado principalmente a pessoas que possuem uma biblioteca pessoal e desejam organizar seus livros e histórico de leitura de maneira mais prática.

O sistema pode ser utilizado por leitores que desejam acompanhar seus hábitos de leitura, consultar rapidamente informações sobre seus livros e verificar a capacidade disponível para novas aquisições.

---

## 4. Base de conhecimento

A principal base de conhecimento do BookIA está localizada na pasta `data` do projeto.

### `livros.csv`

O arquivo contém os dados dos livros cadastrados na biblioteca, incluindo:

- ID;
- título;
- autor;
- gênero;
- quantidade de páginas;
- status de leitura;
- data de início;
- data de término;
- informação sobre doação.

Atualmente, a base utilizada pelo BookIA contém **15 livros**.

Entre os livros cadastrados estão *Dom Casmurro*, *O Hobbit*, *Duna*, *Coraline*, *1984*, *It a Coisa*, *As Crônicas de Narnia* e *O Nome do Vento*.

### `biblioteca.json`

O arquivo contém as informações relacionadas à capacidade física da estante.

Atualmente:

- capacidade total: **30 livros**;
- quantidade atual: **15 livros**;
- espaço disponível: **15 livros**.

IMPORTANTE:
Qualquer outro arquivo presente do repositório original não é utilizado pelo BookIA, pois pertence a outras funcionalidades/projetos dados como base para o desenvolvimento deste. 

---

## 5. Funcionamento da aplicação

A aplicação é executada utilizando o Streamlit.

Ao acessar o BookIA, o usuário encontra:

1. identificação do sistema;
2. quantidade total de livros;
3. quantidade de livros lidos;
4. quantidade de livros não lidos;
5. espaço disponível na estante;
6. tabela contendo os livros da biblioteca;
7. ferramenta para verificar novas compras;
8. campo para realizar perguntas ao assistente de IA.

Na ferramenta de compras, o usuário informa quantos livros pretende comprar. O sistema compara essa quantidade com o espaço disponível na estante e informa se a compra é possível.

Na área do assistente, o usuário pode realizar perguntas sobre os dados da biblioteca.

---

## 6. Uso da LLM

O BookIA utiliza uma LLM da família Gemini para interpretar as perguntas feitas pelo usuário e produzir respostas.

Os dados do arquivo `livros.csv` são transformados em texto e enviados junto com informações calculadas pela aplicação, como:

- quantidade total de livros;
- quantidade de livros lidos;
- quantidade de livros não lidos;
- capacidade da estante;
- quantidade atual;
- espaço disponível.

A LLM recebe o contexto da biblioteca antes de responder à pergunta do usuário.

A integração é realizada por meio da biblioteca oficial `google-genai`, utilizando uma chave armazenada em uma variável de ambiente no arquivo `.env`. Que por questão de segurança não estará anexada aqui.

---

## 7. Prompt e regras do agente

O BookIA possui instruções específicas para orientar o comportamento da LLM.

Entre as principais regras estão:

- utilizar exclusivamente os dados fornecidos;
- não inventar livros;
- não inventar autores;
- não inventar datas;
- não inventar páginas;
- não inventar quantidades;
- considerar somente livros marcados como lidos quando a pergunta tratar de leituras;
- considerar somente livros marcados como doados quando a pergunta tratar de doações;
- utilizar os dados da estante para cálculos relacionados à capacidade;
- informar claramente quando uma informação não estiver disponível;
- responder em português;
- manter respostas claras e objetivas.

Essas regras têm como objetivo reduzir respostas incorretas ou informações inventadas pela IA.

---

## 8. Limitações

O BookIA depende da disponibilidade do serviço de inteligência artificial utilizado pela aplicação.

Durante os testes, foram observados momentos em que a API retornou o erro `503 UNAVAILABLE`, indicando indisponibilidade temporária do modelo devido à alta demanda.

Para evitar que o usuário veja uma mensagem técnica extensa, a aplicação apresenta uma mensagem informando que o serviço de IA está temporariamente indisponível.

Outra limitação é que as respostas da LLM dependem das informações disponíveis na base de conhecimento. Quando determinado dado não está presente nos arquivos utilizados pelo BookIA, o agente deve informar que não encontrou a informação.

---

## 9. Avaliação e métricas

A avaliação do BookIA será realizada por meio de perguntas relacionadas aos dados reais da biblioteca.

Entre os testes estão:

- Consultar quais livros ainda não foram lidos
✅ Resposta correta;

- Consultar a quantidade total de livros
✅ 15 livros;

- Consultar o espaço disponível na estante
✅ 15 livros;

- Consultar quais livros já foram lidos
✅ 12 livros;

- Consultar um livro que não existe na biblioteca
✅ O agente informou que a informação não estava disponível;

- Identificar o livro com mais páginas entre os não lidos
✅ It a Coisa, de Stephen King, com 1.104 páginas.

A avaliação considera principalmente:

### Precisão

Calculada a quantidade de respostas corretas em relação ao número total de perguntas avaliadas.

**Precisão = respostas corretas ÷ total de testes × 100**

### Alucinação

Também verificado se o agente inventa informações que não estão presentes na base de conhecimento.

Esse teste é especialmente importante para verificar se as regras definidas no prompt estão sendo respeitadas.

E como retorno resumidamente:

Os testes demonstraram que o BookIA conseguiu utilizar os dados fornecidos pela biblioteca para responder às perguntas propostas. Também foi verificado um comportamento importante de segurança contra informações inventadas: ao ser questionado sobre um livro que não estava cadastrado, o agente informou que não encontrou a informação na base.

Durante o desenvolvimento, também ocorreram momentos - como citado - em que a API do Gemini retornou o erro 503 UNAVAILABLE, indicando indisponibilidade temporária do serviço. Por esse motivo, os testes de integração foram realizados em momentos diferentes. Posteriormente, novas tentativas foram realizadas com sucesso.

A avaliação apresentada corresponde aos testes efetivamente realizados durante o desenvolvimento e NÃO representa uma avaliação exaustiva de todos os possíveis tipos de pergunta, por isso não se pode dizer que há uma eficiência de 100%.


---

## 10. Conclusão e pitch

O BookIA demonstra como uma aplicação simples pode utilizar inteligência artificial para facilitar a organização de uma biblioteca pessoal, com um layout simples, respostas sucintas.

O sistema combina uma base estruturada de livros com uma interface desenvolvida em Streamlit e uma LLM capaz de interpretar perguntas em linguagem natural.

A proposta permite que o usuário consulte sua biblioteca de maneira mais rápida e fácil, além de acompanhar informações relacionadas às leituras e à capacidade da sua estante.

Como resultado, o BookIA integra organização de dados, regras de negócio e inteligência artificial em uma aplicação prática e voltada para uma necessidade cotidiana.

### Pitch

O BookIA é um assistente inteligente criado para transformar uma biblioteca pessoal em uma experiência mais organizada e interativa.

Em vez de procurar manualmente informações sobre seus livros, o usuário pode perguntar ao BookIA o que deseja saber. O sistema utiliza os dados cadastrados na biblioteca para responder perguntas sobre leituras, livros não lidos, doações e espaço disponível na estante.

Além disso, o BookIA possui regras para evitar que a inteligência artificial invente informações que não estejam presentes na base.

A proposta é unir uma interface simples, dados estruturados e inteligência artificial para tornar o gerenciamento de uma biblioteca pessoal mais prático.

## Nota sobre o desenvolvimento!

O desenvolvimento do BookIA foi realizado como parte de um processo de aprendizagem e contou com o apoio de uma ferramenta de inteligência artificial generativa durante algumas etapas do projeto. Como: 
apoio para compreender conceitos, solucionar dúvidas, identificar e corrigir erros, estruturar partes do código e organização. As decisões sobre a proposta do projeto, suas funcionalidades, testes, resultados e organização da documentação, além de questionamentos, foram acompanhadas e avaliadas durante TODO o desenvolvimento.
O projeto também passou por etapas de tentativa, erro e correção, incluindo dificuldades na integração com a API de inteligência artificial. Essas etapas fazem parte do processo de desenvolvimento e foram registradas na documentação para apresentar de forma transparente a evolução do BookIA. Ainda sobre os arquivos que possam constar aqui e são da base da DIO, não quis ferir nenhum direito, eles não foram usados para fazer a BookIa funcionar.
