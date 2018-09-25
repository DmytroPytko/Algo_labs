class Putivka:

    def __init__(self, country, duration, price):
        self.country = country
        self.duration = duration
        self.price = price

    def __repr__(self):
        return "Country " + self.country + ", duration " + str(self.duration) + ", " + str(self.price)


