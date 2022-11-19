import os

if __name__ == '__main__':
    command = "python .\main.py -s "
    test_data = [[28011, 67158946935057], [81279, 565450408615425], [51813, 229783022530665]]

    no_inputs = 3

    print(f"Enter {no_inputs} shares")
    shares = []
    for i in range(1, no_inputs+1):
        x = int(input(f"#{i} Enter X: "))
        y = int(input(f"#{i} Enter Y: "))
        shares.append([x,y])


    for i in range(0, len(shares)):
        command += f"{shares[i][0]} {shares[i][1]} "

    print(command)
    os.system(command)
