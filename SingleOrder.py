""" SingleOrder.py
This module contains the SingleOrder Class.

Author(s):
    Roy Lin

Date Created:
    October 16th, 2018
"""
class SingleOrder:
    """
    SingleOrder Class - Represents a Order Item in the Lob Orders List
    
    Attributes:
        _order_id (String): The ID of the Order Being Purchased.
        _resource (String): The resource that the Order needs.
        _order_type (String): The type of the order.
        _latitude (Integer): The latitude of the Current Order.
        _longitude (Integer): The longitude of the Current Order.
        _deliverability (String): The Deliverability Status of the item.
    
    """
    def __init__(self, order_id, resource, order_type, address, deliverability):
        """
        Constructor for the SingleOrder Class.
        
        Args:
            self (none): None.
            order_id (String): The ID of the Order Being Purchased.
            resource (String): The resource that the Order 
            needs.
            order_type (String): The type of the order.
            address (Key-value pairs of Latitude and Longitude): The address of 
            the Current Order.
            deliverability (String): The Deliverability Status of the item.
        
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._order_id = order_id
        self._resource = resource
        self._order_type = order_type
        self._latitude = address['latitude']
        self._longitude = address['longitude']
        self._deliverability = deliverability

    def get_order_id(self):
        """
        Public Accessor for the Member Variable: Order ID.
        
        Args:
            self (none): None.
        Returns:
            (String):The ID of the Order Being Purchased.
        """
        return self._order_id
    
    def get_resource(self):
        """
        Public Accessor for the Member Variable: Resource.
        
        Args:
            self (none): None.
        Returns:
            (String): The resource that the Order needs.
        """
        return self._resource

    def get_order_type(self):
        """
        Public Accessor for the Member Variable: Order Type.
        
        Args:
            self (none): None.
        Returns:
            (String): The type of the order.
        """
        return self._order_type

    def get_latitude(self):
        """
        Public Accessor for the Member Variable: Latitude.
        
        Args:
            self (none): None.
        Returns:
            (Integer): The latitude of the Current Order.
        """
        return self._latitude

    def get_longitude(self):
        """
        Public Accessor for the Member Variable: Longitude.
        
        Args:
            self (none): None.
        Returns:
            (Integer): The longitude of the Current Order.
        """
        return self._longitude
    
    def get_deliverabiliy(self):
        """
        Public Accessor for the Member Variable: Deliverability.
        
        Args:
            self (none): None.
        Returns:
            (Integer): The Deliverability Status of the item.
        """
        return self._deliverability