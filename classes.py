class User:
    def __init__(self:str, name:str, surname:str, id:int, city:str):
        self.name = name
        self.surname = surname
        self.id = id
        self.city = city
    def show_info(self):
        print("Name is: ", self.name, "Surname is: ", self.surname, "ID is: ", self.id, "City is: ", self.city)

class balance(User):
    def __init__(self, name, surname, id, city, user_balance:int):
        super().__init__(name, surname, id, city)
        self.__user_balance = user_balance
    
    def get_balance(self):
        return self.__user_balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__user_balance = new_balance
        else:
            print("Balance cannot be negative.")

