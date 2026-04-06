from dataclasses import dataclass

@dataclass
class ParsedQuery:
    """Represents structured query extracted from user input."""
    user: str
    intent: str