#sender.py
from vidstream import ScreenShareClient
import threading
# Give IP address of target laptop to which screen sharing is to be shared
sender = ScreenShareClient('192.168.150.29', 9999)

t = threading.Thread(target=sender.start_stream) 
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()
