class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.price} EUR: {self.description}"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if isinstance(product, Product) and product not in self.products:
            self.products.append(product)

    def calculator(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def __str__(self):
        cart_c = ""
        for product in self.products:
            cart_c += str(product) + "\n"

        total_s = self.calculator()

        return f"Cart Contents:\n{cart_c}Total Price: {total_s} EUR"

product1 = Product("Microphone", 100, "For notebook")
product2 = Product("notebook", 1000, "High quality")

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
print(cart)
