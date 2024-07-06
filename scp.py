import os

def get_save_path():
    # Prompt the user for a save path
    save_path = input("Enter the save path: ")
    
    # Ensure the save path is a valid directory
    if not os.path.isdir(save_path):
        print(f"Error: {save_path} is not a valid directory.")
        return None
    
    return save_path

def construct_scp_command(save_path):
    # Construct the SCP command
    scp_command = f"scp -r -P 2222 root@localhost:/* {save_path}"
    return scp_command

if __name__ == "__main__":
    save_path = get_save_path()
    
    if save_path:
        scp_command = construct_scp_command(save_path)
        print(f"SCP Command: {scp_command}")
