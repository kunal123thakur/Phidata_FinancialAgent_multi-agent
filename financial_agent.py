from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the GROQ_API_KEY from environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')



web_search_agent = Agent(
    name='web search agent',
    role="search the web fot the information",
    model = Groq(id="llama-3.3-70b-versatile",GROQ_API_KEY=GROQ_API_KEY),
    tools=[DuckDuckGo()],
    instructions=["Always include sources "],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name = "Finance Ai Agent",
    role = "Get the financial data",
    model = Groq(id="llama-3.3-70b-versatile",GROQ_API_KEY=GROQ_API_KEY),
    tools=[
        YFinanceTools(stock_price=True, stock_fundamentals=True,company_news=True,analyst_recommendations=True ),],
        
    instructions=["use tables to display the data "],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    # name="Multi Ai Agent",
    model = Groq(id="llama-3.3-70b-versatile",GROQ_API_KEY=GROQ_API_KEY),
    instructions=["Always include sources ","use tables to display the data "],
    show_tool_calls=True,
    markdown=True,

)

#intiation
multi_ai_agent.print_response("Summarize analyst recommendation ans share the latest news and stock price of Apple Inc. (AAPL) ")

