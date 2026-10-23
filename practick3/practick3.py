class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def reduce_stock(self, quantity):
        if self.stock - quantity >= 0:
            self.stock -= quantity
            print(f"{self.name} осталось {self.stock}")
            return True
        else:
            print(f"Этого товара слишком мало")
            return False


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items.keys() and product.stock >= quantity:
            self.items[product] = self.items[product] + quantity
        elif product.stock >= quantity:
            self.items[product] = quantity
        else:
            print(f"Этого товара слишком мало")

    def remove_item(self, product):
        if product in self.items.keys():
            self.items.pop(product)
        else:
            print('Такого товара нет в корзине')

    def update_quantity(self, product, quantity):
        if product in self.items.keys():
            self.items[product] = quantity
        else:
            print('Такого товара нет в корзине')

    def get_total_price(self):
        total = 0
        for k in self.items.keys():
            total += k.price * self.items[k]

        return total

    def clear(self):
        self.items.clear()


class Order:
    def __init__(self, order_id, customer, items):
        super().__init__()
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.final_price = 0

    def calculate_final_price(self, discount_percent, tax_percent):
        base_price = 0
        for product, quantity in self.items.items():
            base_price += product.price * quantity

        self.final_price = (base_price * (1 - discount_percent / 100)) * (1 + tax_percent / 100)
        return self.final_price

    def process_order(self):
        for p in self.items.keys():
            p.reduce_stock(self.items[p])


class Customer:
    def __init__(self, name, email, cart, order_history):
        super().__init__()
        self.name = name
        self.email = email
        self.cart = cart
        self.order_history = order_history

    def checkout(self, order_id, discount=0, tax=0):
        if not self.cart.items:
            print("Корзина пуста")
            return

        items_copy = self.cart.items.copy()
        new_order = Order(order_id, self, items_copy)
        new_order.calculate_final_price(discount, tax)
        print(f"Итоговая цена заказа №{order_id} со скидкой {discount}% и налогом {tax}%: {new_order.final_price}")
        new_order.process_order()
        self.order_history.append(new_order)
        self.cart.clear()
