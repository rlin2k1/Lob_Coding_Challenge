# Lob_Coding_Challenge
Lob 2019 Internship Coding Challenge

## Purpose
* READ INSTRUCTIONS.pdf<br>
* The Great Routing Problem Program - Outputs Which Partner of Lob with Take Care
of Which Order

## Technologies Used
* Developed on the macOS High Sierra Version 10.13.6 using Visual Studio Code<br>
* Python 3.6.3 for CL Application<br>

## Dependencies Needed
* Python2 or Python3 (Both Compatible)
* argparse library (pip install argparse)
* Ordered Dict Library (pip install collections)
* Scipy Library (pip install scipy) - For Euclidean Distance
* json library (Already a Built-In Module with Python)
* unittest library (Already a Built-In Module with Python)

## Usage
To get the Text File for Orders, run: python fix_routing_problem.py -o /PATHTOORDERSJSON -p /PATHTOPARTNERS<br>

The Text File will be CREATED in the Same folder as the ORDERS JSON File inputted.

The order of the command line arguments do not matter, use '-h' option for help. Can Specify Local or Absolute Path to the Orders and Partner JSON Files. If Permission Problems for opening JSON Files, run 'chmod 755 'JSONFILES'<br>
*I Chose to Add the Command Line Options for Clarity for the user on Which File is Which - ORDERS and PARTNERS*

## TESTING
https://powerfulpython.com/blog/automated-tests-types-for-python/ <br>
Automated Tests in Python -> Unit Testing in Python. <br>
Unit Test - Test a Specific Component in Isolation. <br>
Integration Test - Test How two Components Interact with each other. <br>
End-to-End Test - Test Entire Flow of Application. <br>
Run: python automated_tests.py -v

## Design Implementation
I chose to go the Object - Oriented Route in creating Orders, SingleOrder, PartnersDB, and OrderCalculator Classes since all can be stand alone - for future extendibilty with other Objects. The Classes are all simple with obvious User Interfaces (function names) for anyone to pick up and code (Add and Change Implementations). This design was rather simple with Python's built in JSON Parsing Library and Argument Parser.<br>
<br>
Some Ideas for Further Improvements would be to have the PartnersDB Connect to a Database on a Server - probably MongoDB since their Stores are similar to JSON Objects. Then, the 'find' access times for Partners would improve rather than searching through all the Base Prices like I am doing now (Which is NOT Constant). For Each SingleOrder in the list of Orders, I am searching through all the Partners. If there are N Orders and M Partners, My run-time is actually: O(N*M) <br>
I would improve this with a DataBase Selection for Prices!

## Resources
* https://docs.python.org/3/library/json.html
* https://developer.rhino3d.com/guides/rhinopython/python-xml-json/
* https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
* https://docs.python.org/3/library/argparse.html
* https://docs.python.org/3/library/unittest.html
* https://www.youtube.com/watch?v=ApTZib0L2X8
