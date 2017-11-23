'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import argparse
import rocksdb

PORT = 3000

class DatastoreClient():
    
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)
        self.db1 = rocksdb.DB("lab2.db", rocksdb.Options(create_if_missing=True))

    def replicator(self):
        return self.stub.replicator(datastore_pb2.Request1())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)
    resp = client.replicator()
    for i in resp:
        
        k = i.key.encode('utf-8')
        l = i.value.encode('utf-8') 
        print(k,l)
        self.db1.put(k,l)
    

if __name__ == "__main__":
    main()

