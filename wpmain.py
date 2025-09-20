from agno.agent import Agent, RunResponse
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.app.whatsapp.app import WhatsappAPI
from agno.app.fastapi.app import FastAPIApp
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.whatsapp import WhatsAppTools
from agno.tools.wikipedia import WikipediaTools
from agno.models.openai.like import OpenAILike
from agno.models.ollama import Ollama
from agno.tools.website import WebsiteTools
from ollama import AsyncClient as OllamaAsyncClient
from ollama import Client as OllamaClient
from typing import Any, Callable, Dict
#from os import getenv
from agno.team import Team
from agno.tools import tool

#ollhost='https://64e24cff7d4e.ngrok-free.app/'
phishingtextagent=Agent(agent_id="PTA",
 #model=Gemini(id="gemini-2.0-flash"),
 #model=Ollama(id="qwen3:14b",async_client=OllamaAsyncClient(host=ollhost),client=OllamaClient(host=ollhost)),
    model=Groq(id="openai/gpt-oss-20b"),
    instructions=("""
                  You are an phishing protection agent your task is to read the message user sends and predict if it's a phishing mail \n
                  Read the text carefully and tell the user why it might be a scam or phishing attack, use google search and duckduckgo search to verify any added links and use website tools to check for inconsistency in the website \n
                  """),
    tools=[WhatsAppTools(),GoogleSearchTools(),WikipediaTools(),WebsiteTools()],
    debug_mode=True)
webhtmlagent=Agent(agent_id="WSA",
 #model=Gemini(id="gemini-2.0-flash"),
 #model=Ollama(id="qwen3:14b",async_client=OllamaAsyncClient(host=ollhost),client=OllamaClient(host=ollhost)),
    model=Groq(id="openai/gpt-oss-20b"),
    instructions=("""
                  You are an phishing protection agent your task is to read the message user sends and predict if it's a phishing mail \n
                  Read the text carefully and tell the user why it might be a scam or phishing attack, use google search and duckduckgo search to verify any added links and use website tools to check for inconsistency in the website \n
                  """),
    tools=[WhatsAppTools(),GoogleSearchTools(),WikipediaTools(),WebsiteTools()],
    debug_mode=True)

#phishingtextagent.print_response("URGENT: YOUR ACCOUNT HAS BEEN SUSPENDED DUE TO SUSPICIOUS ACTVITY, CLICK LINK TO KNOW MORE https://sbibank.xyz")

fstapp=FastAPIApp(agents=[phishingtextagent])
wpapp=WhatsappAPI(agent=phishingtextagent)
app=wpapp.get_app()
if __name__ == "__main__":
    wpapp.serve(app="wpmain:app", port=8001, reload=True)