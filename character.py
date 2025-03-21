class Character:
    def __init__(self, combat_strength, health_points):
        self._combat_strength = combat_strength
        self._health_points = health_points

    def __del__(self):
        print("The Character is being destroyed")

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self._health_points = value
