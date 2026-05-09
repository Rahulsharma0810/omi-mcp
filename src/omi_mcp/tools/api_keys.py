"""API Key MCP tools."""

from typing import Optional

from fastmcp import FastMCP

from omi_mcp.api_client import get_client

mcp = FastMCP("omi-mcp api-keys")


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