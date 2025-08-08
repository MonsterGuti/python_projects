from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant

class FlowerShopManager:
    VALID_PLANTS = {
        "Flower": Flower,
        "LeafPlant": LeafPlant,
    }

    VALID_CLIENTS = {
        "BusinessClient": BusinessClient,
        "RegularClient": RegularClient,
    }

    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")
        plant_class = self.VALID_PLANTS[plant_type]
        new_plant = plant_class(plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")
        if any(c.phone_number == client_phone_number for c in self.clients):
            raise ValueError("This phone number has been used!")
        client_class = self.VALID_CLIENTS[client_type]
        new_client = client_class(client_name, client_phone_number)
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")

        matching_plants = [p for p in self.plants if p.name == plant_name]
        if not matching_plants:
            raise ValueError("Plants not found!")
        if len(matching_plants) < plant_quantity:
            return "Not enough plant quantity."

        plants_to_sell = matching_plants[:plant_quantity]
        total_price = sum(p.price for p in plants_to_sell)
        discounted_price = total_price * (1 - client.discount / 100)
        self.income += discounted_price

        for plant in plants_to_sell:
            self.plants.remove(plant)

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {discounted_price:.2f}"

    def remove_plant(self, plant_name: str):
        plant = next((p for p in self.plants if p.name == plant_name), None)
        if plant is None:
            return "No such plant name."
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        removed = [c for c in self.clients if c.total_orders == 0]
        self.clients = [c for c in self.clients if c.total_orders > 0]
        return f"{len(removed)} client/s removed."

    def shop_report(self):
        report = "~Flower Shop Report~\n"
        report += f"Income: {self.income:.2f}\n"
        total_orders = sum(c.total_orders for c in self.clients)
        report += f"Count of orders: {total_orders}\n"
        report += f"~~Unsold plants: {len(self.plants)}~~\n"

        plant_counts = {}
        for plant in self.plants:
            plant_counts[plant.name] = plant_counts.get(plant.name, 0) + 1

        sorted_plants = sorted(plant_counts.items(), key=lambda x: (-x[1], x[0]))
        for name, count in sorted_plants:
            report += f"{name}: {count}\n"

        report += f"~~Clients number: {len(self.clients)}~~\n"
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        for client in sorted_clients:
            report += client.client_details() + "\n"

        return report.strip()
