class person:
    def _init_(self, name, age, height):
        self.age = age
        self.name = name
        self.height = height
    def get_info(self):
        print("name: ", self.name, "age: ", self.age, "heght: ", self.height)
class singer(person):
    award = None
    def _init_(self, name, age, height, grade):
        super()._init_(name, age, height)
        self.award = award
    def get_info(self):
        super().get_info()
        print("award: ", self.grade)
class painter(person):
    paintings = None
    def _init_(self, name, height, paintings):
        super()._init(name, age, height)
        self.paintings = paintings
    def get_info(self):
        super().get_info()
        print("paintings: ", self.paintings)
class grandparent(person):
    pass


singer = singer("John", 21, 190, 16)
painter = painter("Stacy", 27, 167, 24)
grandparent = grandparent("Nil", 86, 164)
singer.get_info()
painter.get_info()
grandparent.get_info()