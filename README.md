# omi-mcp

Extended MCP tools for Omi REST API (https://api.omi.me).

## Why This MCP?

Omi already provides an [official MCP server](https://docs.omi.me/doc/developer/mcp/introduction) for AI assistants. This project provides an **alternative** with additional capabilities:

| Feature | Official Omi MCP | This MCP Server |
|---------|-----------------|---------------|
| **Memories** | 5 tools | 5 tools |
| **Conversations** | 3 tools | 6 tools |
| **Folders** | ❌ | ✅ List folders |
| **Action Items** | ❌ | ✅ Full CRUD |
| **API Keys** | ❌ | ✅ Manage keys |
| **Transport** | SSE | STDIO |

### What This MCP Adds

- **Full Conversation Management**: Create, update, delete conversations
- **Action Items**: Complete task/todo management (CRUD)
- **Folders**: List and organize folders
- **API Key Management**: Create and revoke API keys programmatically
- **STDIO Transport**: Works with Claude Desktop, Cursor, and all MCP clients

## Features

This MCP server wraps the Omi REST API endpoints:

- **Memories** (5 tools): list, create, create-batch, update, delete
- **Conversations** (6 tools): list, create, create_from_segments, get, update, delete
- **Folders** (1 tool): list
- **Action Items** (5 tools): list, create, create-batch, update, delete
- **API Keys** (3 tools): list, create, revoke

## Installation

### Using uvx (recommended)

```bash
uvx omi-mcp
```

### Using pip

```bash
pip install omi-mcp
```

### Development

```bash
pip install -e ".[dev]"
```

## Configuration

### Authentication

Set one of these environment variables before starting the MCP server:

```
OMI_AUTHORIZATION_HEADER="Authorization: Bearer omi_mcp_XXXXX"
# or
AUTHORIZATION="Bearer omi_mcp_XXXXX"
# or
OMI_API_KEY="omi_mcp_XXXXX"
```

## Usage

### Running the MCP Server

```bash
# Run with stdio transport (for MCP clients)
python -m omi_mcp.server
```

### Claude Desktop MCP Config

Add to your Claude MCP settings (`claude_mcp.json`):

```json
{
  "mcpServers": {
    "omi-mcp": {
      "command": "uvx",
      "args": ["omi-mcp"]
    }
  }
}
```

**Note**: `configure_api_key` is removed. Configure auth via environment variables only.

### Available Tools

#### Memories
- `get_memories` - List all memories
- `create_memory` - Create a new memory
- `create_memories_batch` - Create multiple memories
- `update_memory` - Update a memory
- `delete_memory` - Delete a memory

#### Conversations
- `get_conversations` - List all conversations
- `create_conversation` - Create a conversation
- `create_conversation_from_segments` - Create from transcript segments
- `get_conversation` - Get a conversation by ID
- `update_conversation` - Update a conversation
- `delete_conversation` - Delete a conversation

#### Folders
- `get_folders` - List all folders

#### Action Items
- `get_action_items` - List all action items
- `create_action_item` - Create a new action item
- `create_action_items_batch` - Create multiple action items
- `update_action_item` - Update an action item
- `delete_action_item` - Delete an action item

#### API Keys
- `get_api_keys` - List all API keys
- `create_api_key` - Create a new API key
- `revoke_api_key` - Revoke an API key

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```
