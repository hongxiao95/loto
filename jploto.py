# coding:utf-8
import random, tqdm
import numpy as np

PARAM_LOTO_7 = (37,7)
PARAM_LOTO_6 = (43,6)
PARAM_MINI_LOTO = (31,5)

lucky = 19260817


def loto(param, lucky:int):
    total = param[0]
    aim_len = param[1]
    print(f"get lucky as {lucky}")

    candidate = np.array(list(range(1, total  + 1)))

    for i in tqdm.tqdm(range(lucky)):
        np.random.shuffle(candidate)
            
    print("Shuffle Finished")
    return candidate[:aim_len]


def main():
    choice = int(input("1. Loto7\n2. Loto6\n3. MiniLoto\n"))
    user_lucky = ""
    try:
        user_lucky = input(f"input a lucky number, default as {lucky}")
        user_lucky = int(user_lucky)
    except Exception:
        user_lucky = lucky
    

    choice = (choice - 1) % 3

    if choice == 0:
        print(f"Running Loto 7: {loto(PARAM_LOTO_7, user_lucky)}")
    elif choice == 1:
        print(f"Running Loto 6: {loto(PARAM_LOTO_6, user_lucky)}")
    else:
        print(f"Runing MiniLoto: {loto(PARAM_MINI_LOTO, user_lucky)}")
    pass

if __name__ == "__main__":
    main()