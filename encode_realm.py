import json
import base64


def encode():
    with open("ayr-realm.json") as realm_file:
        realm = json.load(realm_file)
    realm_string = json.dumps(realm).encode()
    return base64.b64encode(realm_string)


def main():
    encoded_realm = encode()
    with open("ayr-realm-b64", "wb") as realm_string_file:
        realm_string_file.write(encoded_realm)


if __name__ == "__main__":
    main()
