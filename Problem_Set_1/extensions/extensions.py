name=input("Name of the file: ")

name=name.lower().strip()

if(".gif" in name):
    print("image/gif ")
elif(".jpg" in name):
    print("image/jpeg  ")
elif(".jpeg" in name):
    print("image/jpeg  ")
elif(".png" in name):
    print("image/png ")
elif(".pdf" in name):
    print("application/pdf ")
elif(".txt" in name):
    print("text/plain ")
elif(".zip" in name):
    print("application/zip ")

else: print("application/octet-stream ")

