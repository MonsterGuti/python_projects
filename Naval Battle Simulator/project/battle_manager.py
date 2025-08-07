from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone

zone_mapper = {
    "RoyalZone": RoyalZone,
    "PirateZone": PirateZone
}

ship_mapper = {
    'RoyalBattleship': RoyalBattleship,
    'PirateBattleship': PirateBattleship
}

class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in zone_mapper:
            raise Exception("Invalid zone type!")

        if any(z.code == zone_code for z in self.zones):
            raise Exception("Zone already exists!")

        zone = zone_mapper[zone_type](zone_code)
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in ship_mapper:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship = ship_mapper[ship_type](name, health, hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if (isinstance(zone, RoyalZone) and isinstance(ship, RoyalBattleship)) or \
           (isinstance(zone, PirateZone) and isinstance(ship, PirateBattleship)):
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        zone.volume -= 1
        ship.is_available = False
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if not ship:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]

        if not attackers or not targets:
            return "Not enough participants. The battle is canceled."

        attacker = max(attackers, key=lambda s: s.hit_strength)
        target = max(targets, key=lambda s: s.health)

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            zone.volume += 1
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            zone.volume += 1
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available]
        result = []
        result.append(f"Available Battleships: {len(available_ships)}")
        if available_ships:
            names = ', '.join(s.name for s in available_ships)
            result.append(f"#{names}#")
        result.append("***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")
        for zone in sorted(self.zones, key=lambda z: z.code):
            result.append(zone.zone_info())
        return '\n'.join(result)
