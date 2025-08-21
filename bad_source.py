# bad_source.py

import sys

def get_tainted_command():
    """
    This is the bad source. It retrieves data from an untrusted source
    (command-line arguments) without any validation or sanitization.
    """
    # SOURCE: sys.argv is considered a source of tainted user input.
    if len(sys.argv) > 2:
        # The command is taken directly from the second command-line argument.
        command = sys.argv[2]
        return command
    else:
        # Default bad command if none is provided.
        return "echo 'No command provided, but this path is tainted.'"
