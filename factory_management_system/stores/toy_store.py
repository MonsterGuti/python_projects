from stores.base_store import BaseStore

class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)

    @property
    def store_type(self):
        return "Toys"

    def store_stats(self):
        stats = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                 self.get_estimated_profit(),
                 "**Toys for sale:"]

        model_counts = {}
        for p in self.products:
            model_counts.setdefault(p.model, []).append(p.price)

        for model in sorted(model_counts):
            prices = model_counts[model]
            avg_price = sum(prices) / len(prices)
            stats.append(f"{model}: {len(prices)}pcs, average price: {avg_price:.2f}")

        return "\n".join(stats)
