"""Action Item MCP tools."""

from typing import Any, Optional

from fastmcp import FastMCP

from omi_mcp.api_client import get_client

mcp = FastMCP("omi-mcp action-items")


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