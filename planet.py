class Planet(object):
    def __init__(self, planet, distanceSun, diameter):
        self.planet = planet
        self.distanceSun = distanceSun
        self.diameter = diameter

    def __str__(self):
        return f"Planet: {self.planet}, Distance from Sun: {self.distanceSun}. Diameter: {self.diameter}"
