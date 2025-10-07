def check_age(age):
    if age < 18:
        raise ValueError("Age is less than 18, You're not allowed to vote")
    print(age)

from urllib import request, error
import socket
from pathlib import Path

from dotenv import load_dotenv

def fetch(url: str, timeout_sec: float = 3.0) -> str | None:
    try:
        with request.urlopen(url, timeout=timeout_sec) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except error.HTTPError as e:
        print(f"HTTP error {e.code} for {url}: {e.reason}")
    except error.URLError as e:
        # DNS failure, refused connection, etc.
        print(f"URL error for {url}: {e.reason}")
    except socket.timeout:
        print(f"Timeout after {timeout_sec}s for {url}")
    return None

class ConfigError(Exception):
    pass

def load_port_from_env() -> int:
    import os

    script_path = Path(__file__).resolve()
    env_path = script_path.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    raw = os.getenv("APP_PORT")  # e.g., "8080" or "oops"

    try:
        if raw is None:
            raise ValueError("APP_PORT missing")
        return int(raw)
    except (ValueError, TypeError) as e:
        # Attach original cause
        raise ConfigError("Invalid APP_PORT; expected integer") from e

def init_app() -> None:
    # We choose not to catch — let the caller decide
    port = load_port_from_env()
    print(f"Starting server on port {port}")

def main() -> None:
    try:
        init_app()
        print("App initialized.")
    except ConfigError as e:
        print(f"[FATAL] Failed to initialize: {e}")
        # Fail fast: don't continue in an invalid state


if __name__ == "__main__":
    print(fetch("https://example.invalid/resource"))
    main()