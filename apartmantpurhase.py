
import purchase as p, apartment as a

class ApartmentPurchase(p.Purchase, a.Apartment):
    def prompt_init():
        init = a.Apartment.prompt_init()
        init.update(p.Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


