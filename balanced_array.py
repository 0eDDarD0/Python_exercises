#Build a program that reads and array and will choose the best spot to balance the array
#The array is balanced if the sum of each side to the center chosen is equal
#Our program will also tell us the closest spot if there's no solution

from operator import indexOf

def sumSide(elements, start, wall):
    '''Returns the sum of all elements of the subarray, start included, wall not included'''
    sumatory = 0

    for i in elements[start:wall]:
        sumatory += i

    return sumatory

elements = [1,2,1,2,1]


def balanza(elements):
    '''Returns a dict where "i" is the most balanced position of the array and "diff" is the difference between the two sides'''
    best_index = 0
    best_difference = -1

    for i in range(1, len(elements)-1):
        attempt = abs(sumSide(elements, 0, i) - sumSide(elements, i+1, len(elements)))
        if(best_difference == -1 or attempt < best_difference):
            best_index = i
            best_difference = attempt

    return {"i": best_index, "diff": best_difference}

elements = [4,7,2,5,8,1,10,3,9]
solution = balanza(elements)
print("Best index to balance: " + str(solution["i"]) + "\nDifference of best index: " + str(solution["diff"]))            
