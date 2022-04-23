# 1. Given a binary array, find the maximum number of consecutive 1s in this array.

def getCount(arr):
    n = len(arr)
    print(n)
    count = 0
    result = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1
            result = max(result, count)
        elif arr[i] == 0:
            count = 0
    return result

arr = [1,1,1,1,0,0,1,1,0,1,1,1,1,1,1]
print(getCount(arr))

# 2. Reverse a given string
# solution 1
# def reverseString(s):
#     rev_string = ''
#     for char in s:
#         rev_string = char + rev_string
#     return rev_string

#solution 2
def reverseString(s):
    s_list = list(s)
    n = len(s_list)
    m = int(n/2)
    i = 0
    for n in range(n, m, -1):
        s_list[i], s_list[n-1] = s_list[n-1], s_list[i]
        i += 1
    return "".join(s_list)
s = 'Thulasi'
print(reverseString(s))

# 3. Check if string is a palindrome
def check_palindrome(s):
    s_list = list(s)
    n = len(s_list)
    m = int(n/2)
    i = 0
    for n in range(n, m, -1):
        if s_list[i] != s_list[n-1]:
            return False
        i += 1
    return True

s = 'civicc'
print(check_palindrome(s))

# 4. Given an array nums of integers, return how many of them contain an even number of digits.
def getDigits(num):
    count = 0
    while num > 0:
        num = int(num / 10)
        count +=1
    return count


def checkEven(arr):
    n = len(arr)
    even_count = 0
    for i in range(n):
        count = getDigits(arr[i])
        if (count % 2) == 0:
            print(f"{arr[i]} has even number of digits")
            even_count += 1
        elif (count % 2) != 0:
            print("{} has odd number of digit".format(arr[i]))
    print("Total number of numbers containing even number of digits are {}".format(even_count))
    # return even_count

# arr = [12,345,2,6,7896]
arr = [555,901,482,1771]
checkEven(arr)

# 5. Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

def squareNumbers(arr):
    n = len(arr)
    result = []
    for i in range(n):
        value = arr[i] * arr[i]
        result.append(value)
        result.sort()
    return result

arr = [-4,-1,0,3,10]
print(squareNumbers(arr))


# 6. Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

def duplicateZero(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            for n in range(n, i+1, -1):
                arr[n-1] = arr[n-2]
            i += 2
            n = len(arr)
            continue
        else:
            i += 1

# 7. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def setFlag(arr1, arr2, n, m):
    p = n + m
    flag = False
    if len(arr1) == p:
        flag = True
        return flag, arr1, p
    elif len(arr2) == p:
        flag = True
        return flag, arr2, p


def concatinateArrays(arr1, arr2, n, m):
    tuple_set = setFlag(arr1, arr2, n, m)
    arr1 = tuple_set[1]
    x = tuple_set[2]
    if tuple_set[0] == True:
        if m == 0:
            arr1[0] = arr2[0]
        else:
            for i in range(x):
                if arr1[i] == 0:
                    for j in range(0, m):
                        arr1[i] = arr2[j]
                        i += 1
                    break
        return arr1


arr1 = [0]
arr2 = [1]
n = 1
m = 0
concatinateArrays(arr1, arr2, n, m)

# 8. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

def removeVal(arr, val):
    n = len(arr)
    replace_value = 0
    count = 0
    step_back = False
    for i in range(n):
        if step_back:
            i -= 1
        if arr[i] == val:
            arr.pop(i)
            arr.append(replace_value)
            step_back = True
            count += 1
    return arr, count

arr = [0,1,2,2,3,0,4,2]
val = 2
print(removeVal(arr, val))


# 9. Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Without using another data structure
def isUnique(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s), +1):
            if s[i] == s[j]:
                return False
    return True


s = 'dsa'
isUnique(s)

# with the help of an extra data structure (array)
# def isUnique(s):
#     s = sorted(s)
#     print(s)
#     for i in range(len(s)):
#         if s[i] == s[i+1]:
#             return False
#     return True
# s = 'ddsa'
# isUnique(s)

# 10. Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(s1, s2):
    n = len(s1)
    m = len(s2)
    check = False
    if n == m:
        check = True

    str1 = ''.join(sorted(s1))
    str2 = ''.join(sorted(s2))
    print(str1)
    print(str2)

    for i in range(n):
        if str1[i] == str2[i]:
            check = True
        else:
            check = False
    return check


s1 = 'abcd'
s2 = 'cdae'
checkPermutation(s1, s2)

# 11. Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.

def replaceSpaces(s):
    t = list(s)
    n = len(t)
    for i in range(n):
        if t[i] == " ":
            t[i] = '%20'
        elif t[n-1] == " ":
            t[n-1] = ""
    t = ''.join(t)
    return t

s = "Mr John Smith "
replaceSpaces(s)


# 12. Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters.

# Solution 1

# input = "hancbnah"
# characters = dict()
# for char in input:
#     if char in characters:
#         characters[char] += 1
#     else:
#         characters[char] = 1

# can_form_palindrom = False
# if len(input) % 2 == 0:  # number of all characrers must be even
#     can_form_palindrom = all([value % 2 == 0 for key, value in characters.items()])
# else:
#     can_form_palindrom = (
#         len([value for key, value in characters.items() if value % 2 != 0]) == 1
#     )

# print(can_form_palindrom)

# Solution 2
def permutationCheck(s):
    s = s.lower()
    t = list(s)
    lst = []
    is_palindrome = False

    t = [ele for ele in t if ele != " "]
    # print(t)
    n = len(t)

    for i in range(n):
        if (t[i] in lst):
            lst.remove(t[i])
        else:
            lst.append(t[i])
    # print(lst)

    if (len(t) % 2 == 0 and len(lst) % 2 == 0):
        for i in range(len(lst)):
            if lst[i] != lst[i + 1]:
                is_palindrome = False
                break
            else:
                is_palindrome = True
    elif (len(t) % 2 == 1 and len(lst) % 2 == 1):
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome


s = "Tact Coa"
print(permutationCheck(s))

# 13. There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def oneEditCheck(s, t):
    n = len(s)
    m = len(t)
    one_edit_away = False

    if n > m:
        i = 0
        while i < n:
            temp = list(s)
            temp.remove(temp[i])
            p = ''.join(temp)
            if p == t:
                one_edit_away = True
            i += 1

    if n == m:
        i = 0
        count = 0
        while i <= (n-1):
            temp_s = list(s)
            temp_t = list(t)
            temp_s.remove(temp_s[i])
            temp_t.remove(temp_t[i])
            if ''.join(temp_s) == ''.join(temp_t):
                count += 1
            i += 1
        if count == 1:
            one_edit_away = True
    return one_edit_away


s = 'geeks'
t = 'geek'

print(oneEditCheck(s, t))

# 14. String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression(s):
    n = len(s)
    s = list(s)
    t = []
    count = 0
    for i in range(n):
        if i == 0:
            t.append(s[i])
        # if s[i] in t:
        if s[i] == s[i-1]:
            count += 1
        else:
            # import pdb;pdb.set_trace()
            t.append(str(count))
            t.append(s[i])
            count = 1
        if i == n-1:
            t.append(str(count))
    t = ''.join(t)
    if len(t) < len(s):
        return t
    else:
        return ''.join(s)



s = 'aba'
print(stringCompression(s))

# 15. Given to arrays of similar objects (with different values) combine the values and print the result.

# def combineArrays(s1, s2):
#     """Method that combines 2 arrays and returns the 1 combined array"""
#     n = len(s1)
#     m = len(s2)
#     t = []

#     for i in range(n):
#         t.append(s1[i])
#     for i in range(m):
#         if s2[i] in t:
#             pass
#         else:
#             t.append(s2[i])
#     return ''.join(t)

def combineArrays(s1, s2):
    """Method that combines 2 arrays and returns the 1 combined array"""
    t = ""

    t = s1 + s2
    # for char in s1:
    #     t = t + char
    # for char in s2:
    #     if char in t:
    #         pass
    #     else:
    #         t = t + char
    return t

# s1 = "abc"
# s2 = "sdc"
# print(combineArrays(s1, s2))

s1 = "abc"
s2 = "sdc"
print(combineArrays(s1, s2))

# 16. Assume you have a method isSubstringwhich checks if one word is a substring of another.
# Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of"erbottlewat").

def isSubstring(s1, s2):
    """Method that checks if a string is a substring of a string"""
    t = ""

    t = s1 + s1
    return t

def isRotation(s1, s2):
    """Method that checks if a string is a rotation of the other"""
    check_string = isSubstring(s1, s2)
    if check_string.count(s2) > 0:
        return True
    else:
            return False

s1 = "waterbottle"
s2 = "erbottlewat"
print(isRotation(s1, s2))

# 17. Create a Flask app

# import flask
# from flask import request, jsonify
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True
#
# # Create some test data for our catalog in the form of a list of dictionaries.
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]
#
#
# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''
#
#
# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)
#
#
# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."
#
#     # Create an empty list for our results
#     results = []
#
#     # Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)
#
#     # Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return jsonify(results)
#
# app.run()

# 18. Fetch data from url using requests
# import requests as r
#
# data = str(r.get('https://api.publicapis.org/entries').text)
# with open('file_test.txt', 'w') as file:
#     file.write(data)

# 19. Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicateNumbers(arr):
    n = len(arr)
    i = 0
    while i < n:
        for j in range(1, n-1, +1):
            if arr[i] == arr[j]:
                arr.pop(arr[j])
                n -= 1
                break
        i += 1
    return arr, n

# arr = [1, 1, 2]
arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicateNumbers(arr))

# 20. Given an array arr of integers, check if there exists two integers N and M
# such that N is the double of M ( i.e. N = 2 * M).

def numAndItsDoubleCheck(arr):
    n = len(arr)
    for i in range(0, n, +1):
        for j in range(0, n, +1):
            if arr[i] == 2 * arr[j]:
                return True
            else:
                return False

arr = [3,1,7,11]
print(numAndItsDoubleCheck(arr))

# 21. Given an array of integers arr, return true if and only if it is a valid mountain array
# Recall that arr is a mountain array if and only if:
#   arr.length >= 3
#   There exists some i with 0 < i < arr.length - 1 such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def isMountainArray(arr):
    n = len(arr)
    m = 0
    p = 0
    mountain_right = False
    mountain_left = False
    if n >= 3:
        if n % 2 == 0:
            m = int(n/2) - 1
            p = int(n/2)
        else:
            m = p = int(n / 2)

        for i in range(0, m, +1):
            if arr[i] < arr[i+1]:
                mountain_right = True
        for j in range(n, p, -1):
            if arr[n-1] < arr[n-2]:
                mountain_left = True
    else:
        mountain_array = False
    if mountain_right and mountain_left:
        return True
    else:
        return False

arr = [0,2,3,4,5,2,1,0]
print(isMountainArray(arr))

# 22. Given an Array of integers, return an Array where every element at an even-indexed position is squared.
#Solution 1
def evenIndexSquaring(arr):
    n = len(arr)
    for i in range(0, n, +2):
        arr[i] = arr[i] * arr[i]
    return arr

# Solution 2
# def evenIndexSquaring(arr):
#     n = len(arr)
#     for i in range(0, n):
#         if i % 2 == 0:
#             arr[i] = arr[i] * arr[i]
#     return arr

# Solution 3
# def evenIndexSquaring(arr):
#     n = len(arr)
#     i = 0
#     while i < n:
#         if i % 2 == 0:
#             arr[i] = arr[i] * arr[i]
#         i += 1
#     return arr

arr = [9, -2, -9, 11, 56, -12, -3]
print(evenIndexSquaring(arr))

# 23. Given an array arr, replace every element in that array with the greatest element
# among the elements to its right, and replace the last element with -1.

def replaceWithGreatestRight(arr):
    n = len(arr)
    i = 0
    while i < n:
        for n in range(n, i+1, -1):
            if arr[n-1] > arr[n-2]:
                arr[i] = arr[n-1]
        i += 1
        n = len(arr)
        if i == n-2:
            arr[n - 2] = arr[n - 1]
        elif i == n-1 or i == n:
            arr[n-1] = -1
    return arr

# arr = [17,18,5,4,6,1]
arr = [400]
print(replaceWithGreatestRight(arr))

# 24. Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZerosToEndOfArray(arr):
    n = len(arr)
    count = 0
    i = 0
    if n == 1:
        pass
    else:
        while i < n:
            if arr[i] == 0:
                arr.remove(arr[i])
                count += 1
                n = len(arr)
            i += 1
        for i in range(count):
            arr.append(0)
    return arr

arr = [0]
# arr = [0,1,0,3,12]
print(moveZerosToEndOfArray(arr))

# 25. Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Solution 1 using sort
def sortArrayByParity(arr):
    arr.sort(key = lambda x: x % 2)
    return arr

# Solution 2
def sortArrayByParity(arr):
    return ([x for x in arr if x % 2 == 0] +
            [x for x in arr if x % 2 == 1])

# Solution 3
def sortArrayByParity(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] % 2 > arr[j] % 2:
            arr[i], arr[j] = arr[j], arr[i]

        if arr[i] % 2 == 0: i += 1
        if arr[j] % 2 == 1: j -= 1

    return arr

# 26. A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i]. (# [''.join(value) for value in index_list], sep=','))

def checkHeightExpected(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    index_list = []

    if not n >= 1 or not m >= 1:
        return False
    if not n == m:
        return False
    for i in range(n):
        if arr1[i] != arr2[i]:
            index_list.append(str(i))
    # import pdb;pdb.set_trace()
    if len(index_list) == 0:
        print("All indices match")
        print(f"Number of indice(s) that do not match are: {len(index_list)}")
    elif len(index_list) == n:
        print("All indices do not match")
        print(f"Number of indice(s) that do not match are: {len(index_list)}")
    elif len(index_list) > 0:
        print("Indices {} do not match".format(', '.join(index_list)))
        print(f"Number of indice(s) that do not match are: {len(index_list)}")
    # return len(index_list)

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5]

# arr1 = [5,1,2,3,4]
# arr2 = [1,2,3,4,5]

arr1 = [1,1,4,2,1,3]
arr2 = [1,1,1,2,3,4]
print(checkHeightExpected(arr1, arr2))

# 27. Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
# Flip the first zero will get the maximum number of consecutive 1s.

def countConsecutives(arr):
    n = len(arr)
    count = 0
    result = 0

    for i in range(n):
        if arr[i] == 0:
            arr[i] = 1
            break

    for i in range(n):
        if arr[i] == 1:
            count += 1
        elif arr[i] == 0:
            result = count
            count = 0

    return max(result, count)

arr = [1,0,1,1,1,1,0,1,1,1,1,1]
# arr = [1,0,1,1,0,1,1,1,1,1]
# arr = [1,0,1,1,0,1]
# arr = [1,0,1,1,0]
print(countConsecutives(arr))

# 28. Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

def thirdDisticntMaxNumber(arr):
    n = len(arr)
    count = 1
    i = 0
    compare = None

    if len(arr) == 0:
        print("No numbers in array, nothing to compare")
        pass
    elif len(arr) == 1:
        return ''.join(arr)
        pass
    elif len(arr) > 1 and len(arr) < 3:
        print(f"The Distinct maximum number between the two numbers in the array is {max(arr)}")
        pass
    else:
        compare = arr[0]
        while i < n:
            if arr[i] != compare:
                count += 1
                compare = arr[i]
            if count == 3:
                print(f"The third distinct maximum number is {arr[i]}")
            i += 1

arr = [2,2,3,3,3,3,1,4]
# arr = [2,3,1,4]
# arr = [2,2,3,1]
# arr = [1,2]
# arr = [3,2,1]
thirdDisticntMaxNumber(arr)

# 29. Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums

# Solution 1
def notInListNumbers(arr):
    n = len(arr)
    num_lst = []
    i = 1

    while i <= n:
        num_lst.append(i)
        i += 1

    for i in range(n):
        if arr[i] in num_lst:
            num_lst.remove(arr[i])
    return num_lst



