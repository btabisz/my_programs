

class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1


    @property
    def mood(self):
        unhappyness = self.hunger + self.boredom
        if unhappyness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappyness <= 10:
            m = "zadowolony"
        elif 11 <= unhappyness <= 15:
            m = "zły"
        else:
            m = "wściekły"
        return m


    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()


    def eat(self, food = 4):
        print("Pychota, dziekuję!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger =0
        self.__pass_time()


    def play(self, fun = 4):
        print("Hurrra!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Podaj imię zwierzaka:")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print("""
        0-zakończ
        1-słuchaj zwierzaczka
        2-nakarm zwierzaczka
        3-pobaw się ze zwierzaczkiem     
        """)
        choice = input("Co wybierasz?")

        if choice == "0":
            print("Do widzenia")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Niestety", choice, "nie jest prawidłowym wyborem")

main()