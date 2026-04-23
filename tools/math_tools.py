from mcp.server.fastmcp import FastMCP

def register(mcp: FastMCP):
    # 1. A simple mathematical tool
    @mcp.tool()
    def calculate_sum(a: int, b: int) -> int:
        """Adds two integers together.
        
        Args:
            a: The first integer.
            b: The second integer.
        """
        return a + b

    # 3. A tool demonstrating lists
    @mcp.tool()
    def filter_even_numbers(numbers: list[int]) -> list[int]:
        """Filters a list of numbers, returning only the even ones.
        
        Args:
            numbers: A list of integers to filter.
        """
        return [num for num in numbers if num % 2 == 0]
