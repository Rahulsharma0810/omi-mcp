"""Pydantic models for Omi REST API."""

from typing import Any, Optional

from pydantic import BaseModel, Field


# Memory models
class Memory(BaseModel):
    """Memory model."""

    id: str
    content: str
    created_at: str
    updated_at: Optional[str] = None


class MemoryResponse(BaseModel):
    """Response when creating a memory."""

    id: str
    status: str
    discarded: bool


class MemoriesListResponse(BaseModel):
    """Response when listing memories."""

    memories: list[dict[str, Any]]
    total: int


# Conversation models
class Conversation(BaseModel):
    """Conversation model."""

    id: str
    title: str
    created_at: str
    discarded: bool


class ConversationResponse(BaseModel):
    """Response when creating a conversation (minimal)."""

    id: str
    status: str
    discarded: bool


class ConversationsListResponse(BaseModel):
    """Response when listing conversations."""

    conversations: list[dict[str, Any]]
    total: int


# Folder models
class Folder(BaseModel):
    """Folder model."""

    id: str
    name: str


class FoldersListResponse(BaseModel):
    """Response when listing folders."""

    folders: list[Folder]


# Action Item models
class ActionItem(BaseModel):
    """Action item model."""

    id: str
    content: str
    completed: bool
    due_date: Optional[str] = None
    created_at: str


class ActionItemResponse(BaseModel):
    """Response when creating an action item."""

    id: str
    status: str
    discarded: bool


class ActionItemsListResponse(BaseModel):
    """Response when listing action items."""

    action_items: list[dict[str, Any]]
    total: int


# API Key models
class ApiKey(BaseModel):
    """API key model."""

    id: str
    name: str
    created_at: str
    last_used: Optional[str] = None
    revoked: bool


class ApiKeyResponse(BaseModel):
    """Response when creating an API key."""

    api_key: str
    name: str


class ApiKeysListResponse(BaseModel):
    """Response when listing API keys."""

    api_keys: list[ApiKey]


# Request models
class CreateMemoryRequest(BaseModel):
    """Request model for creating a memory."""

    content: str = Field(..., description="Memory content")


class CreateMemoriesBatchRequest(BaseModel):
    """Request model for creating multiple memories."""

    contents: list[str] = Field(..., description="List of memory contents")


class UpdateMemoryRequest(BaseModel):
    """Request model for updating a memory."""

    content: str = Field(..., description="Updated memory content")


class CreateConversationRequest(BaseModel):
    """Request model for creating a conversation."""

    text: str = Field(..., description="Conversation text")


class CreateConversationFromSegmentsRequest(BaseModel):
    """Request model for creating a conversation from segments."""

    segments: list[dict[str, Any]] = Field(
        ..., description="List of transcript segments"
    )


class UpdateConversationRequest(BaseModel):
    """Request model for updating a conversation."""

    title: Optional[str] = Field(None, description="New conversation title")
    discarded: Optional[bool] = Field(None, description="Discarded status")


class CreateActionItemRequest(BaseModel):
    """Request model for creating an action item."""

    content: str = Field(..., description="Action item content")
    due_date: Optional[str] = Field(None, description="Due date (ISO 8601)")


class CreateActionItemsBatchRequest(BaseModel):
    """Request model for creating multiple action items."""

    items: list[dict[str, Any]] = Field(
        ..., description="List of action item objects"
    )


class UpdateActionItemRequest(BaseModel):
    """Request model for updating an action item."""

    content: Optional[str] = Field(None, description="Updated content")
    due_date: Optional[str] = Field(None, description="New due date")
    completed: Optional[bool] = Field(None, description="Completion status")


class CreateApiKeyRequest(BaseModel):
    """Request model for creating an API key."""

    name: str = Field(..., description="API key name")
    permissions: Optional[list[str]] = Field(
        None, description="List of permissions"
    )