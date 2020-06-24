
import utility as u
import property as p

class Rental(p.Property):
    def __init__(self, furnished='', utilities='',rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished= u.get_valid_input("Is the property furnished? ",("yes", "no")))
    prompt_init = staticmethod(prompt_init)