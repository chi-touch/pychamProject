class Gun:
    def __init__(self, AK47, speed):
        self.AK47 = AK47
        self.capacity = speed
        self.bullets_loaded = speed
        self.toggle_indicator = False

    def load_bullets(self, number_of_bullets):
        if number_of_bullets > self.capacity:
            raise ValueError("bullet capacity exceeded")
        self.bullets_loaded = number_of_bullets

    def reload_bullets(self, number_of_bullets):
        if number_of_bullets < self.capacity:
            self.bullets_loaded = self.capacity

    def shoot_gun(self):
        if self.bullets_loaded > 0:
            self.bullets_loaded -= 1

    def safety_indicator(self):
        self.toggle_indicator = not self.toggle_indicator

    def get_number_of_bullets(self):
        return self.bullets_loaded
