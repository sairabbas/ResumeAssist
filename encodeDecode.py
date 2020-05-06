import base64

#converts a string of text into a txt file
def decodeFile(text):
    decoded_string = ""
    with open(text, "rb") as encoded_file:
        data = encoded_file.read()
        decoded_string = base64.b64decode(data[2:-1])
    with open("decoded.txt", "wb") as txt:
        txt.write(decoded_string)

#converts a txt file into a string of bytes
def encodeFile(txt):
    encoded_string = ""
    with open(txt, "rb") as txt_file:
        encoded_string = base64.b64encode(txt_file.read())
    return encoded_string