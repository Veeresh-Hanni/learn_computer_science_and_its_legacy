from openai_client import OpenAIChatClient
from geminiai_client import GeminiAIChatClient

class ChatClient:
    """
    Unified wrapper for OpenAIChatClient or GeminiAIChatClient.
    Provides:
    - complete(): returns full text
    - complete_stream(): yields text chunks (if supported)
    """

    def __init__(self, client: OpenAIChatClient | GeminiAIChatClient):
        self._client = client

    def complete(self, prompt: str, max_tokens: int = 200) -> str:
        """
        Return full text from the AI client.
        Works for OpenAI or Gemini.
        """
        if hasattr(self._client, "complete"):
            return self._client.complete(prompt, max_tokens=max_tokens)
        else:
            raise NotImplementedError("Client does not implement complete()")

    def complete_stream(self, prompt: str, max_tokens: int = 200):
        """
        Stream text if supported.
        Yields chunks.
        """
        if hasattr(self._client, "complete_stream"):
            yield from self._client.complete_stream(prompt, max_tokens=max_tokens)
        else:
            # Fallback: return full text as single chunk
            yield self.complete(prompt, max_tokens=max_tokens)
