for i in range(9):
    msg = ""
    for j in range(9):
        cX = i // 3
        cY = j // 3
        msg += str(cX) + "" + str(cY) + "."
        if j == 2 or j == 5:
            msg += "|"
    if i == 3 or i == 6:
        print("====================")
    print(msg)