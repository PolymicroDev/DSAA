def find_compliment(numbers,sum):
    compliments = {}

    for i in range(len(numbers)):
        compliments[numbers[i]] = i

    for i in range(len(numbers)):
        dif = sum-numbers[i]

        if compliments.get(dif):
            second_index = compliments[dif]
            return print(f"Indices are: {i} and {second_index}")
            
    return ("No compliment was found")

find_compliment([1,3,4,2],6)




