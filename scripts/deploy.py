import subprocess
import sys

def deploy():
    try:
        print("Starting deployment...")

        # Example: Deploy to server (replace with your actual deployment steps)
        subprocess.check_call(["scp", "-r", "./build", "user@your-server:/path/to/deployment"])

        print("Deployment completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deploy()
