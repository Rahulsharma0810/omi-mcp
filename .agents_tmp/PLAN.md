# 1. OBJECTIVE

Create MCP server tools that wrap all methods of the Omi REST API (https://api.omi.me). The MCP server should provide tools for memories, conversations, folders, action items, and API keys management. Currently the codebase only has MCP tools for limited memory and conversation operations, not the full REST API.

# 2. CONTEXT SUMMARY

- **Base URL:** https://api.omi.me
- **Authentication:** Bearer token (API key prefixed with `omi_dev_`)
- **Rate Limits:** 100 requests/min, 10,000 requests/day
- Current implementation only has basic memory and conversation MCP tools, missing full REST API coverage

**Total REST API Endpoints (21):**
- Memories: 5 endpoints (list, create, create-batch, update, delete)
- Conversations: 7 endpoints (list, create, create_full, create_from_segments, get, update, delete)
- Folders: 1 endpoint (list)
- Action Items: 5 endpoints (list, create, create-batch, update, delete)
- API Keys: 3 endpoints (list, create, revoke)

# 3. APPROACH OVERVIEW

Create a Python MCP server that wraps the Omi REST API using the FastMCP framework. Each REST API endpoint becomes an MCP tool with proper parameter handling. Tools will be organized by resource type (memories, conversations, folders, action-items, api-keys). Include proper error handling for API errors (429 rate limit, 401 auth, 404 not found, etc.). The MCP server will use environment variable for API key authentication.

# 4. IMPLEMENTATION STEPS

## Step 1: Set up project structure and dependencies
- **Goal:** Create project skeleton and configuration files
- **Method:** Create pyproject.toml with required dependencies (fastmcp, httpx, pydantic, python-dotenv), create src/omi_mcp/ directory structure
- **Reference:** pyproject.toml, src/omi_mcp/__init__.py

## Step 2: Create API client and models
- **Goal:** HTTP client for Omi REST API and type definitions
- **Method:** Create api_client.py for HTTP requests with proper auth headers, Create models.py with Pydantic models for all request/response types
- **Reference:** src/omi_mcp/api_client.py, src/omi_mcp/models.py

## Step 3: Implement Memory tools (5 tools)
- **Goal:** Add 5 memory-related MCP tools
- **Method:** Implement get_memories, create_memory, create_memories_batch, update_memory, delete_memory
- **Reference:** src/omi_mcp/tools/memories.py

## Step 4: Implement Conversation tools (7 tools)
- **Goal:** Add 7 conversation-related MCP tools
- **Method:** 
  - get_conversations - List conversations with filters
  - create_conversation - Create from text, returns minimal response (id, status, discarded)
  - create_conversation_full - Create from text, returns full conversation object
  - create_conversation_from_segments - Create from transcript segments
  - get_conversation - Get single conversation by ID with optional transcript
  - update_conversation - Update title or discarded status
  - delete_conversation - Delete conversation by ID
- **Reference:** src/omi_mcp/tools/conversations.py

## Step 5: Implement Folder tools (1 tool)
- **Goal:** Add folder listing MCP tool
- **Method:** Implement get_folders
- **Reference:** src/omi_mcp/tools/folders.py

## Step 6: Implement Action Item tools (5 tools)
- **Goal:** Add 5 action item-related MCP tools
- **Method:** Implement get_action_items, create_action_item, create_action_items_batch, update_action_item, delete_action_item
- **Reference:** src/omi_mcp/tools/action_items.py

## Step 7: Implement API Key tools (3 tools)
- **Goal:** Add 3 API key management MCP tools
- **Method:** Implement get_api_keys, create_api_key, revoke_api_key
- **Reference:** src/omi_mcp/tools/api_keys.py

## Step 8: Create main MCP server entry point
- **Goal:** Register all tools and start MCP server
- **Method:** Create server.py that imports and registers all tools, configure MCP server with name "omi-mcp", version, and tool descriptions
- **Reference:** src/omi_mcp/server.py

## Step 9: Create configuration and .env.example
- **Goal:** Documentation for API key configuration
- **Method:** Create .env.example with OMI_API_KEY placeholder
- **Reference:** .env.example

# 5. TESTING AND VALIDATION

Verify all 21 tools are registered with the MCP server. Test authentication works with valid API key. Test each tool category returns expected responses. Verify error handling for invalid API key (401), rate limits (429), not found (404). Success: MCP server starts and all tools are callable via MCP protocol.
