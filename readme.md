Here’s a `README.md` that explains your project, making it easy for you to revisit and understand the structure and purpose of each component:

---
![alt text](<Screenshot 2025-03-29 161719.png>)

# AI Agent-Based Project

This project demonstrates the use of AI agents in a multi-agent system. The system is composed of several agents, each performing specific tasks. The agents are designed to use the Groq model and various tools to search the web for information and retrieve financial data.

## Overview

The project has three main agents:
1. **Web Search Agent**: Responsible for searching the web and retrieving relevant information.
2. **Finance AI Agent**: Retrieves financial data for stocks, such as stock price, fundamentals, company news, and analyst recommendations.
3. **Multi-AI Agent**: A composite agent that combines both the Web Search Agent and Finance AI Agent to provide a broader range of capabilities.

### Key Tools Used:
- **Groq**: The language model used for AI tasks. In this project, the Groq model is used to process instructions and generate responses.
- **DuckDuckGo**: A tool used by the Web Search Agent to perform searches.
- **YFinanceTools**: A tool used by the Finance AI Agent to fetch stock price, financial fundamentals, company news, and analyst recommendations.
- **dotenv**: A Python package used for loading environment variables from a `.env` file.

## Setup

### Prerequisites
- Python 3.x
- Install the required libraries:
  ```bash
  pip install phi dotenv yfinance duckduckgo
  ```

### Environment Variables
Create a `.env` file in the root directory of your project to store your API keys. You should have the following in your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

This key is used by the Groq model in all the agents.

### Folder Structure

Your project should have the following structure:

```
/project_root
  ├── .env                  # Environment variables
  ├── agent_code.py         # The Python code for agents
  ├── README.md             # This readme file
```

## How It Works

### 1. Web Search Agent
The Web Search Agent is initialized to search the web using DuckDuckGo and retrieve relevant information. It is configured to always include sources in its results and to return responses in Markdown format.

```python
web_search_agent = Agent(
    name='web search agent',
    role="search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile", GROQ_API_KEY=GROQ_API_KEY),
    tools=[DuckDuckGo()],
    instructions=["Always include sources "],
    show_tool_calls=True,
    markdown=True,
)
```

### 2. Finance AI Agent
The Finance AI Agent is tasked with fetching financial data related to stocks using the YFinanceTools. It retrieves stock prices, financial fundamentals, company news, and analyst recommendations. The agent formats its responses in tables for better clarity.

```python
financial_agent = Agent(
    name="Finance Ai Agent",
    role="Get the financial data",
    model=Groq(id="llama-3.3-70b-versatile", GROQ_API_KEY=GROQ_API_KEY),
    tools=[
        YFinanceTools(stock_price=True, stock_fundamentals=True, company_news=True, analyst_recommendations=True),
    ],
    instructions=["use tables to display the data "],
    show_tool_calls=True,
    markdown=True,
)
```

### 3. Multi-AI Agent
The Multi-AI Agent is a combination of the Web Search Agent and Finance AI Agent. It is capable of handling tasks that require both web searches and financial data fetching. In this setup, the Multi-AI Agent is asked to summarize analyst recommendations, stock prices, and the latest news for Apple Inc. (AAPL).

```python
multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile", GROQ_API_KEY=GROQ_API_KEY),
    instructions=["Always include sources", "use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)
```

### Initiating the Multi-AI Agent
You initiate the multi-agent system by calling the `print_response` method with a task. The agents will work together to complete the task:

```python
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news and stock price of Apple Inc. (AAPL)")
```

### Task Example
When you run the above command, the Multi-AI Agent will:
- Search the web for relevant information about Apple Inc. (AAPL).
- Fetch the stock price, analyst recommendations, and other financial data related to Apple Inc.
- Display the results in Markdown format with sources and tables.

## Conclusion

This project demonstrates how to use multiple AI agents to handle different tasks, such as web search and financial analysis. Each agent is specialized in its task, and the Multi-AI Agent combines them to provide a holistic solution.

---

Feel free to modify the instructions and tools for the agents to suit your needs.