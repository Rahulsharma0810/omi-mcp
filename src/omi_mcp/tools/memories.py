"""Memory MCP tools."""

from typing import Optional

from fastmcp import FastMCP

from omi_mcp.api_client import get_client

mcp = FastMCP("omi-mcp memories")


@mcp.tool()
def get_memories(limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
    """List all memories.

    Args:
        limit: Maximum number of memories to return.
        offset: Number of memories to skip for pagination.

    Returns:
        Dictionary with memories list and total count.
    """
    client = get_client()
    return client.get_memories(limit=limit, offset=offset)


@mcp.tool()
def create_memory(content: str) -> dict:
    """Create a new memory.

    Args:
        content: The content of the memory to create.

    Returns:
        Dictionary with created memory details (id, status, discarded).
    """
    client = get_client()
    return client.create_memory(content=content)


@mcp.tool()
def create_memories_batch(contents: list[str]) -> dict:
    """Create multiple memories in batch.

    Args:
        contents: List of memory contents to create.

    Returns:
        Dictionary with created memories details.
    """
    client = get_client()
    return client.create_memories_batch(contents=contents)


@mcp.tool()
def update_memory(memory_id: str, content: str) -> dict:
    """Update an existing memory.

    Args:
        memory_id: The ID of the memory to update.
        content: The new content for the memory.

    Returns:
        Dictionary with updated memory details.
    """
    client = get_client()
    return client.update_memory(memory_id=memory_id, content=content)


@mcp.tool()
def delete_memory(memory_id: str) -> dict:
    """Delete a memory.

    Args:
        memory_id: The ID of the memory to delete.

    Returns:
        Dictionary with deletion status.
    """
    client = get_client()
    return client.delete_memory(memory_id=memory_id)