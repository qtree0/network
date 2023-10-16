import socket
import threading
import tkinter as tk
from tkinter import Scrollbar, Text

# 서버 정보 입력
host = input("Enter server address: ")
name = input("Enter your name: ")
port = 2500

# 서버에 연결
s = socket.socket()
s.connect((host, port))

# GUI 창 설정
root = tk.Tk()
root.title("Chat Room")

chat_text = Text(root, width=40, height=10)
chat_text.pack(padx=10, pady=10)
chat_text.config(state=tk.DISABLED)

scrollbar = Scrollbar(root, command=chat_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=10)


def send_message(event=None):
    message = entry.get()
    entry.delete(0, tk.END)
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, f"You: {message}\n")
    chat_text.config(state=tk.DISABLED)

    s.send(message.encode())


root.bind('<Return>', send_message)


def receive_messages():
    while True:
        message = s.recv(1024).decode()
        chat_text.config(state=tk.NORMAL)
        chat_text.insert(tk.END, f"Friend: {message}\n")
        chat_text.config(state=tk.DISABLED)


receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# 클라이언트 이름 서버로 보내기
s.send(name.encode())

root.mainloop()