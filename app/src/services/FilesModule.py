import os;

class FilesModule:
    BASE_DIR = "/app/app/data"
    QUEUED_DIR = f"{BASE_DIR}/queued"
    DOING_DIR = f"{BASE_DIR}/doing"
    DONE_DIR = f"{BASE_DIR}/done"

    def __init__(self):
        # Ensure required directories exist
        os.makedirs(self.QUEUED_DIR, exist_ok=True)
        os.makedirs(self.DOING_DIR, exist_ok=True)
        os.makedirs(self.DONE_DIR, exist_ok=True)

    def print_directories(self):
        print("Directories:")
        print(f"QUEUED_DIR: {self.QUEUED_DIR}")
        print(f"DOING_DIR: {self.DOING_DIR}")
        print(f"DONE_DIR: {self.DONE_DIR}")
