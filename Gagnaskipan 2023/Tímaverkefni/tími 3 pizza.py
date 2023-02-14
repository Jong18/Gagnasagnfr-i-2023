

class Pizza_class:
    def __init__(self, topping):
        self.topping = topping
        self.status = 'Unserved'
        self.pizza = {}



    def toppings(self, topping, status, pizza):
        generated_ID = self.generating_ID(pizza)
        self.pizza.update({generated_ID: topping})
        
    def generating_ID(self, pizza: dict):
        for key in pizza:
            if key == None:
                pizza.update({1:None})
            else:
                key += 1
                pizza.update({key:None})
        return pizza

    def __str__(self) -> str:
        return f""



