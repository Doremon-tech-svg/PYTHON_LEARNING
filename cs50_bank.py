greet = input("Greeting: ").strip().lower()
if greet.split()[0] == "hello" or greet.split()[0] == "hello,":
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")
