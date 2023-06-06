from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self._engine: Engine
        self._battery: Battery
        self._tire: Tire

    @abstractmethod
    def needs_service() -> bool:
        pass


class Engine(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class Battery(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class Tire(ABC):
    def __init__(self, sensors_status: list):
        self.sensors_status = sensors_status

    @abstractmethod
    def needs_service() -> bool:
        pass