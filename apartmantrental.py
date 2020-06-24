
import rental as r, apartment as a

class ApartmentRental(r.Rental, a.Apartment):
    def prompt_init():
        init = a.Apartment.prompt_init()
        init.update(r.Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

