from ninja import *
from pets import *

ninja = Ninja('Rubeus', 'fluffy', 'treats', 'canned food', pet('fang', 'dog'))

ninja.walk().feed().bath()

buckbeak = serviceAnimals("buckbeak", "hippogriff")
buckbeak.job("protect")
buckbeak.job("calm")
