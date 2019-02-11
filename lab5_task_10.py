class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass
vehicle = Vehicle()
landvehicle = LandVehicle()
trackedvehicle = TrackedVehicle()

for x in [vehicle, landvehicle, trackedvehicle]:
	for X in [Vehicle, LandVehicle, TrackedVehicle]:
		print(isinstance(x,X))
	print()
