
# abstract.py
# Real-world Example: Transport System (Abstract Classes)

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Bus(Transport):
    def start(self):
        print("Bus engine started. Ready for passengers.")

    def stop(self):
        print("Bus stopped at the station.")

class Train(Transport):
    def start(self):
        print("Train departed from the station.")

    def stop(self):
        print("Train arrived at the station.")

if __name__ == "__main__":
    bus = Bus()
    train = Train()
    for vehicle in [bus, train]:
        vehicle.start()
        vehicle.stop()
