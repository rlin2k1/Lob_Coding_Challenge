""" fix_routing_problem.py
The Great Routing Problem Program - Outputs Which Partner of Lob with Take Care
of Which Order

USAGE: python3 fix_routing_problem.py -p /PATHTOPARTNERJSON -o /PATHTOORDERJSON

Author(s):
    Roy Lin

Date Created:
    October 16th, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
import argparse #For Argument Parsing
import json #For JSON Parsing

from Orders import Orders #For Order Class Containing Order Items
from PartnersDB import PartnersDB #For Partners DataBase Creation
from OrderCalculator import OrderCalculator #Order Calculator Class - Find Match
# ---------------------------------------------------------------------------- #
# Helper Functions for Order Calculator
# ---------------------------------------------------------------------------- #
def return_json_data(path_to_file):
    """
    Returns the JSON Object for Use with Python's JSON Library.
    
    Args:
        path_to_file (String): File Path to JSON File.
    Returns:
        (JSON Object): JSON Object Represented in the JSON File.
    """
    try:
        opened_file = open(path_to_file, 'r')
        json_object = json.load(opened_file)
        return json_object
    except:
        print("Cannot Open the Path to " + path_to_file)
        exit(1)

def main():
    """
    main Function for the Lob Coding Challenge of Calculating which Partner gets
    what Order.
    
    Args:
        self (none): None.
    Returns:
        (void): No return value. Just prints the Orders that Goes with Certain
        Partners.
    """
    # ------------------------------------------------------------------------ #
    # Constructs Argument Parser for Parsing Arguments
    # ------------------------------------------------------------------------ #
    argument_parser = argparse.ArgumentParser(description='Order Calculator')
    argument_parser.add_argument("-o", "--orders", required=True, \
    help="PATH TO ORDERS JSON")
    argument_parser.add_argument("-p", "--partners", required=True, \
    help="PATH TO PARTNERS JSON")

    arguments = vars(argument_parser.parse_args())

    # ------------------------------------------------------------------------ #
    # Get and Load JSON Paths for Orders and Partners
    # ------------------------------------------------------------------------ #
    path_to_orders = arguments['orders']
    path_to_partners = arguments['partners']

    orders_json = return_json_data(path_to_orders)
    partners_json = return_json_data(path_to_partners)

    # ------------------------------------------------------------------------ #
    # Initialize Orders with Each Order Item
    # ------------------------------------------------------------------------ #
    lob_orders = Orders(orders_json)

    # ------------------------------------------------------------------------ #
    # Intialize Partners DataBase
    # ------------------------------------------------------------------------ #
    partners_db = PartnersDB(partners_json)

    # ------------------------------------------------------------------------ #
    # Initialize Order Calculator
    # ------------------------------------------------------------------------ #
    order_calculator = OrderCalculator(lob_orders, partners_db)

    # ------------------------------------------------------------------------ #
    # Output Each Order for Each Partner
    # ------------------------------------------------------------------------ #
    file = open(path_to_orders.split('.')[0] + '.txt', 'w')
    partner_order_dict = (order_calculator.get_partner_orders())
    for key, value in partner_order_dict.items():
        file.write(key + '\n') 
        for order in value:
            file.write(order + '\n')
    return

if __name__ == '__main__':
    main()