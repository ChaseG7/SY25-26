import datetime

v1 = "my_diary.txt"

while True:
    print("1. Write, 2. Read, 3. Clear, 4. Exit")
    v2 = input("Select (1-4): ")
    if v2 == "1":
        v3 = open(v1, "a")
        v4 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        v5 = input("Entry: ")
        v6 = v3.write(f"[{v4}] {v5}\n")
        v3.close()
        print("Characters saved:", len(v5))
    elif v2 == "2":
        v3 = open(v1, "r")
        v7 = v3.readlines()
        v3.close()
        print("-----")
        for v8 in v7:
            print(v8.strip())
        print("-----")
    elif v2 == "3":
        v3 = open(v1, "w")
        v3.close()
        print("Diary cleared.")
    elif v2 == "4":
        break