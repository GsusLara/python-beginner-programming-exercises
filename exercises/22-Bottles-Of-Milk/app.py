def number_of_bottles():
    for i in range(100):
        num=99-i
        if (num ==1):
            print(str(num) + " bottle of milk on the wall," + str(num) + " bottle of milk.")
            print("Take one down and pass it around, no more bottles of milk on the wall.")
            print()
        elif (num ==0):
            print("No more bottles of milk on the wall, no more bottles of milk.")
            print("Go to the store and buy some more, 99 bottles of milk on the wall.")
            print()
        else:
            print(str(num) + " bottles of milk on the wall ," + str(num) + " bottles of milk.")
            print("Take one down and pass it around, "+ str(num-1) + "  bottles of milk on the wall.")
            print()
    

number_of_bottles()