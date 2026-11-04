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


# TEST ONLY: Intentional SAST vulnerabilities.
# Do not execute these functions.

def unsafe_eval(user_input: str):
    return eval(user_input)


def unsafe_shell_command(user_input: str):
    return subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True
    )


