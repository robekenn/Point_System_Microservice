import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5558")



# -- TEST SIGN IN --

#request with serilization

siReq = [1, "jane_doe", "coolerpassword"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()
print(message)

# -- END TEST SIGN IN -- 


# -- TEST SIGN UP --

#request with serilization
siReq = [2, "Juan", "thebestpass"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)


#receive responce
message = socket.recv()
print(message)

# -- END TEST SIGN UP --

# -- TEST DELETE USER --

#request with serilization
siReq = [3, "user_001"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)


#receive responce
message = socket.recv()
print(message)

# -- END TEST DELETE USER --  
