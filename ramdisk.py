import time
from pymobiledevice3.irecv import IRecv

# Initialize IRecv instance
irecv = IRecv()

# Define the files and commands to be sent in sequence
commands = [
    ('iBSS.img4', 'buffer'),  # Send iBSS.img4 as buffer
    (None, 'sleep', 1),       # Sleep for 1 second
    ('iBSS.img4', 'buffer'),  # Send iBSS.img4 as buffer again
    (None, 'sleep', 1),       # Sleep for 1 second
    ('iBEC.img4', 'buffer'),  # Send iBEC.img4 as buffer
    (None, 'sleep', 1),       # Sleep for 1 second
    ('go', 'command'),        # Send 'go' command
    (None, 'sleep', 1),       # Sleep for 1 second
    ('ramdisk', 'buffer'),    # Send ramdisk as buffer
    (None, 'sleep', 1),       # Sleep for 1 second
    ('ramdisk', 'command'),   # Send 'ramdisk' command
    (None, 'sleep', 1),       # Sleep for 1 second
    ('devicetree.img4', 'buffer'),  # Send devicetree.img4 as buffer
    (None, 'sleep', 1),       # Sleep for 1 second
    ('devicetree', 'command'),# Send 'devicetree' command
    (None, 'sleep', 1),       # Sleep for 1 second
    ('trustcache.img4', 'buffer'),  # Send trustcache.img4 as buffer
    (None, 'sleep', 1),       # Sleep for 1 second
    ('firmware', 'command'),  # Send 'firmware' command
    (None, 'sleep', 1),       # Sleep for 1 second
    ('kernelcache.img4', 'buffer'), # Send kernelcache.img4 as buffer
    (None, 'sleep', 1),       # Sleep for 1 second
    ('bootx', 'command')      # Send 'bootx' command
]

# Process each command in sequence
for item in commands:
    if item[1] == 'buffer':
        # Read and send the buffer file
        with open(item[0], 'rb') as f:
            irecv.send_buffer(f.read())
    elif item[1] == 'command':
        # Send the command
        irecv.send_command(item[0])
    elif item[1] == 'sleep':
        # Sleep for the specified duration
        time.sleep(item[2])

print("All commands executed successfully.")
