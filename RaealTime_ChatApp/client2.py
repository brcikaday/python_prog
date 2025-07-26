import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = '172.20.10.13'
PORT = 5050

username= ""
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def addMessage(message):
    messageArea.config(state="normal")
    messageArea.insert(tk.END, message + '\n')
    # messageArea.config(state="disabled")


def connect():
    global username
    username = username_text.get()
    client.connect((HOST,PORT))

    client.send(username.encode('utf-8'))
    username_text.config(state="disabled")
    username_button.config(state="disabled")

    threading.Thread(target=receive ).start()

def receive():
    while True:
        try:
            
            message = client.recv(2048).decode('utf-8')
            addMessage(message)
        except:
            addMessage("an error occured")
            client.close()
            break


def sendMessage():
    global username

    message = messagebox.get()

    if message.lower() == 'exit':
        client.send('!exit'.encode('utf-8'))  # signal to server
    else:
        client.send(f'{username}: {message}'.encode('utf-8'))
    
    messagebox.delete(0, tk.END)



darkgrey = "#121212"
medgrey = "#1F1B24"
oceanblue = "#464E88"
font = ("Helvetica", 17)
btfont = ("Helvetica", 14)
smallfont = ("Helvetica", 13)

home = tk.Tk()
home.title("Messenger")
home.geometry("600x600")
home.resizable(False,False)

home.grid_rowconfigure(0, weight=1)
home.grid_rowconfigure(1, weight=4)
home.grid_rowconfigure(2, weight=1)


top_frame = tk.Frame(home, width=600, height=100 , bg=darkgrey)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(home, width=600, height=400 , bg = medgrey )
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(home, width=600, height=100 , bg=darkgrey)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame,text="Enter username " , font = font, bg= darkgrey , fg= "white")
username_label.pack(side=tk.LEFT , padx=10)

username_text = tk.Entry(top_frame, font=font, bg= medgrey , fg="white" , width=25)
username_text.pack(side= tk.LEFT)

username_button = tk.Button(top_frame, text="Join" ,font= btfont, bg = oceanblue, fg="white" , command= connect)
username_button.pack(side=tk.LEFT, padx=15 ) 

messagebox = tk.Entry(bottom_frame, font=font, bg= medgrey , fg="white" , width=38)
messagebox.pack(side="left", padx=10)

message_button = tk.Button(bottom_frame, text="send" ,font= btfont, bg = oceanblue, fg="white" , command= sendMessage)
message_button.pack(side=tk.LEFT, padx=5)

messageArea = scrolledtext.ScrolledText(middle_frame, font = smallfont , bg= medgrey, fg="white", width = 67, height = 26.5)
messageArea.config(state=tk.DISABLED)
messageArea.pack(side="top") 



# HOST = '127.0.0.1'
# PORT = 5050

# username  = input('enter username: ')
# client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST,PORT))

# client.send(username.encode('utf-8'))



# def write():
#     while True:
#         message = input()

#         if message.lower() == 'exit':
#             client.send('!exit'.encode('utf-8'))  # signal to server
#             break
#         else:
#             client.send(f'{username}: {message}'.encode('utf-8'))



# write_thread = threading.Thread(target=sendMessage).start()

home.mainloop()