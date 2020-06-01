from pathlib import Path


def find_root(start: Path = Path(".")) -> Path:
    absolute_location = start.resolve()
    if (absolute_location / ".git").is_dir():
        return absolute_location
    else:
        return find_root(absolute_location / "..")


ROOT = find_root()
