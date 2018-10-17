""" OrderCalculator.py
This module contains the OrderCalculator Class.

Author(s):
    Roy Lin

Date Created:
    October 16th, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from Orders import Orders
from PartnersDB import PartnersDB

class OrderCalculator:
    """
    OrderCalculator Class - Calculator for Which Orders go With Which Partners
    in the Lob Universe.
    
    Attributes:
        _partner_orders_dict (Ordered Dict): Represents the Ordered Dictionary
        Connecting Partners with a List of Orders
        *(Can Be Easily Extendible for Other Features as Well)*
    """
    def __init__(self, orders, partners_db):
        """
        Constructor for the OrderCalculator Class.
        
        Args:
            self (none): None.
            orders (Orders): Orders Object Representing a List of SingleOrders.
            partners_db (PartnersDB): PartnersDB Object Containing the
            Partners of Lob.
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._partner_orders_dict = self.set_partner_orders(orders, \
        partners_db)

    def set_partner_orders(self, orders, partners_db):
        """
        Sets the Orders with the Correct Partners.
        
        Args:
            self (none): None.
            orderse (Orders): Orders Object Representing a List of SingleOrders.
            partners_db (PartnersDB): PartnersDB Object Containing the
            Partners of Lob.
        Returns:
            (Ordered Dict): Represents the Ordered Dictionary Connecting 
            Partners with a List of Orders
        """
        partner_orders_dict = partners_db.get_ordered_partners()
        order_items = orders.get_order_items()
        for order in order_items:
            if(order.get_deliverabiliy() != "deliverable"):
                continue
            optimum_partner = partners_db.get_optimum_partner(order)
            if(optimum_partner == -1):
                continue
            partner_orders_dict[optimum_partner].append(order.get_order_id())

        return partner_orders_dict

    def get_partner_orders(self):
        """
        Public Accessor for the Member Variable: Partner - Orders Dictionary
        *More Memory Efficient for Partners if set_partner_orders()
        was already called.*
        
        Args:
            self (none): None.
        Returns:
            (Ordered Dict): Represents the Ordered Dictionary Connecting 
            Partners with a List of Orders
        """
        return self._partner_orders_dict