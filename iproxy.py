import argparse
import subprocess

def forward_port(port1, port2, background):
    command = ["pymobiledevice3", "usbmux", "forward", str(port1), str(port2)]
    if background:
        command.append("-d")
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Port forwarding successful.")
    else:
        print("Port forwarding failed.")
        print(result.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Forward ports using pymobiledevice3 with optional background mode.')
    parser.add_argument('port1', type=int, help='Local port to forward from')
    parser.add_argument('port2', type=int, help='Remote port to forward to')
    parser.add_argument('-d', '--background', action='store_true', help='Run in background mode')

    args = parser.parse_args()
    
    forward_port(args.port1, args.port2, args.background)
