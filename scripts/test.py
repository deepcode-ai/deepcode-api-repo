import subprocess
import sys

def run_tests():
    try:
        print("Running tests...")

        # Example: Run pytest to execute tests
        subprocess.check_call(["pytest", "tests"])

        print("All tests passed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Tests failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
