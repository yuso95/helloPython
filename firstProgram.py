import sys

class Animal:
    def __init__(self, name, legCount):
        self._name = name
        self._legCount = legCount

    def saySomething(self, voice):
        return str(self._name) + "said that " + str(voice)

    def __str__(self):
        a = "This animal is a " + str(self._name) 
        b = ". It has " + str(self._legCount) + " legs"
        return a + b
def main():
    name = sys.stdin.readline()
    legCount = sys.stdin.readline()

    cat = Animal(name, legCount)

    print(cat


if __name__ == "__main__":
    main()

