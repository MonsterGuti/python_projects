from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        ships = self.get_ships()
        pirate_ships = [s for s in ships if isinstance(s, PirateBattleship)]

        result = [
            "@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {len(ships)}, {len(pirate_ships)} out of them are Pirate Battleships."
        ]

        if ships:
            names = ", ".join(ship.name for ship in ships)
            result.append(f"#{names}#")

        return "\n".join(result)

