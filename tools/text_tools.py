from mcp.server.fastmcp import FastMCP

def register(mcp: FastMCP):
    # 2. A tool demonstrating slightly more complex types
    @mcp.tool()
    def analyze_text(text: str) -> dict:
        """Analyzes a given text and returns basic statistics.
        
        Args:
            text: The string to analyze.
        """
        words = text.split()
        return {
            "character_count": len(text),
            "word_count": len(words),
            "longest_word": max(words, key=len) if words else ""
        }
