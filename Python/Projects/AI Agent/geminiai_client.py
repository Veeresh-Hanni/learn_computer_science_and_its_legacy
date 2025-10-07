
import os
import google.generativeai as genai


class GeminiAIChatClient:
    """
    Simple wrapper around Google Gemini API for chat-style completions.
    """

    def __init__(self, model: str = "gemini-1.5-flash"):
        """
        Initializes the Gemini client.
        It auto-reads the GEMINI_API_KEY from environment variables.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("Missing GEMINI_API_KEY environment variable.")

        # Configure Gemini client
        genai.configure(
            api_key=api_key,
            client_options={"api_endpoint": "https://generativelanguage.googleapis.com/v1"}
        )

        self._model = model
        self._client = genai.GenerativeModel(model)

    def complete(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Send a text prompt to Gemini and return the generated text response.
        Raises RuntimeError on failure.
        """
        try:
            response = self._client.generate_content(
                prompt,
                generation_config={"max_output_tokens": max_tokens}
            )

            # Extract text
            text = getattr(response, "text", None)
            if not text:
                raise RuntimeError("Gemini API response was empty.")

            return text

        except Exception as ex:
            raise RuntimeError(
                "Failed to get response from Gemini API. "
                "Check GEMINI_API_KEY, model name, and network connectivity."
            ) from ex

    def chat(self):
        """
        Start an interactive chat session with Gemini.
        """
        print(f"🧠 Gemini Chat started — Model: {self._model}")
        chat = self._client.start_chat()

        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in {"exit", "quit"}:
                print("👋 Ending chat session.")
                break

            try:
                response = chat.send_message(user_input)
                print("Gemini:", response.text)
            except Exception as e:
                print("⚠️ Error:", e)
    def complete_stream(self, prompt: str, max_tokens: int = 200):
        """
        Stream partial responses from Gemini API.
        Yields text chunks as they arrive.
        """
        try:
            stream = self._client.generate_content_stream(
                model=self._model,
                contents=prompt
            )
            for chunk in stream:
                if chunk.text:
                    yield chunk.text
        except Exception as ex:
            raise RuntimeError(f"Streaming failed: {ex}")

# --------------------------
# 💡 Example usage
# --------------------------
if __name__ == "__main__":
    gemini = GeminiAIChatClient(model="gemini-2.5-pro")

    # One-shot completion
    print("\n=== One-shot completion ===")
    output = gemini.complete("Explain difference between TCP and UDP in 2 lines.")
    print("Response:", output)

    # Start chat (interactive)
    # gemini.chat()
