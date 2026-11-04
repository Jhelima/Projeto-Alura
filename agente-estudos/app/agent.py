import os
from datetime import date
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.skills import load_skill_from_dir

load_dotenv()

# Caminho absoluto para a pasta de skills
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.join(BASE_DIR, "skills", "plano-de-estudos")
skill = load_skill_from_dir(skill_path)

# Carrega as ferramentas expostas pela skill
tools_list = skill.get_tools() if hasattr(skill, "get_tools") else []

# Define o agente principal do ADK
root_agent = Agent(
    name="agente_estudos",
    model=os.getenv("MODEL", "gemini-1.5-flash"),
    instruction=f"Você é um tutor de estudos especializado. Hoje é {date.today().isoformat()}.",
    tools=tools_list
)

