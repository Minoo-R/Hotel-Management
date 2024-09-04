class guest():
    def __init__(self, fullname, phoneNumber, email, roomType, roomNumber, duration, paymentMethod):
        self.fullname = fullname
        self.phoneNumber = phoneNumber
        self.email = email
        self.roomType = roomType
        self.roomNumber = int(roomNumber)
        self.duration = int(duration)
        self.paymentMethod = paymentMethod

    def to_list(self):
        return [self.fullname, self.phoneNumber, self.email, self.roomType, self.roomNumber, self.duration, self.paymentMethod]

    def __str__(self):
        return f"{self.fullname}, {self.phoneNumber}, {self.email}, {self.roomType}, {self.roomNumber}, {self.duration}, {self.paymentMethod}"

    def __repr__(self):
        return self.__str__()
