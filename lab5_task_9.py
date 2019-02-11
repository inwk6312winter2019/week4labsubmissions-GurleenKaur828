class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass
for x in [Vehicle, LandVehicle, TrackedVehicle]:
	for y in [Vehicle, LandVehicle, TrackedVehicle]:
		print(issubclass(x,y))
	print()

