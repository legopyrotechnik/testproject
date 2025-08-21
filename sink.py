# sink.py

import subprocess
import sys

# Import the source functions from the other files
from good_source import get_safe_command
from bad_source import get_tainted_command

def execute_command(command_string):
    """
    This is the sink. It executes a command string using a shell.
    A SAST scanner should identify the call to subprocess.run with shell=True
    as a potential vulnerability.
    """
    print(f"Executing command: {command_string}")
    try:
        # SINK: This line is vulnerable if command_string is user-controlled.
        subprocess.run(command_string, shell=True, check=True, capture_output=True, text=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Stderr: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ["good", "bad"]:
        print("Usage: python sink.py [good|bad]")
        sys.exit(1)

    if sys.argv[1] == "good":
        # This path uses a safe, hardcoded source.
        # A SAST scanner should NOT flag this data flow.
        safe_cmd = get_safe_command()
        execute_command(safe_cmd)
    
    elif sys.argv[1] == "bad":
        # This path uses a tainted source from user input.
        # A SAST scanner SHOULD flag this data flow as a command injection vulnerability.
        tainted_cmd = get_tainted_command()
        execute_command(tainted_cmd)
