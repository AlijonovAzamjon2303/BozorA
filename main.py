from Models import Company, Product, Basket

menu = ("1.Add\n"
        "2.View\n"
        "3.Remove\n"
        "4.Total\n"
        "5.Exit\n")
basket = Basket()

while True:
    print(menu)
    choice = input(">>> ")
    if choice == "1":
        company = Company("Company", 2025)
        name = input("name = ")
        price = int(input("price = "))
        amount = int(input("amount = "))
        product = Product(name, price, amount, company)
        basket.add_product(product)
    elif choice == "2":
        basket.view_products()
    elif choice == "3":
        product_name = input("O'chiriladigan name = ")
        basket.remove(product_name)
    elif choice == "4":
        print(basket.total())