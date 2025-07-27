import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen3:1.7b")
project_root = os.path.dirname(os.path.abspath(__file__))

async def main():
    client = MultiServerMCPClient({
        "files": {
            "command": "python",
            "args": ["./mcp_server.py"],
            "transport": "stdio",
            "env": {"PYTHONPATH": project_root}
        }
    })

    # session = client.sessions["files"]
    tools = await client.get_tools()
    print(tools)

    agent = create_react_agent(model, tools)

    print("Agent initialized. Type 'exit' for exit :)")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        try:
            response = await agent.ainvoke({"messages": user_input})
            for m in response['messages']:
                print("Agent: ", m.content)
        except Exception as e:
            import traceback
            print("Exception:", e)
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())








