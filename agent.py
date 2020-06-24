

import houserental as hr
import housepurchase as hp
import apartmantrental as ar
import apartmantpurhase as ap
import utility as u

class Agent():
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): hr.HouseRental,
        ("house", "purchase"): hp.HousePurchase,
        ("apartment", "rental"): ar.ApartmentRental,
        ("apartment", "purchase"): ap.ApartmentPurchase
    }

    def add_property(self):
        property_type = u.get_valid_input("What type of property? ",("house", "apartment")).lower()
        payment_type = u.get_valid_input("What payment type? ",("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

agent = Agent()
agent.add_property()
agent.display_properties()