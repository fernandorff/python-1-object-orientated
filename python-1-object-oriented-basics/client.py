class Client:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("GET -> @property name()")
        return self.__name.title()

    @name.setter
    def name(self, name):
        print("SET -> name()")
        self.__name = name


client_1 = Client("yujo")
print(client_1.name)
client_1.name = "haze"
print(client_1.name)
