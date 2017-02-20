# File: property.py


class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        This method initializes a new Property instance.
        :param square_feet: square footage of instance.
        :param beds: amount of bedrooms in instance.
        :param baths: amount of bathrooms in instance.
        :param kwargs: this allows method to take unlimited amount of arguments
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        """
        (self) -> (None)
        This method prints out a Property instance details.
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square_footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.beds))
        print("bathrooms: {}".format(self.baths))
        print()

    @staticmethod
    def prompt_init():
        """
        This method asks user to enter appropriate info for Property instance.
        :return: (dict{(str):(str) })
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter amount of baths: "))

