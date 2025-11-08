class painter:
    def hobby(self):
        print("hooby: painting")

class Singer:
    def hobby(self):
        print("hooby: singing")

def showHobby(person):
    person.hobby()

p = painter()
s = Singer()

showHobby(p)
showHobby(s)