# def getDigits(num):
#     count = 0
#     while num > 0:
#         num = int(num / 10)
#         count +=1
#     return count
#
#
# def checkEven(arr):
#     n = len(arr)
#     for i in range(n):
#         count = getDigits(arr[i])
#         if (count % 2) == 0:
#             print("This digit is even", arr[i])
#         elif (count % 2) != 0:
#             print("This digit is not even", arr[i])
#
# arr = [12,345,2,6,7896]
# checkEven(arr)


# def getDigits(num):
#     count = 0
#     while num > 0:
#         num = int(num / 10)
#         count +=1
#     return count
#
# arr = [-7,-3,2,3,11]
# print(getDigits(10))

# def duplicateZero(arr):
#     n = len(arr)
#     temp = arr.copy()
#     # print(temp)
#     for i in range(n):
#         if arr[i] == 0:
#             if arr[n - 1] == 0:
#                 arr[n - 1] == arr[n - 1]
#             else:
#                 arr[i+1] == 0
#         else:
#             arr[i] == arr[i]
#     return arr

# def duplicateZero(arr):
#     n = len(arr)
#     temp = arr.copy()
#     for i in range(n):
#         try:
#             if arr[i] == 0:
#                 temp[i], temp[i+1] == 0
#             else:
#                 temp[i] == temp[i]
#         except:
#             if arr[n-1] == 0:
#                 temp[n-1] = temp[n-1]

# def duplicateZero(arr):
#     m = n = len(arr)
#     j = 0
#     skip_index = False
#     for i, value in enumerate(arr):
#         if skip_index:
#             i += 1
#             n = m
#             skip_index = False
#         if value == 0:
#             j = i
#             # n = m
#             for n in range(n, j+1, -1):
#                 arr[n-1] = arr[n-2]
#                 skip_index = True
#             continue
#         elif arr[n - 1] == 0:
#             pass
        # else:
        #     value = value

# def duplicateZero(arr):
#     m = n = len(arr)
#     j = 0
#     for i in range(n):
#         if arr[i] == 0:
#             j = i
#             # n = m
#             for n in range(n, j+1, -1):
#                 arr[n-1] = arr[n-2]
#             # i += 2
#             # n = m
#             continue
#         elif arr[n - 1] == 0:
#             pass
#         else:
#             arr[i] = arr[i]

# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#
#         possible_dups = 0
#         length_ = len(arr) - 1
#
#         # Find the number of zeros to be duplicated
#         for left in range(length_ + 1):
#
#             # Stop when left points beyond the last element in the original list
#             # which would be part of the modified list
#             if left > length_ - possible_dups:
#                 break
#
#             # Count the zeros
#             if arr[left] == 0:
#                 # Edge case: This zero can't be duplicated. We have no more space,
#                 # as left is pointing to the last element which could be included
#                 if left == length_ - possible_dups:
#                     arr[length_] = 0 # For this zero we just copy it without duplication.
#                     length_ -= 1
#                     break
#                 possible_dups += 1
#
#         # Start backwards from the last element which would be part of new list.
#         last = length_ - possible_dups
#
#         # Copy zero twice, and non zero once.
#         for i in range(last, -1, -1):
#             if arr[i] == 0:
#                 arr[i + possible_dups] = 0
#                 possible_dups -= 1
#                 arr[i + possible_dups] = 0
#             else:
#                 arr[i + possible_dups] = arr[i]
#
# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# duplicateZero(arr)
# print(arr)

# expected arr= [1, 0, 0, 2, 3, 0, 0, 4]


# def setFlag(arr1, arr2, n, m):
#     p = n + m
#     flag = False
#     if len(arr1) == p:
#         flag = True
#         return flag, arr1, p
#     elif len(arr2) == p:
#         flag = True
#         return flag, arr2, p
#
# def concatinateArrays(arr1, arr2, n, m):
#     tuple_set = setFlag(arr1, arr2, n, m)
#     arr1 = tuple_set[1]
#     x = tuple_set[2]
#     if tuple_set[0] == True:
#         if m == 0:
#             arr1[0] = arr2[0]
#         else:
#             for i in range(x):
#                 if arr1[i] == 0:
#                     for j in range(0, m):
#                             arr1[i] = arr2[j]
#                             i += 1
#                     break
#         return arr1
#
#
# arr1 = [0]
# arr2 = [1]
# n = 1
# m = 0
# print(concatinateArrays(arr1, arr2, n, m))


# def removeVal(arr, val):
#     n = len(arr)
#     replace_value = 0
#     count = 0
#     step_back = False
#     for i in range(n):
#         if step_back:
#             i -= 1
#         if arr[i] == val:
#             arr.pop(i)
#             arr.append(replace_value)
#             step_back = True
#             count += 1
#     return arr, count
#
# arr = [0,1,2,2,3,0,4,2]
# val = 2
# print(removeVal(arr, val))


# def getCount(arr):
#     n = len(arr)
#     print(n)
#     count = 0
#     result = 0
#     for i in range(n):
#         if arr[i] == 1:
#             count += 1
#             result = max(result, count)
#         elif arr[i] == 0:
#             count = 0
#     return result
#
# arr = [1,1,1,1,0,0,1,1]
# print(getCount(arr))


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

# import requests as r
#
# data = str(r.get('https://api.publicapis.org/entries').text)
# with open('file_test.txt', 'w') as file:
#     file.write(data)

def reverse(s):
    s_list = list(s)
    n = len(s_list)
    m = int(n/2)
    i = 0
    for n in range(n, m, -1):
        s_list[i], s_list[n-1] = s_list[n-1], s_list[i]
        i += 1
    return "".join(s_list)

# def reverse(s):
#     s = list(s)
#     n = len(s)
#     m = int(n/2)
#     for i in range(0, m, +1):
#         s[i], s[n-1] = s[n-1], s[i]
#         n -= 1
#     return ''.join(s)
#
# s = 'water'
# print(reverse(s))

sample = [
    {'name': 'Thulasi'},
    {'Occupation': 'Student'}
]

print(sample[0])



# def revers_may_be_better(input):
#     i = 0
#     j = len(input) - 1
#     input = list(input)
#     while i < j:
#         temp = input[i]
#         input[i] = input[j]
#         input[j] = temp
#         i += 1
#         j -= 1
#     return "".join(input)

# def check_palindrome(s):
#     s_list = list(s)
#     n = len(s_list)
#     m = int(n/2)
#     i = 0
#     for n in range(n, m, -1):
#         if s_list[i] != s_list[n-1]:
#             return False
#         i += 1
#     return True
#
# s = 'saasgsaas'
# print(check_palindrome(s))

# # , "bello", "cello"
# print(reverse("cello"))


# test_strings = [("heelo", False), ("apple", False), ("sas", True), ("saas", True), ("civic", True)]
#
# for test_string, is_palindrome in test_strings:
#     assert check_palindrome(test_string) == is_palindrome
#
# import flask
#
# app = flask.Flask(__name__)
# app.config["Debug"] = True
#
# @app.route('/', methods=["GET"])
# def index():
#     return '<h1>Hello World</h1>'
#
# app.run()

# def duplicateZero(arr):
#     n = len(arr)
#     i = 0
#     while i < n:
#         if arr[i] == 0:
#             arr[n - 1] = arr[n - 2]
#         elif arr[n-1] == 0:
#             pass
#         i += 1
#     return arr
#
# arr = [1,0,2,3,0,4,5,0]
# print(duplicateZero(arr))


# def oneEditCheck(s, t):
#     n = len(s)
#     m = len(t)
#     one_edit_away = False
#
#     if n > m:
#         i = 0
#         while i < n:
#             temp = list(s)
#             temp.remove(temp[i])
#             p = ''.join(temp)
#             if p == t:
#                 one_edit_away = True
#             i += 1
#
#     if n == m:
#         i = 0
#         count = 0
#         while i <= (n-1):
#             temp_s = list(s)
#             temp_t = list(t)
#             temp_s.remove(temp_s[i])
#             temp_t.remove(temp_t[i])
#             if ''.join(temp_s) == ''.join(temp_t):
#                 count += 1
#             i += 1
#         if count == 1:
#             one_edit_away = True
#     return one_edit_away
#
#
# s = 'pale'
# t = 'bake'
#
# print(oneEditCheck(s, t))

# def getDigits(num):
#     count = 0
#     while num > 0:
#         num = int(num / 10)
#         count += 1
#     return count
#
# num = 12
# print(getDigits(num))