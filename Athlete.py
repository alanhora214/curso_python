class Athlete:

    def __init__(self,name,number):
        self.name=name
        self.number=number

    def __str__(self):
        return f"Athlete: {self.name}, Number: {self.number}"
    
    def __repr__(self):
        return f"Athlete(name='{self.name}', number={self.number})"
    
    def to_json(self):
        """
        Generate json of Athlete
        """
        return {
            "name":self.name,
            "number":self.number
        }
    
if __name__ == "__main__":
    athlete1= Athlete("Lionel Messi")
    athlete1.number=10
    print(athlete1)
    print(repr(athlete1))
