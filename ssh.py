import paramiko

# Define the connection parameters
hostname = 'localhost'
port = 2222
username = 'root'
password = 'alpine'

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's SSH key (not recommended for production use)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    client.connect(hostname, port=port, username=username, password=password)
    print("Connected successfully")
    
    # Execute a command (optional)
    stdin, stdout, stderr = client.exec_command('uname -a')
    print("Output: ", stdout.read().decode())

finally:
    # Close the connection
    client.close()
    print("Connection closed")
