
import rental as r, house as h

class HouseRental(r.Rental, h.House):
    def prompt_init():
        init = h.House.prompt_init()
        init.update(r.Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)