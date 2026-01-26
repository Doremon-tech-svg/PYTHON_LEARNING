ex = input("File name: ").strip().split(".")
n = len(ex)
ex = ex[n-1].lower()

if ex == "jpeg" or ex == "jpg":
    print(f"image/jpeg")
elif ex == "gif" or ex == "png":
    print(f"image/{ex}")
elif ex == "pdf" or ex == "zip":
    print(f"application/{ex}")
elif ex == "txt":
    print("text/plain")
else:
    print("application/octet-stream")


