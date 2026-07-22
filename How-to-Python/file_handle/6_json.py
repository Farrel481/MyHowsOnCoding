"""
JSON: JavaScript Object Notation.
JSON adopts the data structure of objects and array from JavaScript.
Not exclusive for JS only.
JS Object ~ Python Dictionary: {"key": "value"}
JS Array  ~ Python List: ["Me", "Myself", "I"]

JSON is important for these:
1. Web API: Transfer Data, Request & Response
2. Configuration
3. No-SQL Database
4. Data Transfer of each Services

JSON Structure:
Python Dict: Object
Python List: Array
Object: - Key have to be a String
        - String use ""
        - Value: str, number, obj, array, bool(true/false), null.

Array : - Writings are the same with PyList

Last element of JSON can't be end with a coma.
Comments are not permitted in JSON
"""

#Python can handle 2 types of JSON:
#1. str filled with JSON valid formats.
data = {"name": "Me", "Age": 18}

#2. JSON File: file with .json extension filled with valid JSON.
