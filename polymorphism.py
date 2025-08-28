from abc import ABC, abstractmethod

class Mover(ABC):
    @abstractmethod
    def move(self):
        pass

class Dragon(Mover):
    def move(self):
        print("The dragon flies through the sky!")

class Car(Mover):
    def move(self):
        print("The car is driving!")

class Plane(Mover):
    def move(self):
        print("The plane soars through the clouds!")

def main():
    movers = [Dragon(), Plane(), Car()]
    for mover in movers:
        mover.move()

if __name__ == "__main__":
    main()