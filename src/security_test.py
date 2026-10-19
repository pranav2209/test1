import subprocess


TEST_PASSWORD = "SecureLine-Test-Password-123"


def run_command(user_input: str):
    # TEST-ONLY intentionally insecure code for security scanner validation.
    return subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True,
    )
