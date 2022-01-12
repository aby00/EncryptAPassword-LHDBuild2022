import base64
p=input("Enter the Password:")

password = p.encode("utf-8")
encoded = base64.b64encode(password)

print("Encrypted Password: " + str(encoded))