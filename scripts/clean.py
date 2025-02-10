import os
import shutil

def clean():
    try:
        print("Cleaning up build artifacts...")

        # Example: Delete build directories, logs, etc.
        if os.path.exists("build"):
            shutil.rmtree("build")
        if os.path.exists("dist"):
            shutil.rmtree("dist")
        if os.path.exists("*.log"):
            for log_file in os.listdir("."):
                if log_file.endswith(".log"):
                    os.remove(log_file)

        print("Cleanup completed successfully.")
    except Exception as e:
        print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    clean()
