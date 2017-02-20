# File: house.py
from .property import Property
from .funcs import get_valid_input


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        """
        This method initializes a new House instance, which inherits from
        Property when calls super().__init__(*kwargs) method.
        :param garage: type of garage of instance.
        :param fenced: type of fence of instance.
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        (self) -> (None)
        This method calls a parent class method display (Property) and then
        prints out a House instance details specific for the House class.
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    @staticmethod
    def prompt_init():
        """
        This method asks user to enter appropriate info for House instance:
        first it calls parent method and then asks for additional info,
        which characterizes a House instance - fence, garage and number of
        stories.
        :return: (dict{(str): (str)})
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
