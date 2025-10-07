from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
def read_file(file_name):
    path = SCRIPT_DIR / file_name
    try:
        with path.open("r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"File not found: {path}")
        # Optionally: path.write_text("", encoding="utf-8")
    except PermissionError as e:
        print(f"Permission denied when reading {path}: {e}")
    except OSError as e:
        # Fallback for other I/O issues
        print(f"OS error for {path}: {e}")
    return None

if __name__ == "__main__":
    content = read_file("file-ede.txt")
    if content is None:
        print("Handled missing/failed read gracefully.")
    else:
        print(content)

