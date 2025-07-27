# Custom Model Tooling Experiments

A practical experiment in AI tool integration using the Model Context Protocol (MCP) to create intelligent file management capabilities. This project demonstrates how to build custom AI agents that can interact with file systems through a clean, protocol-based interface.

**Key Learning Goal**: This project showcases how to work with the MCP protocol beyond just Claude - demonstrating integration with OpenAI models, LangChain, and other AI frameworks. It proves that MCP is a universal standard for AI-tool communication, not limited to any single AI provider.

## 🚀 What This Does

This project creates an AI-powered file management system that consists of:

- **MCP Server**: Provides file storage tools (create, read, list files) via Model Context Protocol
- **AI Agent**: A conversational agent powered by Ollama (qwen3:1.7b) that can interact with your files using natural language
- **Seamless Integration**: Uses LangChain and LangGraph for smooth AI-to-tool communication

Ask the AI agent to "create a shopping list", "show me all my files", or "read my notes" - it understands and executes these commands through the MCP protocol.

## 📋 Prerequisites

### 1. Ollama Installation

You need to install Ollama for your platform:

- **Windows**: Download from [https://ollama.com/download/windows](https://ollama.com/download/windows) (Requires Windows 10 or later)
- **macOS**: Download from [https://ollama.com/download](https://ollama.com/download)
- **Linux**: Download from [https://ollama.com/download](https://ollama.com/download)

### 2. Python Requirements

- Python 3.12 or higher

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd custom-model-tooling-experiments
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Download the AI model**:
   ```bash
   ollama pull qwen3:1.7b
   ```

## 🚀 Usage

### Start the AI Agent

Run the client to start interacting with your AI file manager:

```bash
python mcp_client.py
```

### Example Interactions

Here's a detailed example showing how the AI agent processes your request:

```
You: create a file with 4 lines of colors

Agent: create a file with 4 lines of colors

Agent: <think>
Okay, the user wants to create a file with 4 lines of colors. Let me think about how to approach this.

First, I need to figure out the content for the file. The user didn't specify the exact colors, so maybe they want common ones like red, blue, green, yellow. I'll go with that. The file should have four lines, each with a color. So lines could be "Red", "Blue", "Green", "Yellow".

Next, the function to use is create_text_file. The parameters required are name and content. The name should be something like "colors.txt" or similar. The content is the string with the four lines. I need to make sure the content is properly formatted as a string.

I should check if the file might already exist, but the user didn't mention overwriting, so it's okay to overwrite. The function will handle that. So the arguments would be name: "colors.txt" and content: "Red\nBlue\nGreen\nYellow".

Wait, the content is a string, so I need to make sure the newlines are correctly placed. Each line ends with a newline character. The function should handle that.

So the tool call would be to create_text_file with those parameters. The user didn't specify the name, but using a default name like "colors.txt" is reasonable. I think that's all.
</think>

Agent: {
  "status": "success",
  "file": "/path/to/project/data/colors.txt"
}

Agent: <think>
Okay, the user asked to create a file with 4 lines of colors. I used the create_text_file function and wrote "Red\nBlue\nGreen\nYellow" into a file named "colors.txt". The response from the tool shows the file was created successfully at the specified path. Now I need to let the user know it's done and maybe provide the file path for reference.

I should confirm the action was successful and mention the location of the file. Keep it simple and clear. Something like, "The file 'colors.txt' has been created at /path/to/project/data/colors.txt. It contains the following colors: Red, Blue, Green, Yellow." That's straightforward and gives the user the necessary information without excess details.
</think>

Agent: The file 'colors.txt' has been created at `/path/to/project/data/colors.txt` and contains the following colors:
**Red**
**Blue**
**Green**
**Yellow**

Let me know if you need further modifications!
```

### Available Commands

The AI agent can understand natural language requests for:

- **Creating files**: "Write a note about...", "Create a file with..."
- **Reading files**: "Show me...", "What's in my...", "Read the..."
- **Listing files**: "What files do I have?", "List my files"

## 🏗️ Project Structure

```
custom-model-tooling-experiments/
├── mcp_client.py          # AI agent client using LangChain
├── mcp_server.py          # MCP server with file tools
├── pyproject.toml         # Project configuration
├── data/                  # Directory for stored files
└── README.md             # This file
```

## 🔧 How It Works

1. **MCP Server** (`mcp_server.py`): Exposes three tools via Model Context Protocol:
   - `create_text_file()`: Creates/overwrites text files
   - `list_files()`: Lists all files in the data directory
   - `get_file()`: Retrieves file content

2. **AI Client** (`mcp_client.py`): 
   - Connects to the MCP server
   - Uses Ollama's qwen3:1.7b model with LangGraph's ReAct agent
   - Translates natural language to tool calls

3. **Data Flow**: User input → AI reasoning → Tool selection → MCP server → File system → Response back to user

## 🛠️ Customization

### Adding New Tools

Extend the MCP server by adding new tools:

```python
@mcp.tool()
def delete_file(name: str):
    """Delete a file from the storage directory."""
    # Your implementation here
```

### Changing AI Model

Modify the model in `mcp_client.py`:

```python
model = ChatOllama(model="llama3.2")  # Use different Ollama model
```

Or pull and use a different model:
```bash
ollama pull llama3.2
```

## 🐛 Troubleshooting

- **MCP server issues**: The MCP server starts automatically, but check the console output for any startup errors
- **Ollama installation problems**: Verify Ollama is properly installed and running with `ollama --version`
- **Model not found**: Ensure you've pulled the model with `ollama pull qwen3:1.7b`
- **Import errors**: Verify all dependencies are installed with `uv sync`

## 📦 Dependencies

- `langchain-mcp-adapters>=0.1.9` - MCP integration for LangChain
- `langchain-ollama>=0.3.6` - Ollama integration (future use)
- `langgraph>=0.5.4` - Agent framework
- `mcp[cli]>=1.12.2` - Model Context Protocol implementation

---

👨‍💻 **Behind the Code**

This project addresses a critical gap in enterprise AI adoption: **vendor lock-in and integration complexity**. While most companies are tied to specific AI providers, this demonstrates how the Model Context Protocol creates a universal standard for AI-tool communication.

**Business Value**: Instead of building separate integrations for Claude, ChatGPT, and other AI models, companies can build once using MCP and connect any AI provider. This reduces development costs, eliminates vendor dependency, and future-proofs AI infrastructure investments.

**More practical tech projects**: [@it_jagger](https://t.me/it_jagger)

## Donate:

ETH (Mainnet): 0x765885e6Cb9e40E1504F80272A7b5B60ffF7b92d  
USDT (SOL): GRNmdL1mpdBhgY8cFZggUo5k9eG5ic5QtA6NFTv6ZAbw
