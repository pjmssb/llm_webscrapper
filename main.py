import os
import dotenv
import anthropic
import nest_asyncio
from lxml import etree
from io import StringIO
import asyncio
from playwright.async_api import async_playwright

nest_asyncio.apply()
dotenv.load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")

print(f"\n\n\n\n\n\n\n\n\n\n\n\n\nLLM API\nURL: {LLM_API_URL}\nKEY: {LLM_API_KEY}")

url = 'https://miasmoda.cl/collections/all?filter.v.option.color=Negro&filter.v.price.gte=&filter.v.price.lte=33.74&sort_by=price-ascending'


página_web = AsyncChromiumLoader([url])
documento = página_web.load()

cliente_llm = anthropic.Anthropic(api_key=LLM_API_KEY)
MODELO_LLM = "claude-3-sonnet-20240229"
ROL = "clothes buyer, 25 years old, married, female"
LIMITE_TOKENS = 1024

respuesta_llm = cliente_llm.messages.create(
    model=MODELO_LLM, max_tokens=LIMITE_TOKENS,messages=[
    {
      "role": ROL,
      "content": f"Selecciona los bodys más economicos en esta página {documento}"
    }
  ]
)

print(respuesta_llm)