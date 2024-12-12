from abc import ABC, abstractmethod

# Базовый класс GameObject
class GameObject(ABC):
    def __init__(self, object_id: int, name: str, x: int, y: int):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

# Интерфейс Attacker
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

# Интерфейс Moveable
class Moveable(ABC):
    @abstractmethod
    def move(self, x: int, y: int):
        pass

# Класс Unit
class Unit(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int, hp: float):
        super().__init__(object_id, name, x, y)
        self._hp = hp

    def is_alive(self) -> bool:
        return self._hp > 0

    def get_hp(self) -> float:
        return self._hp

    def receive_damage(self, damage: float):
        self._hp = max(0, self._hp - damage)

# Класс Archer
class Archer(Unit, Attacker, Moveable):
    def __init__(self, object_id: int, name: str, x: int, y: int, hp: float, damage: float):
        super().__init__(object_id, name, x, y, hp)
        self._damage = damage

    def attack(self, unit):
        if self.is_alive():
            unit.receive_damage(self._damage)

    def move(self, x: int, y: int):
        if self.is_alive():
            self._x = x
            self._y = y

# Класс Building
class Building(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int, built: bool):
        super().__init__(object_id, name, x, y)
        self._built = built

    def is_built(self) -> bool:
        return self._built

# Класс Fort
class Fort(Building, Attacker):
    def __init__(self, object_id: int, name: str, x: int, y: int, built: bool, damage: float):
        super().__init__(object_id, name, x, y, built)
        self._damage = damage

    def attack(self, unit):
        if self.is_built():
            unit.receive_damage(self._damage)

# Класс MobileHouse
class MobileHouse(Building, Moveable):
    def __init__(self, object_id: int, name: str, x: int, y: int, built: bool):
        super().__init__(object_id, name, x, y, built)

    def move(self, x: int, y: int):
        if self.is_built():
            self._x = x
            self._y = y

# Пример использования
if __name__ == "__main__":
    archer = Archer(1, "Archer1", 0, 0, 100, 15)
    enemy = Unit(2, "Enemy", 5, 5, 50)

    print(f"Enemy HP before attack: {enemy.get_hp()}")
    archer.attack(enemy)
    print(f"Enemy HP after attack: {enemy.get_hp()}")
