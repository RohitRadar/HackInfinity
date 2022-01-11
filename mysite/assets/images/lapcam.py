import socket
import tqdm
import os
import argparse
import cv2
from time import sleep

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 64 

def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024*64)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the socket
    s.close()


host = "192.168.1.9"
port = 5001
filename = "pic.jpg"
while(1):
    vid = cv2.VideoCapture(0)
    ret,frame = vid.read()
    cv2.imwrite("pic.jpg",frame)
    #vid.release()
    send_file(filename, host, port)