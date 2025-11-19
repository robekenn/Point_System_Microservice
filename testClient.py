import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")



# -- TEST GET POINTS --

#request with serilization

siReq = [1, "user_001"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()
print("Jane Doe has: ",message, " points")


#------

siReq = [1, "user_2222"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()
print("Jane Doe has: ",message, " points")


#-----

siReq = [1, "user_003"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()
print("Jane Doe has: ",message, " points")

# -- END TEST GET POINTS -- 


# -- TEST ADD POINTS --

#request with serilization

#pt 1
siReq = [2, "user_001", 22]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)


#receive responce
message = socket.recv()
print("Juan has: ",message, " points")

#pt 2
siReq = [2, "user_002", -22]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)


#receive responce
message = socket.recv()
print("Juan has: ",message, " points")

# -- END TEST ADD POINTS -- 
