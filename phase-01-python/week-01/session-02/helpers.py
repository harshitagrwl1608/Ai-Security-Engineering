
def clean_username(username):
    """Remove surrounding whitespace and convert a username to lowercase."""
    return username.strip().lower()


def format_event(event_type, source_ip, username):
    """Return a readable security event message."""
    return f"{event_type} | Source: {source_ip} | User: {username}"


def failed_login_threshold_exceeded(failed_attempts, threshold=5):
    """Return True when failed attempts are greater than the threshold."""
    return failed_attempts > threshold
