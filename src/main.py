import os
import sys
from dotenv import load_dotenv
from adk import Agent, UI  # Ajuste conforme as classes exatas do seu ADK

# Carrega as configurações do ficheiro .env
load_dotenv()

def bootstrap():
    """
    Verifica se todas as credenciais necessárias estão presentes
    antes de iniciar o agente.
    """
    required_keys = ["GOOGLE_API_KEY", "TRELLO_API_KEY", "TRELLO_TOKEN"]
    missing_keys = [key for key in required_keys if not os.getenv(key)]
    
    if missing_keys:
        print(f"❌ Erro: As seguintes chaves estão faltando no .env: {', '.join(missing_keys)}")
        print("Certifique-se de configurar o arquivo .env baseado no .env.example")
        sys.exit(1)

def main():
    # 1. Validação de ambiente
    bootstrap()
    
    print("🤖 Iniciando Agente de Automação de Tarefas...")

    try:
        # 2. Inicialização do Agente
        # O ADK geralmente requer a chave do Gemini para o cérebro do agente
        agent = Agent(
            name="TaskBot-Simoncini",
            model="gemini-1.5-flash",
            api_key=os.getenv("GOOGLE_API_KEY"),
            instructions="""
                Você é um assistente de produtividade especializado em Trello.
                Sua função é criar, listar e mover tarefas de forma eficiente.
                Sempre confirme a execução da tarefa no quadro do usuário.
            """
        )

        # 3. Execução da Interface (Web ou Terminal)
        # Como no seu README você mencionou 'adk web', usamos a interface UI
        ui = UI(agent)
        ui.launch()

    except Exception as e:
        print(f"⚠️ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
