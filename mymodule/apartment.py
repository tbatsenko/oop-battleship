# file: apartment.py

from .property import Property
from .funcs import get_valid_input


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        This method initializes a new Apartment instance, which inherits from
        Property when calls super().__init__(*kwargs) method.
        :param balcony: type of balcony of instance.
        :param laundry: type of laundry of instance.
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        (self) -> (None)
        This method calls a parent class method display (Property) and then
        prints out an Apartment instance details specific for Apartment class.
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    @staticmethod
    def prompt_init():
        """
        This method asks user to enter appropriate info for Apartment instance:
        first it calls parent method and then asks for additional info, which
        characterizes an Apartment instance - laundry and balcony.
        :return: (dict{(str):(str) })
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does "
                                  "the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
