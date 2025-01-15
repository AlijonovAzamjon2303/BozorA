class Company:
    def __init__(self, name, yil):
        self.name = name
        self.yil = yil

    def __str__(self):
        return f"{self.name} - {self.yil}yy"

class Product:
    def __init__(self, name, price, quantity, company):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.company = company

    def __str__(self):
        return f"{self.company.name}|{self.name} -- {self.quantity}x{self.price}"

class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for item in self.products:
            if item.name == product.name:
                item.quantity += product.quantity
                return
        self.products.append(product)

    def view_products(self):
        for product in self.products:
            print(product)