def guessing(a):
    array = [i for i in range(1,a+1)]
    left_point = 0
    right_point = len(array)-1

    mid_point = (left_point + right_point) // 2
    mid_element = array[mid_point]

    while left_point <= right_point:
        mid_point = (left_point + right_point) // 2
        mid_element = array[mid_point]

        if mid_point == 0:
            print(f"{mid_element} a számod")
            return
        
        gon = input(f"Nagyobb, mint {mid_element}? ")
        if gon == "igen":
            left_point = mid_point + 1

        if gon == "nem":
            gon1 = input(f"Kisebb mint {mid_element}? ")
            if gon1 == "nem":
                print(f"{mid_element} a számod")
                return
            right_point = mid_point - 1 #200000



    print(f"A számod csak a {mid_element} lehet, vagy pedig nem az intervallumban választottál")

guessing(10)








