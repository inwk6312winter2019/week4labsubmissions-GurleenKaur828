class Time():
	hour=4
	minute=23
	second=27
time=Time()

def print_time(t):
	return('{:02}:{:02}:{:02}'.format(t.hour,t.minute,t.second))

print(print_time(time))



