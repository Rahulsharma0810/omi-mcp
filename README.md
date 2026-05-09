# omi-mcp

Extended MCP tools for Omi REST API (https://api.omi.me).

## Features

This MCP server wraps all 21 endpoints of the Omi REST API:

- **Memories** (5 tools): list, create, create-batch, update, delete
- **Conversations** (7 tools): list, create, create_full, create_from_segments, get, update, delete
- **Folders** (1 tool): list
- **Action Items** (5 tools): list, create, create-batch, update, delete
- **API Keys** (3 tools): list, create, revoke

## Installation

```bash
pip install -e .
```

## Configuration

Copy `.env.example` to `.env` and set your Omi API key:

```bash
cp .env.example .env
# Edit .env and set OMI_API_KEY
```

Get your API key from https://omi.me

## Usage

### Running the MCP Server

```bash
# Set the API key
export OMI_API_KEY=omi_dev_your_key

# Run with stdio transport
python -m omi_mcp.server

# Or run with HTTP transport
MCP_HOST=0.0.0.0 MCP_PORT=8080 python -m omi_mcp.server
```

### Using with MCP Clients

The server provides the following tools:

#### Memories
- `get_memories` - List all memories
- `create_memory` - Create a new memory
- `create_memories_batch` - Create multiple memories
- `update_memory` - Update a memory
- `delete_memory` - Delete a memory

#### Conversations
- `get_conversations` - List all conversations
- `create_conversation` - Create a conversation (minimal response)
- `create_conversation_full` - Create a conversation (full response)
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
