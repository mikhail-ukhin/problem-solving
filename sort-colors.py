# Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


# 2-way
def sortColors(arr):
    nums = [0 for _ in range(3)]
    p, i = 0, 0

    for item in arr: nums[item] += 1

    while i < len(arr):
        if nums[p] == 0:
            p += 1
        else:    
            arr[i] = p
            nums[p] -= 1
            i += 1

    return arr 

# 1-way
def sortColors2(arr):
    l, m, h = 0, 0, len(arr) - 1

    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 2:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
        else:
            m += 1    







