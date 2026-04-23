import sys
from mcp.server.fastmcp import FastMCP
from tools import math_tools, text_tools

# Initialize the FastMCP server
# The name here will be used to identify your server
mcp = FastMCP("My First FastMCP Server")

# Register tools from different modules
math_tools.register(mcp)
text_tools.register(mcp)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "sse":
        print("Starting server on localhost:8000 with SSE transport...")
        mcp.run(transport="sse")
    else:
        # Default to stdio
        mcp.run()