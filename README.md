# 🤖 Agent de Automação de Fluxo de Trabalho

Este repositório contém o desenvolvimento de um **Agente de IA** capaz de automatizar a gestão de tarefas no Trello, integrando a inteligência generativa do Google Gemini para interpretar comandos e organizar fluxos de trabalho.

---

## 📋 Descrição do Projeto

O objetivo deste projeto foi criar um agente autônomo em Python que utiliza o **ADK (Agent Development Kit)** para interagir com a API do Trello. O agente processa prompts em linguagem natural, identifica a intenção do usuário e executa ações como criação, listagem e movimentação de cards em quadros de produtividade.

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** [Python 3.10+](https://www.python.org/)
* **IA Generativa:** [Google AI Studio (Gemini API)](https://aistudio.google.com/)
* **Gestão de Tarefas:** [Trello API](https://developer.atlassian.com/cloud/trello/)
* **Framework de Agentes:** ADK (Agent Development Kit - CI&T)

---

## 🔧 Configuração do Ambiente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/Maike-Simoncini/Agent.git](https://github.com/Maike-Simoncini/Agent.git)
cd Agent

```
### 2. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto (utilize o .env.example como base) e insira suas credenciais:
```text
GOOGLE_API_KEY=sua_chave_aqui
TRELLO_API_KEY=sua_chave_aqui
TRELLO_TOKEN=seu_token_aqui

```
### 3. Instalação e Execução
Utilizamos um ambiente virtual para garantir a integridade das dependências:
```bash
# Criar ambiente virtual
python -m venv .lab-dio

# Ativar ambiente (Windows)
.\.lab-dio\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Iniciar o Agente via Web Interface
adk web

```
## 📈 Resultados Alcançados
O agente demonstrou autonomia para:
 1. **Interpretar intenções:** "Crie uma tarefa de estudo de Python para amanhã".
 2. **Sincronização em tempo real:** Refletir alterações instantaneamente no board do Trello.
 3. **Gestão de Fluxo:** Mover tarefas entre as colunas "To Do", "Doing" e "Done" com base no status da atividade.

## 👨‍💻 Autor
**Maike Simoncini da Silva** *Tecnólogo em Análise e Desenvolvimento de Sistemas*   [LinkedIn](https://www.linkedin.com/in/maike-simoncini-da-silva-9769b2287)  
*Projeto desenvolvido como parte do Bootcamp "Do Prompt ao Agente" da DIO em parceria com a CI&T.*
