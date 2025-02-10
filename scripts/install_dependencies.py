import subprocess
import sys

def install_dependencies():
    try:
        print("Installing dependencies...")

        # Example: Install dependencies using pip (adjust for your needs)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Dependency installation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
