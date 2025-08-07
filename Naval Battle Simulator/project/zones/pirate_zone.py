from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone

class PirateZone(BaseZone):
    INITIAL_VOLUME = 8  # Fix to 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        ships = self.get_ships()
        royal_ships = [s for s in ships if isinstance(s, RoyalBattleship)]

        result = [
            "@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {len(ships)}, {len(royal_ships)} out of them are Royal Battleships."
        ]

        if ships:
            names = ", ".join(ship.name for ship in ships)
            result.append(f"#{names}#")

        return "\n".join(result)
