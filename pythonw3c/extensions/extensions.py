cfilnavn=input("File name: ").lower().strip()

if filnavn.endswith(".gif"):
    print("image/gif")
elif filnavn.endswith(".jpeg") or filnavn.endswith(".jpg"):
    print("image/jpeg")
elif filnavn.endswith(".png"):
    print("image/png")
elif filnavn.endswith(".pdf"):
    print("application/pdf")
elif filnavn.endswith(".txt"):
    print("text/plain")
elif filnavn.endswith(".zip"): 
    print("application/zip")
else: print("application/octet-stream")

