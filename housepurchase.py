

import house as h, purchase as p

class HousePurchase(p.Purchase, h.House):
    def prompt_init():
        init = h.House.prompt_init()
        init.update(p.Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)