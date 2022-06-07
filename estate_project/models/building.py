class Building:

    def __init__(self, city, neighborhood, area, room_number):
        self.city = city
        self.neighborhood = neighborhood
        self.area = area
        self.room_number = room_number

    def __str__(self):
        return f'{self.city, self.neighborhood, self.street, self.area, self.room_number}'


