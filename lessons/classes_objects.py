"""Example of a class and object instantitation."""


class Pizza:
    """Models the idea of a Pizza."""

    #Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool

def price(pizza: Pizza) -> float:
    """Calculate the price of a Pizza."""
    total: float = 0.0
    if pizza.size == "large":
        total += 10.0
    else:
        total += 8.0

    total += pizza.toppings * 0.75

    if pizza.extra_cheese:
        total += 1.0

    return total


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False

print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${price(a_pizza)}")
