import zmq
import json
import Get_Points
import Add_Points

def JDump(data):
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

#initilises the socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5559")

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
          # Get User Points
          print("Get User Points")
          retMessage = Get_Points.get_points(message[1], data) #sends the userID and the Data
          socket.send_string(str(retMessage))
          JDump(data)
    elif message[0] == 2:
          #Add Points
          print("Add Points")
          retMessage = Add_Points.add_points(message[1], message[2], data) #sends the userID, then amount wanting to add and the Data
          socket.send_string(str(retMessage))
          JDump(data)

