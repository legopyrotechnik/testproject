# good_source.py

def get_safe_command():
    """
    This is the good source. It returns a command from a hardcoded,
    pre-approved list. This data is considered safe and untainted.
    """
    # SOURCE: This is a hardcoded, trusted list of commands.
    ALLOWED_COMMANDS = [
        "ls -l",
        "echo 'Hello, Secure World!'"
    ]
    
    # The function always returns a value from this safe list.
    return ALLOWED_COMMANDS[0]
