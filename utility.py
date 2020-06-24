
import property as p
import apartment as a

def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def prompt_init():
    parent_init = p.Property.prompt_init()
    laundry = get_valid_input("What laundry facilities does the property have? ",a.Apartment.valid_laundries)
    balcony = get_valid_input("Does the property have a balcony? ",a.Apartment.valid_balconies)
    parent_init.update({
        "laundry": laundry,
        "balcony": balcony
    })
    return parent_init
prompt_init = staticmethod(prompt_init)