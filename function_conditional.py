def main():
    t = input("What time it is? ")
    time = convert(t)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    l = time.split(":")
    return (float(l[0]) + float(l[1])/60)


if __name__ == "__main__":
    main()
