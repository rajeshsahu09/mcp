import sys
import asyncio
from contextlib import AsyncExitStack
from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.client.stdio import stdio_client, StdioServerParameters

async def main():
    use_sse = len(sys.argv) > 1 and sys.argv[1] == "sse"

    # We use AsyncExitStack to easily manage the different async context managers
    async with AsyncExitStack() as stack:
        try:
            if use_sse:
                url = "http://localhost:8000/sse"
                print(f"Connecting to MCP server at {url} via SSE...")
                read_stream, write_stream = await stack.enter_async_context(sse_client(url))
            else:
                print("Connecting to MCP server via STDIO...")
                # Start the server as a subprocess
                server_params = StdioServerParameters(
                    command=sys.executable,
                    args=["server.py"]
                )
                read_stream, write_stream = await stack.enter_async_context(stdio_client(server_params))

            # Create the MCP session using the streams
            session = await stack.enter_async_context(ClientSession(read_stream, write_stream))
            
            # Initialize the connection with the server
            await session.initialize()
            print("Connected successfully!\n")

            # 1. Discover what tools the server has
            print("--- Available Tools ---")
            tools_result = await session.list_tools()
            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")
            print()

            # 2. Call a specific tool (calculate_sum)
            tool_name = "calculate_sum"
            tool_args = {"a": 10, "b": 25}
            
            print(f"--- Calling Tool: {tool_name} ---")
            print(f"Arguments: {tool_args}")
            
            result = await session.call_tool(tool_name, arguments=tool_args)
            
            # The result contains a list of contents
            print("Result:")
            for content in result.content:
                if content.type == "text":
                    print(f"  > {content.text}")
                    
        except Exception as e:
            print(f"Error: {e}")
            if use_sse:
                print("\nNote: Make sure your server is running!")
                print("You can run it in another terminal with: python server.py sse")
            else:
                print("\nNote: Make sure server.py is in the current directory.")

if __name__ == "__main__":
    asyncio.run(main())
