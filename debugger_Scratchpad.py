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

# sample = [
#     {'name': 'Thulasi'},
#     {'Occupation': 'Student'}
# ]
#
# print(sample[0])

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
