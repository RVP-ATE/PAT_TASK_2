# defining the pyramid strategy
def pyramid():
    x=0
# 'i' representing the rows
    for i in range(0,21):
        k = 0
# 'j' representing the column
        for j in range(1,x+1):
# condition for the j to go as a pyramid
            if j>=1:
                k=k+1
            print(k,end="")
        print()
# column should be incremented for each row increment
        x = x+1

pyramid()
# End of the program