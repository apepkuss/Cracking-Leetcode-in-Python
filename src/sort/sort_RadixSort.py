

# Radix Sort
#
# Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in range from 1 to k.
# What if the elements are in range from 1 to n^2? We can't use counting sort because counting sort will take O(n^2)
# which is worse than comparison based sorting algorithms. Can we sort such an array in linear time? Radix Sort is
# the answer.
#
# The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit.
# Radix sort uses counting sort as a subroutine to sort input array according to the i'th digit.
#
# Example:
# Original, unsorted list: 170, 45, 75, 90, 802, 24, 2, 66
#
# Sorting by least significant digit (1s place) gives: [Notice that we keep 802 before 2, because 802 occurred before
# 2 in the original list, and similarly for pairs 170 & 90 and 45 & 75.]
# 170, 90, 802, 2, 24, 45, 75, 66
#
# Sorting by next digit (10s place) gives: [Notice that 802 again comes before 2 as 802 comes before 2 in the previous
# list.]
# 802, 2, 24, 45, 66, 170, 75, 90
#
# Sorting by most significant digit (100s place) gives:
# 2, 24, 45, 66, 75, 90, 170, 802

# What is the running time of Radix Sort?
# Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing
# numbers, for example, for decimal system, b is 10. What is the value of d? If k is the maximum possible value,
# then d would be O(logb(k)). So overall time complexity is O((n+b) * logb(k)). Which looks more than the time
# complexity of comparison based sorting algorithms for a large k. Let us first limit k. Let k <= nc where c is a
# constant. In that case, the complexity becomes O(nLogb(n)). But it still doesn't beat comparison based sorting
# algorithms.
#
# What if we make value of b larger?. What should be the value of b to make the time complexity linear? If we set b
# as n, we get the time complexity as O(n). **CONCLUSION** we can sort an array of integers with range from 1 to nc
# if the numbers are represented in base n (or every digit takes log2(n) bits).
#
# Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort?
# If we have logn bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide
# range of input numbers. The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort
# uses hardware caches more effectively. Also, Radix sort uses counting sort as a subroutine and counting sort takes
# extra space to sort numbers.

def radix_sort(arr):
    # find the maximum element in arr to know number of digits
    maxval = max(arr)

    # Do Counting Sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i where
    # i is current digit number
    exp = 1
    while maxval/exp > 0:
        count_sort(arr, exp)
        exp *= 10

def count_sort(arr, exp):
    n = len(arr)

    tmp = [0] * n
    count = [0] * n

    for i in range(n):
        idx = arr[i] / exp
        count[idx] += 1

    for i in range(1, n):
        count[i] += count[i-1]

    # sort
    i = n-1
    while i >= 0:
        idx = arr[i] / exp
        j = idx % 10
        count[j] -= 1
        tmp[count[j]] = arr[i]
        i -= 1

    for i in range(n):
        arr[i] = tmp[i]

