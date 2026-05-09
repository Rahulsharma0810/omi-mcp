"""Folder MCP tools."""

from fastmcp import FastMCP

from omi_mcp.api_client import get_client

mcp = FastMCP("omi-mcp folders")


@mcp.tool()
def get_folders() -> dict:
    """List all folders.

    Returns:
        Dictionary with folders list.
    """
    client = get_client()
    return client.get_folders()