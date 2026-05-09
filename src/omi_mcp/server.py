"""Main MCP server for Omi REST API."""

from typing import Any, Optional

from fastmcp import FastMCP

from omi_mcp.api_client import get_client

# Create single MCP server
mcp = FastMCP("omi-mcp")

# =============================================================================
# Memory Tools
# =============================================================================


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


# =============================================================================
# Conversation Tools
# =============================================================================


@mcp.tool()
def get_conversations(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    folder_id: Optional[str] = None,
) -> dict:
    """List all conversations.

    Args:
        limit: Maximum number of conversations to return.
        offset: Number of conversations to skip for pagination.
        folder_id: Filter by folder ID.

    Returns:
        Dictionary with conversations list and total count.
    """
    client = get_client()
    return client.get_conversations(limit=limit, offset=offset, folder_id=folder_id)


@mcp.tool()
def create_conversation(text: str) -> dict:
    """Create a conversation from text.

    Args:
        text: The conversation text.

    Returns:
        Dictionary with created conversation details from Omi.
    """
    client = get_client()
    return client.create_conversation(text=text)


@mcp.tool()
def create_conversation_from_segments(segments: list[dict[str, Any]]) -> dict:
    """Create a conversation from transcript segments.

    Args:
        segments: List of transcript segments with speaker and text.

    Returns:
        Dictionary with created conversation details.
    """
    client = get_client()
    return client.create_conversation_from_segments(segments=segments)


@mcp.tool()
def get_conversation(conversation_id: str, transcript: Optional[bool] = None) -> dict:
    """Get a conversation by ID.

    Args:
        conversation_id: The ID of the conversation.
        transcript: Whether to include transcript in response.

    Returns:
        Dictionary with conversation details.
    """
    client = get_client()
    return client.get_conversation(conversation_id=conversation_id, transcript=transcript)


@mcp.tool()
def update_conversation(
    conversation_id: str,
    title: Optional[str] = None,
    discarded: Optional[bool] = None,
) -> dict:
    """Update a conversation.

    Args:
        conversation_id: The ID of the conversation to update.
        title: New title for the conversation.
        discarded: Updated discarded status.

    Returns:
        Dictionary with updated conversation details.
    """
    client = get_client()
    return client.update_conversation(
        conversation_id=conversation_id,
        title=title,
        discarded=discarded,
    )


@mcp.tool()
def delete_conversation(conversation_id: str) -> dict:
    """Delete a conversation.

    Args:
        conversation_id: The ID of the conversation to delete.

    Returns:
        Dictionary with deletion status.
    """
    client = get_client()
    return client.delete_conversation(conversation_id=conversation_id)


# =============================================================================
# Folder Tools
# =============================================================================


@mcp.tool()
def get_folders() -> dict:
    """List all folders.

    Returns:
        Dictionary with folders list.
    """
    client = get_client()
    return client.get_folders()


# =============================================================================
# Action Item Tools
# =============================================================================


@mcp.tool()
def get_action_items(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> dict:
    """List all action items.

    Args:
        limit: Maximum number of action items to return.
        offset: Number of action items to skip for pagination.

    Returns:
        Dictionary with action_items list and total count.
    """
    client = get_client()
    return client.get_action_items(limit=limit, offset=offset)


@mcp.tool()
def create_action_item(content: str, due_date: Optional[str] = None) -> dict:
    """Create a new action item.

    Args:
        content: The content of the action item.
        due_date: Due date in ISO 8601 format.

    Returns:
        Dictionary with created action item details.
    """
    client = get_client()
    return client.create_action_item(content=content, due_date=due_date)


@mcp.tool()
def create_action_items_batch(items: list[dict[str, Any]]) -> dict:
    """Create multiple action items in batch.

    Args:
        items: List of action item objects with content and optional due_date.

    Returns:
        Dictionary with created action items details.
    """
    client = get_client()
    return client.create_action_items_batch(items=items)


@mcp.tool()
def update_action_item(
    action_item_id: str,
    content: Optional[str] = None,
    due_date: Optional[str] = None,
    completed: Optional[bool] = None,
) -> dict:
    """Update an action item.

    Args:
        action_item_id: The ID of the action item to update.
        content: Updated content.
        due_date: Updated due date.
        completed: Updated completion status.

    Returns:
        Dictionary with updated action item details.
    """
    client = get_client()
    return client.update_action_item(
        action_item_id=action_item_id,
        content=content,
        due_date=due_date,
        completed=completed,
    )


@mcp.tool()
def delete_action_item(action_item_id: str) -> dict:
    """Delete an action item.

    Args:
        action_item_id: The ID of the action item to delete.

    Returns:
        Dictionary with deletion status.
    """
    client = get_client()
    return client.delete_action_item(action_item_id=action_item_id)


# =============================================================================
# API Key Tools
# =============================================================================


@mcp.tool()
def get_api_keys() -> dict:
    """List all API keys.

    Returns:
        Dictionary with API keys list.
    """
    client = get_client()
    return client.get_api_keys()


@mcp.tool()
def create_api_key(name: str, permissions: Optional[list[str]] = None) -> dict:
    """Create a new API key.

    Args:
        name: Name for the API key.
        permissions: List of permissions for the key.

    Returns:
        Dictionary with created API key details (includes the actual key).
    """
    client = get_client()
    return client.create_api_key(name=name, permissions=permissions)


@mcp.tool()
def revoke_api_key(api_key_id: str) -> dict:
    """Revoke an API key.

    Args:
        api_key_id: The ID of the API key to revoke.

    Returns:
        Dictionary with revocation status.
    """
    client = get_client()
    return client.revoke_api_key(api_key_id=api_key_id)


# Run the server
if __name__ == "__main__":
    main()


def main():
    """Entry point for the MCP server."""
    import os

    # Run the server with stdio transport
    mcp.run(transport="stdio")