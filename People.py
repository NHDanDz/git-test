class People:
    def __init__(self, EmCode, Name, Date, Pos, Sal):
        self.EmCode = EmCode
        self.Name = Name
        self.Date = Date
        self.Pos = Pos
        self.Sal = Sal   
    def to_list(self):
        return [self.EmCode, self.Name, self.Date, self.Pos, self.Sal]