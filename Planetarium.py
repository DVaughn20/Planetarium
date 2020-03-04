from planet import Planet


class Planetarium(object):
    def __init__(self):
        self.planets = []

    def __str__(self):
        return '[' + ', \n '  .join(str(planet) for planet in self.planets) + ']'

    def add_planet(self, planet):
        self.planets.append(planet)





