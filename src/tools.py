import os
import requests
from typing import List, Optional

# Carregamento de credenciais (assumindo que o main.py já chamou load_dotenv)
API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
BOARD_ID = os.getenv("TRELLO_BOARD_ID")

BASE_URL = "https://api.trello.com/1"

def list_trello_cards() -> List[str]:
    """
    Lista todos os nomes dos cards presentes no quadro configurado.
    """
    url = f"{BASE_URL}/boards/{BOARD_ID}/cards"
    query = {'key': API_KEY, 'token': TOKEN}
    
    try:
        response = requests.get(url, params=query)
        response.raise_for_status()
        cards = response.json()
        return [card['name'] for card in cards]
    except Exception as e:
        return [f"Erro ao listar cards: {str(e)}"]

def create_trello_card(name: str, desc: Optional[str] = "Criado via Agente Python") -> str:
    """
    Cria um novo card no Trello na lista inicial do quadro.
    """
    # Para simplificar, precisamos do ID da lista (To Do). 
    # Em um projeto real, você buscaria esse ID dinamicamente.
    list_id = "ID_DA_SUA_LISTA_AQUI" # Substitua pelo ID real ou lógica de busca
    
    url = f"{BASE_URL}/cards"
    query = {
        'idList': list_id,
        'key': API_KEY,
        'token': TOKEN,
        'name': name,
        'desc': desc
    }

    try:
        response = requests.post(url, params=query)
        response.raise_for_status()
        return f"Sucesso: Card '{name}' criado no Trello."
    except Exception as e:
        return f"Falha ao criar card: {str(e)}"

def move_card_to_done(card_name: str) -> str:
    """
    Localiza um card pelo nome e o move para a lista 'Done'.
    """
    # Lógica simplificada: 
    # 1. Busca o card pelo nome
    # 2. Atualiza o idList para o ID da coluna 'Done'
    done_list_id = "ID_DA_LISTA_DONE"
    
    # Aqui entraria a lógica de 'Fuzzy Matching' que comentamos antes
    # para garantir que variações de texto não quebrem a automação.
    return f"Simulação: Card '{card_name}' movido para concluído."

# Estas funções são as que você passa para o Agente no main.py
tools = [list_trello_cards, create_trello_card, move_card_to_done]
