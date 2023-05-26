class Challenge:
    name: str
    description: str
    category: str
    points: int
    flag: str

    def __init__(self, name, description, category, points, flag):
        self.name = name
        self.description = description
        self.category = category
        self.points = points
        self.flag = flag

    def checkFlag(self, flag):
        return flag == self.flag
