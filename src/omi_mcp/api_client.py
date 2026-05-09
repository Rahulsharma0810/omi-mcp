"""API client for Omi REST API."""

import os
from typing import Any, Optional

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.omi.me/v1/dev/user"
DEFAULT_TIMEOUT = 30.0


class OmiApiClient:
    """Client for Omi REST API."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize client with API key.

        Args:
            api_key: Omi API key. Falls back to OMI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("OMI_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set OMI_API_KEY environment variable.")
        self.base_url = BASE_URL
        self.timeout = DEFAULT_TIMEOUT

    def _headers(self) -> dict[str, str]:
        """Get headers with authentication."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict[str, Any]:
        """Make HTTP request to API."""
        url = f"{self.base_url}{endpoint}"
        with httpx.Client(timeout=self.timeout) as client:
            response = client.request(
                method=method,
                url=url,
                headers=self._headers(),
                params=params,
                json=json,
            )
            response.raise_for_status()
            return response.json()

    # Memories endpoints
    def get_memories(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> dict[str, Any]:
        """List memories."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._request("GET", "/user/memories", params=params)

    def create_memory(self, content: str) -> dict[str, Any]:
        """Create a single memory."""
        return self._request("POST", "/memories", json={"content": content})

    def create_memories_batch(self, contents: list[str]) -> dict[str, Any]:
        """Create multiple memories."""
        return self._request("POST", "/memories/batch", json={"contents": contents})

    def update_memory(self, memory_id: str, content: str) -> dict[str, Any]:
        """Update a memory."""
        return self._request(
            "PATCH", f"/memories/{memory_id}", json={"content": content}
        )

    def delete_memory(self, memory_id: str) -> dict[str, Any]:
        """Delete a memory."""
        return self._request("DELETE", f"/memories/{memory_id}")

    # Conversations endpoints
    def get_conversations(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        folder_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """List conversations."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if folder_id is not None:
            params["folder_id"] = folder_id
        return self._request("GET", "/conversations", params=params)

    def create_conversation(self, text: str) -> dict[str, Any]:
        """Create a conversation from text.

        Returns: Full conversation object from Omi.
        """
        return self._request("POST", "/conversations/full", json={"text": text})

    def create_conversation_from_segments(
        self,
        segments: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Create a conversation from transcript segments."""
        return self._request(
            "POST", "/conversations/from_segments", json={"segments": segments}
        )

    def get_conversation(
        self,
        conversation_id: str,
        transcript: Optional[bool] = None,
    ) -> dict[str, Any]:
        """Get a conversation by ID."""
        params = {}
        if transcript is not None:
            params["transcript"] = transcript
        return self._request("GET", f"/conversations/{conversation_id}", params=params)

    def update_conversation(
        self,
        conversation_id: str,
        title: Optional[str] = None,
        discarded: Optional[bool] = None,
    ) -> dict[str, Any]:
        """Update a conversation."""
        json = {}
        if title is not None:
            json["title"] = title
        if discarded is not None:
            json["discarded"] = discarded
        return self._request("PATCH", f"/conversations/{conversation_id}", json=json)

    def delete_conversation(self, conversation_id: str) -> dict[str, Any]:
        """Delete a conversation."""
        return self._request("DELETE", f"/conversations/{conversation_id}")

    # Folders endpoints
    def get_folders(self) -> dict[str, Any]:
        """List folders."""
        return self._request("GET", "/folders")

    # Action Items endpoints
    def get_action_items(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> dict[str, Any]:
        """List action items."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._request("GET", "/action-items", params=params)

    def create_action_item(
        self,
        content: str,
        due_date: Optional[str] = None,
    ) -> dict[str, Any]:
        """Create an action item."""
        json = {"content": content}
        if due_date is not None:
            json["due_date"] = due_date
        return self._request("POST", "/action-items", json=json)

    def create_action_items_batch(
        self,
        items: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Create multiple action items."""
        return self._request("POST", "/action-items/batch", json={"items": items})

    def update_action_item(
        self,
        action_item_id: str,
        content: Optional[str] = None,
        due_date: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> dict[str, Any]:
        """Update an action item."""
        json = {}
        if content is not None:
            json["content"] = content
        if due_date is not None:
            json["due_date"] = due_date
        if completed is not None:
            json["completed"] = completed
        return self._request(
            "PATCH", f"/action-items/{action_item_id}", json=json
        )

    def delete_action_item(self, action_item_id: str) -> dict[str, Any]:
        """Delete an action item."""
        return self._request("DELETE", f"/action-items/{action_item_id}")

    # API Keys endpoints
    def get_api_keys(self) -> dict[str, Any]:
        """List API keys."""
        return self._request("GET", "/api-keys")

    def create_api_key(
        self,
        name: str,
        permissions: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """Create an API key."""
        json = {"name": name}
        if permissions is not None:
            json["permissions"] = permissions
        return self._request("POST", "/api-keys", json=json)

    def revoke_api_key(self, api_key_id: str) -> dict[str, Any]:
        """Revoke an API key."""
        return self._request("DELETE", f"/api-keys/{api_key_id}")


def get_client(api_key: Optional[str] = None) -> OmiApiClient:
    """Get Omi API client instance."""
    return OmiApiClient(api_key=api_key)