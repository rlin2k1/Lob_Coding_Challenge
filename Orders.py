""" Orders.py
This module Contains the Orders Class.

Author(s):
    Roy Lin

Date Created:
    October 16th, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from SingleOrder import SingleOrder

class Orders:
    """
    Order Class - Represents Orders in the Lob Universe.

    Attributes:
        _orders_json (JSON Object): JSON Object Represented in the Orders JSON 
        File.
        _list_of_OrderItems (List): Contains Order Items in a List.
    """
    def __init__(self, orders_json):
        """
        Constructor for the Orderse Class.
        
        Args:
            self (none): None.
            roders_json (JSON Object): JSON Object Represented in the Orders 
            JSON File.
        
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._orders_json = orders_json #Can Be Useful in Future
        self._list_of_OrderItems = self.make_order_items(orders_json)

    def make_order_items(self, orders_json):
        """
        Retrieves the Order Items from the Orders Json File.
        
        Args:
            self (none): None.
            orders_json (JSON Object): JSON Object Represented in the Orders 
            JSON File.
        Returns:
            (List): Contains Order Items in a List.
        """
        rs = []
        for order in orders_json:
            #From Orders Schema (THIS MAY CHANGE), we need Object ID, Resource,
            #Object Type, Address, and Deliverability
            object_id = order['id']
            resource = order['resource']
            object_type = order['type']
            address = order['address']
            deliverability= order['deliverability']
            new_order = SingleOrder(object_id, resource, object_type, address, \
            deliverability)
            rs.append(new_order)
        return rs;

    def get_order_items(self):
        """
        Public Accessor for the Member Variable: Order Items List.
        *More Memory Efficient for Order Items if make_order_items() was 
        already called.*
        
        Args:
            self (none): None.
        Returns:
            (List): Contains Order Items in a List.
        """
        return self._list_of_OrderItems

    def get_orders_json(self):
        """
        Public Accessor for the Member Variable: Orders_Json - JSON Object.
        
        Args:
            self (none): None.
        Returns:
            (JSON Object): JSON Object Represented in the Orders JSON 
            File.
        """
        return self._orders_json