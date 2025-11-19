import deleteU
import zmq
import json
import sign_in
import sign_up

def JDump(data):
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

#initilises the socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

#read JSON Database's data
with open('data.json', 'r') as file:
        data = json.load(file)



while True:
    #  Wait for next request from client
    message = socket.recv()

    #changes the recieved JSON to normal data
    message = json.loads(message)
    print(message)

    if message[0] == 1:
          # Sign-in
          print("signin")
          retMessage = sign_in.sign_in(message[1], message[2], data) #Sends the username and password
          socket.send_string(retMessage)
          JDump(data)
    elif message[0] == 2:
          #Sign-up
          print("Signup")
          retMessage = sign_up.sign_up(message[1], message[2], data)#Sends the username and password
          socket.send_string(retMessage)
          JDump(data)
    elif message[0] == 3:
          #Delete User
          retMessage = deleteU.delete_user(message[1], data)
          socket.send_string(retMessage)
          JDump(data)

