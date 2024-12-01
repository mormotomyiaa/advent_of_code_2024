from functools import reduce


def main():
    left_list = []
    right_list = []

    with open("01/input","r") as file:
        for line in file.readlines():
            [left,right] = line.strip().split("   ")
            left_list.append(int(left))
            right_list.append(int(right))
    value = reduce(lambda x,y : x + (abs(y[0]-y[1])), zip(sorted(left_list),sorted(right_list)),0)
    print(value)

        


if __name__ == "__main__":
    main()