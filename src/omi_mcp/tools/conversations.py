"""Conversation MCP tools."""

from typing import Any, Optional

from fastmcp import FastMCP

from omi_mcp.api_client import get_client

mcp = FastMCP("omi-mcp conversations")


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
    """Create a conversation from text (minimal response).

    Args:
        text: The conversation text.

    Returns:
        Dictionary with created conversation details (id, status, discarded).
    """
    client = get_client()
    return client.create_conversation(text=text)


@mcp.tool()
def create_conversation_full(text: str) -> dict:
    """Create a conversation from text (full response).

    Args:
        text: The conversation text.

    Returns:
        Dictionary with full conversation object.
    """
    client = get_client()
    return client.create_conversation_full(text=text)


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