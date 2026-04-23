# Python FastMCP Server

This is a Python-based Model Context Protocol (MCP) server built using the `FastMCP` framework. It demonstrates how to create, modularize, and interact with an MCP server using both Server-Sent Events (SSE) and STDIO transport mechanisms.

## Project Structure

- `server.py`: The main entry point for the MCP server. It initializes the `FastMCP` instance and registers tools from the `tools` package.
- `client.py`: An automated Python client that connects to the server and tests the available tools. It connects using the STDIO transport by default and runs the server as a background subprocess.
- `tools/`: A package containing the modularized MCP tools.
  - `math_tools.py`: Contains mathematical tools like `calculate_sum` and `filter_even_numbers`.
  - `text_tools.py`: Contains text processing tools like `analyze_text`.
- `requirements.txt`: Python dependencies required for this project.

## Setup

1. Ensure you have Python installed.
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

### Running the Client (STDIO Mode)

The simplest way to test the project is to run the client. In STDIO mode, the client will automatically start `server.py` in the background, discover the available tools, and execute a sample tool call (`calculate_sum`).

```bash
python client.py
```

### Running the Server (SSE Mode)

If you wish to communicate over a network, you can run the server in Server-Sent Events (SSE) mode:

1. Start the server in a terminal:
   ```bash
   python server.py sse
   ```
2. Open a second terminal and run the client in SSE mode:
   ```bash
   python client.py sse
   ```

## VS Code Integration

This server is fully compatible with **Cline VS Code**. To use it, you can add it to your `config.json`:

```json
{
  "mcpServers": {
    "my-python-server": {
      "command": "path\\to\\your\\venv\\Scripts\\python.exe",
      "args": [
        "path\\to\\your\\server.py"
      ]
    }
  }
}
```
*(Make sure to use absolute paths to your python executable and server.py file).*
