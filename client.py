'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import argparse
import uuid
PORT = 3000

class DatastoreClient():
    
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, key, value):
        return self.stub.put(datastore_pb2.Request(key=key,value=value))
   
    def get(self, key):
        return self.stub.get(datastore_pb2.Request2(key=key))
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)
    value = 'foo'
    print("## PUT Request: value = " + value) 
    key=uuid.uuid4().hex
    resp = client.put(key,value)
    print("## PUT Response: key = " + key)
    print("## GET Request: key = " + resp.key)
    r = client.get(resp.key) 
    print("## GET Response: value = " + r.value) 


if __name__ == "__main__":
    main()

