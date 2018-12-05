""" automated_tests.py
Automated Tests for the Lob Great Routing Problem
DO NOT FORGET EDGE CASES!
    -No Partners
    -No Orders

Author(s):
    Roy Lin

Date Created:
    October 16th, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from __future__ import print_function #Make Print Compatible with Python 2 and 3
import json #To Parse Through JSON Files
import unittest #For Automated Testing Purposes
import filecmp #For Testing Comparison of Files

from Orders import Orders #For Order Class Containing Order Items
from PartnersDB import PartnersDB  #For Partners DataBase Creation
from OrderCalculator import OrderCalculator #Order Calculator Class - Find Match
from fix_routing_problem import return_json_data

# ---------------------------------------------------------------------------- #
# Intialization of Testing Variables - Easily Extendible and Dynamic!
# ---------------------------------------------------------------------------- #
list_of_order_jsons = ['./Test_Files/Test_Orders/orders.json', \
'./Test_Files/Test_Orders/orders1.json', \
'./Test_Files/Test_Orders/orders2.json', \
'./Test_Files/Test_Orders/orders3.json', \
'./Test_Files/Test_Orders/orders4.json']

list_of_partner_jsons = ['./Test_Files/Test_Partners/partners.json']

list_of_answer_jsons = ['./Test_Files/Test_Answers/answers.txt', \
'./Test_Files/Test_Answers/answers1.txt', \
'./Test_Files/Test_Answers/answers2.txt', \
'./Test_Files/Test_Answers/answers3.txt', \
'./Test_Files/Test_Answers/answers4.txt']

list_of_orders_count = [10, 69, 36, 99, 42]

list_of_partners_count = [10]

class TestOrderCalculator(unittest.TestCase):
    def test_answer_files_json(self):
        print()
        print("Following Tests tested with Partner File: " + \
        list_of_partner_jsons[0] + ":")
        print()
        for i in range(0, len(list_of_order_jsons)):
            print("Testing Orders JSON File: " + list_of_order_jsons[i])
            print("Expected Output: ")
            answers = open(list_of_answer_jsons[i], 'r')
            print(answers.read())
            answers.close()
            #Testing Base - fix_routing_problem.py
            orders_json = return_json_data(list_of_order_jsons[i])
            partners_json = return_json_data(list_of_partner_jsons[0])
            lob_orders = Orders(orders_json)
            partners_db = PartnersDB(partners_json)
            order_calculator = OrderCalculator(lob_orders, partners_db)
            
            print("Actual Output:")
            file = open(list_of_order_jsons[i].split('.json')[0] + '.txt', 'w')
            partner_order_dict = (order_calculator.get_partner_orders())
            for key, value in partner_order_dict.items():
                file.write(key + '\n') 
                print(key)
                for order in value:
                    file.write(order + '\n')
                    print(order)
            file.close()
            self.assertEqual(True, filecmp.cmp(list_of_answer_jsons[i], \
            list_of_order_jsons[i].split('.json')[0] + '.txt') )
            print("Same as Corresponding Answer File - PASS")
            print()
        print("----------------------------------------------------------------\
-------")

    def test_order_item_count(self):
        for i in range(0, len(list_of_order_jsons)):
            print("Testing Order JSON File: " + list_of_order_jsons[i] + \
            " with Expected Order Item Amount of " + \
            str(list_of_orders_count[i]))

            #Testing Orders Class
            orders_json = return_json_data(list_of_order_jsons[i])
            lob_orders = Orders(orders_json)
            actual_order_item_amount = len(lob_orders.get_order_items())
            print("Actual Order Amount: " + str(actual_order_item_amount), \
            end = "")

            self.assertEqual(actual_order_item_amount, \
            list_of_orders_count[i])
            print(" - PASS")
            print()
        print("----------------------------------------------------------------\
-------")

    def test_partners_count(self):
        print()
        for i in range(0, len(list_of_partner_jsons)):
            print("Testing Partner JSON File: " + list_of_partner_jsons[i] + \
            " with Expected Partner Count of " + \
            str(list_of_partners_count[i]))

            #Testing PartnerDB Class
            partners_json = return_json_data(list_of_partner_jsons[i])
            partners_db = PartnersDB(partners_json)
            actual_partner_amount = partners_db.get_partners_count()
            print("Actual Partner Count: " + str(actual_partner_amount), \
            end = "")

            self.assertEqual(actual_partner_amount, \
            list_of_partners_count[i])
            print(" - PASS")
            print()
        print("----------------------------------------------------------------\
-------")

if __name__ == '__main__':
    unittest.main()
