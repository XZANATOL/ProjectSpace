from datetime import datetime

from interfaces import Car

class Thovex(Car):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if any([
            service_threshold_date < datetime.today().date(),
            self.engine.needs_service(),
            self.battery.needs_service()
            ]):
            return True
        else:
            return False
