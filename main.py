import os
import dotenv
import time

dotenv.load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")

print(f"LLM API\nURL: {LLM_API_URL}\nKEY{LLM_API_KEY}")