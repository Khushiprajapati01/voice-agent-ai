def clean_text(text: str) -> str:
    """Remove extra whitespace and normalize text."""
    return " ".join(text.split())

def is_silent(text: str) -> bool:
    """Check if transcription result is empty or noise."""
    return not text or len(text.strip()) < 2
