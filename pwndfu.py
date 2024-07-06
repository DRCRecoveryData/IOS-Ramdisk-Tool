import subprocess
import sys

def install_libusbk_driver():
    # Define the Apple DFU Device ID (Product ID)
    device_id = "1227"
    
    try:
        # Run zadig.exe with command line parameters to install libusbK driver
        subprocess.run(["zadig.exe", "--device", device_id, "--instlib", "libusbK", "--force_install"], check=True)
        print("libusbK driver installed successfully for DFU Mode.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install libusbK driver: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_libusbk_driver()
