import subprocess
import sys

def build():
    try:
        print("Starting build process...")

        # Example: Run build commands (adjust as needed)
        subprocess.check_call(["make", "build"])

        print("Build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build()
