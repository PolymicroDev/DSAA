
def reverse(x: int) -> int:
    num = str(x)
    new_num = ""
    for i in range(3,0):
        print(num[i])
        new_num += num[i]
        i-=1
    
    return new_num


print(reverse(322))