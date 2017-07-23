# Code for CS325 Project 1
# Members: Gabriel Janzen, Paul Lee, Mazen Alotaibi
#
# To run: python mss.py


import time

def enumeration(list):
    starttime = time.time()

    maxSum = int(list[0])
    maxArray = list[0]
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            sum = int(0)
            for k in range(i, j):
                sum += int(list[k])
                if sum > maxSum:
                    maxSum = sum
                    maxArray = list[i:j+1]

    runtime = time.time() - starttime
    print("list size:", len(list))
    print("  runtime:", runtime)
    print(list)
    print("maxSum:", maxSum)
    print("maxArray:", maxArray)
    print("\n")
    return maxSum, maxArray

def betterEnumeration(list):
    starttime = time.time()

    maxSum = int(list[0])
    maxArray = list[0]
    for i in range(len(list)):
        sum = int(0)
        for j in range(i, len(list)):
            sum += int(list[j])
            if sum > maxSum:
                maxSum = sum
                maxArray = list[i:j+1]

    runtime = time.time() - starttime
    print("list size:", len(list))
    print("  runtime:", runtime)
    print(list)
    print("maxSum:", maxSum)
    print("maxArray:", maxArray)
    print("\n")
    return maxSum, maxArray


input = map(str.split, open('./MSS_Problems.txt'))
output = open('./MSS_Results.txt', 'w')

if __name__ == "__main__":

    for i in range(0, len(input)):
        enumeration(input[i])


    for i in range(0, len(input)):
        betterEnumeration(input[i])
