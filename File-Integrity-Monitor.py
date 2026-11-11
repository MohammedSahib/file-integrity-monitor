import hashlib
import json
import argparse
parser = argparse.ArgumentParser(description="Enter File to check integrity of:")
parser.add_argument("filename",help = "The file to check integrity of")
args=parser.parse_args()
file_data ={}
file_data["file_name"] = args.filename
def handle_json():
    with open("destination.json","w") as file:
        json.dump(file_data,file)
def opening_in_rb():
    with open(args.filename, "rb") as pointer:
        file_hash = hashlib.file_digest(pointer,"sha256")
        return file_hash.hexdigest()
def testing_writer():
    with open(args.filename,"a") as pointer2:
        pointer2.write("this is li now maybe\n")

first_hash=opening_in_rb()
file_data["file_hash"] = first_hash
handle_json()

print("Before",first_hash)
testing_writer()


second_hash=opening_in_rb()
print("After:",second_hash)
if (first_hash==second_hash):
    print("snapshots match")






