
import property as p

class Apartment(p.Property):
    valid_laundries = ("coin", "credit_card", "none")
    valid_balconies = ("yes", "no", "solarium")
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = p.Property.prompt_init()

        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input(
                "What laundry facilities does the property have? ({})"
                    .format(", ".join(Apartment.valid_laundries)))

        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? ""({})"
                    .format(", ".join(Apartment.valid_balconies)))

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)