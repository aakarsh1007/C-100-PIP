class Car(object):
    def __init__(self, company, model, color, speedLimit):
        self.company = company
        self.model = model
        self.color = color
        self.speedLimit = speedLimit

    def start(self):
        print(f"car {self.company} has started")
        
    def stop(self):
        print("car has stopped")

    def accelerate(self):
        print("car has acclerated")

    def changeGear(self):
        print("car has changed gears")

    
audi = Car("Audi", "Q7", "Blue", "240kmph")

audi.start()
audi.accelerate()
audi.changeGear()
audi.stop()

toyota = Car("Toyota", "Fortuner", "White", "210kmph")
toyota.start()
