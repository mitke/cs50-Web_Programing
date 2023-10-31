class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []
    
  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True
    
  def open_seats(self):
    return self.capacity - len(self.passengers)
  
flight_853 = Flight(3)

people = ["Herry", "Ron", "Hermione", "Ginny", "Mile", "Žile"]

for person in people:
  if flight_853.add_passenger(person):
    print(f"Added {person} to flight 853 successfully")
  else:
    print(f"No available seats for {person}")
