# IOS Ramdisk Tool

This repository contains tools to assist with various tasks related to iOS devices in DFU mode, including driver installation, ramdisk loading, port forwarding, and file transfer.

## Tools

### 1. pwndfu.py

This script installs the libusbK driver for Apple DFU devices using Zadig.

#### Usage

Run the script to install the driver:
```bash
python pwndfu.py
```

### 2. ramdisk.py

This script sends a series of files and commands to an iOS device in DFU mode to load a ramdisk.

#### Prerequisites

- Ensure you have `pymobiledevice3` installed.

#### Usage

Place your required `.img4` files and other necessary files in the same directory as the script, then run:
```bash
python ramdisk.py
```

### 3. iproxy.py

This script forwards a local port to a remote port on an iOS device using `pymobiledevice3`.

#### Usage

Forward a port with optional background mode:
```bash
python iproxy.py <local_port> <remote_port> [-d]
```
Example:
```bash
python iproxy.py 2222 22 -d
```

### 4. scp.py

This script constructs an SCP command to transfer files from an iOS device to a specified local directory.

#### Usage

Run the script and follow the prompts:
```bash
python scp.py
```
You will be asked to provide a save path where the files will be copied.

## Dependencies

Ensure the following dependencies are installed:

- Python 3.x
- `pymobiledevice3`
- `zadig` (for Windows)

Install `pymobiledevice3` using pip:
```bash
pip install pymobiledevice3
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## Acknowledgements

- Thanks to the developers of `pymobiledevice3` for their invaluable library.

For any issues or questions, please open an issue on GitHub.