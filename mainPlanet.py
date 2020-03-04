from planet import Planet
from Planetarium import Planetarium


earth = Planet("Earth", 92960000, 7917)
mercury = Planet("Mercury", 35980000, 3031)
venus = Planet("Venus", 67240000, 7520)
mars = Planet("Mars", 141600000, 4212)
jupiter = Planet("Jupiter", 483800000, 86881)
saturn = Planet("Saturn", 890800000, 72367)
uranus = Planet("Uranus", 1784000000, 31518)
neptune = Planet("Neptune", 2793000000, 30599 )
pln = Planetarium()

pln.add_planet(venus)
pln.add_planet(earth)
pln.add_planet(mercury)
pln.add_planet(mars)
pln.add_planet(jupiter)
pln.add_planet(saturn)
pln.add_planet(uranus)
pln.add_planet(neptune)

print(str(pln))
