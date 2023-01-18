"""B64 Encode and Decode Realm JSON File"""
import argparse
import base64
import json

parser = argparse.ArgumentParser(
    prog="manage_realm",
    description="B64 Encode and Decode Realm JSON File for storing to and retrieving from Parameter store",
)
parser.add_argument("operation", choices=["encode", "decode"])
args = parser.parse_args()


def encode():
    with open("ayr-realm.json") as realm_file:
        realm = json.load(realm_file)
    realm_string = json.dumps(realm).encode()
    encoded_realm = base64.b64encode(realm_string)
    with open("ayr-realm-b64", "wb") as realm_string_file:
        realm_string_file.write(encoded_realm)


def decode():
    with open("ayr-realm-b64") as realm_string_file:
        realm_string = realm_string_file.read()
    decoded_realm_string = base64.b64decode(realm_string).decode()
    decoded_realm = json.loads(decoded_realm_string)
    with open("ayr-realm.json", "w") as realm_file:
        json.dump(decoded_realm, realm_file, indent=2)


def main():
    if args.operation == "decode":
        decode()
    else:
        encode()


if __name__ == "__main__":
    main()
