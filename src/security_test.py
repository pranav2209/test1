import shlex
import subprocess


TEST_PASSWORD = "SecureLine-Test-Password-123"


def run_command(user_input: str):
    # TEST-ONLY intentionally insecure code for security scanner validation.
    args = shlex.split(user_input)
    return subprocess.run(
        args,
        capture_output=True,
        text=True,
    )
