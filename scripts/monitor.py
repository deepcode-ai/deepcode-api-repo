import subprocess

def monitor_services():
    try:
        print("Checking service status...")

        # Example: Check if a service is running (replace 'your-service' with actual service name)
        subprocess.check_call(["systemctl", "is-active", "--quiet", "your-service"])

        print("Service is running.")
    except subprocess.CalledProcessError:
        print("Service is not running.")

if __name__ == "__main__":
    monitor_services()
