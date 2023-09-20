import subprocess

# Load allowed MAC addresses from file
with open('allowed_macs.txt', 'r') as f:
    allowed_macs = [line.strip() for line in f.readlines()]

def get_connected_macs():
    """Retrieve the MAC addresses of connected devices."""
    cmd = "iw dev wlan0 station dump | grep Station | awk '{print $2}'"
    result = subprocess.check_output(cmd, shell=True).decode('utf-8')
    return result.splitlines()

def disconnect_unallowed_macs(connected_macs):
    """Disconnect devices that are not in the allowed list."""
    for mac in connected_macs:
        if mac not in allowed_macs:
            print(f"Disconnecting unauthorized device: {mac}")
            cmd = f"iw dev wlan0 station del {mac}"
            subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    connected_macs = get_connected_macs()
    disconnect_unallowed_macs(connected_macs)
