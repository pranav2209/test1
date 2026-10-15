import subprocess
import shlex

TEST_PASSWORD = "SecureLine-Test-Password-123"


def run_command(user_input: str):
    # TEST-ONLY intentionally insecure code for security scanner validation.
    return subprocess.run(
        shlex.split(user_input),
        capture_output=True,
        text=True,
    )
