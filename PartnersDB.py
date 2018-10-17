""" PartnersDB.py
This module contains the PartnersDB Class.

Author(s):
    Roy Lin

Date Created:
    October 16th, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from SingleOrder import SingleOrder
import sys
from collections import OrderedDict #Partners Listed in Order
from scipy.spatial import distance as dist #Distances

class PartnersDB:
    """
    PartnersDB Class - Represents a Database for Partners.
    
    Attributes:
        _partners_json (JSON Object): JSON Object Represented in the Partners
        JSON File.
        _partners_count (Integer): The Count of the Number of Partners in the
        JSON
        _empty_ordered_dict (Ordered Dict Object): The Ordered Dictionary 
        Representing the Partners in Order.
    """
    def __init__(self, partners_json):
        """
        Constructor for the PartnersDB Class.
        
        Args:
            self (none): None.
            partners_json (JSON Object): JSON Object Represented in the Partners
            JSON File.
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._partners_json = partners_json
        self._partners_count = self.calculate_partners_count(partners_json)
        self._empty_ordered_dict = self.make_ordered_partners(partners_json)
    
    def make_ordered_partners(self, partners_json):
        """
        Makes an Ordered Dictionary Based on the Partners in the Partners JSON
        Object.
        
        Args:
            partners_json (JSON Object): JSON Object Represented in the Partners
            JSON File.
        Returns:
            (Ordered Dict Object): The Ordered Dictionary Representing the 
            Partners in Order.
        """
        ordered_dict = OrderedDict()
        for partner in partners_json:
            ordered_dict[ partner['id'] ] = []
        return ordered_dict
    
    def get_ordered_partners(self):
        """
        Public Accessor for the Member Variable: Partners Ordered Dictionary
        *More Memory Efficient for PartnersDB if make_ordered_partners()
        was already called.*

        Args:
            self (none): None.
        Returns:
            (Ordered Dict Object): The Ordered Dictionary Representing the 
            Partners in Order.
        """
        return self._empty_ordered_dict

    def calculate_partners_count(self, partners_json):
        """
        Calculates How Many Different Partners there are in the Parters DB.
        
        Args:
            self (none): None.
            partners_json (JSON Object): JSON Object Represented in the Partners
            JSON File.
        Returns:
            (Integer): Count of Different Partners.
        """
        count = 0
        for partner in partners_json:
            count = count + 1
        return count

    def get_partners_count(self):
        """
        Public Accessor for the Member Variable: Partner Count - Integer.
        *More Memory Efficient for PartnersDB if calculate_partners_count()
        was already called.*
        
        Args:
            self (none): None.
        Returns:
            (Integer): Count of Different Partners.
        """
        return self._partners_count
    
    def get_partners_json(self):
        """
        Public Accessor for the Member Variable: Partners_Json - JSON Object.
        
        Args:
            self (none): None.
        Returns:
            (JSON Object): JSON Object Represented in the Partners JSON File.
        """
        return self._partners_json

    def get_optimum_partner(self, order):
        """
        Returns the Optimum Partner in Relation if the Order Can Be Completed
        by Said Partner in the Shortest Distance.
        
        Args:
            self (none): None.
            order (SingleOrder): Represents a Order Item in the Lob Universe.
        Returns:
            (String): The Optimum Partner ID as a String. 
            Sentinel: Returns Empty String if ERROR and Partner Cannot Be Found.
        """
        optimum_partner = ""
        minimum_distance = sys.maxsize
        for partner in self._partners_json:
            if (order.get_resource() == partner['resource']) and \
            (order.get_order_type() in partner['type']) and \
            partner['capacity'] > 0:
                current_distance = dist.euclidean((order.get_latitude(), \
                order.get_longitude()), (partner['address']['latitude'], \
                partner['address']['longitude']))
                if(current_distance < minimum_distance):
                    minimum_distance = current_distance
                    optimum_partner = partner
        if(optimum_partner == ""):
            return ""
        optimum_partner['capacity'] = optimum_partner['capacity'] - 1
        return optimum_partner['id']