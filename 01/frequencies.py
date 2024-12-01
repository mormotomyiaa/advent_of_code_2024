from functools import reduce


def main():
    left_dict = dict()
    right_dict = dict()

    with open("01/input","r") as file:
        for line in file.readlines():
            [left,right] = line.strip().split("   ")
            count_left = left_dict.setdefault(int(left),0)
            left_dict[int(left)] = count_left+1
            count = right_dict.setdefault(int(right),0)
            right_dict[int(right)] = count+1
            

    def calc_similarity(a:int, b):
        key, value = b
        if (count := right_dict.get(key)) is not None:
            a += key*value*count
        return a

    # value =reduce(calc_similarity, left_dict.items(),0)


    value =reduce(lambda x,y : x + (y[0]*y[1]*right_dict.get(y[0]) if right_dict.get(y[0]) else 0 ), left_dict.items(),0)
    print(value)

    

    # value = reduce(lambda x,y : x + (abs(y[0]-y[1])), zip(sorted(left_list),sorted(right_list)),0)

        


if __name__ == "__main__":
    main()