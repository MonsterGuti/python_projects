from products.chair import Chair
from products.hobby_horse import HobbyHorse
from stores.furniture_store import FurnitureStore
from stores.toy_store import ToyStore
from stores.base_store import BaseStore
from products.base_product import BaseProduct

class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            product = Chair(model, price)
        elif product_type == "HobbyHorse":
            product = HobbyHorse(model, price)
        else:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type == "FurnitureStore":
            store = FurnitureStore(name, location)
        elif store_type == "ToyStore":
            store = ToyStore(name, location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        suitable_products = [p for p in products if p.sub_type == store.store_type]

        if not suitable_products:
            return "Products do not match in type. Nothing sold."

        for product in suitable_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price

        return f"Store {store.name} successfully purchased {len(suitable_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        filtered = [p for p in self.products if p.model == product_model]
        for p in filtered:
            p.discount()
        return f"Discount applied to {len(filtered)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}"
        ]

        product_counts = {}
        for p in self.products:
            product_counts[p.model] = product_counts.get(p.model, 0) + 1

        for model in sorted(product_counts):
            result.append(f"{model}: {product_counts[model]}")

        result.append(f"***Partner Stores: {len(self.stores)}***")
        for s in sorted(self.stores, key=lambda x: x.name):
            result.append(s.name)

        return "\n".join(result)
