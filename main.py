from Models import Company, Product, Basket


c1 = Company("Apple", 1990)
pr1 = Product("16 pro", 1200, 10, c1)
pr2 = Product("16 pro", 1200, 2, c1)
pr3 = Product("17 pro", 2000, 2, c1)
pr4 = Product("16 pro", 1200, 7, c1)
b = Basket()

b.add_product(pr1)
b.add_product(pr2)
b.add_product(pr3)
b.add_product(pr4)

b.view_products()