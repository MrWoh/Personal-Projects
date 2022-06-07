from estate_project.models.building import Building


class House(Building):
    def __init__(self, city, neighborhood, area, room_number, heating):
        super().__init__(self, city, neighborhood, area, room_number)
        self.heating = heating

    def __str__(self):
        return f'{self.city, self.neighborhood, self.street, self.area, self.room_number, self.heating}'
