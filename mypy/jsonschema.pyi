from typing import Any

def validate(instance: Any, schema: Any) -> None: ...

class ValidationError(Exception): ...