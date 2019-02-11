class Time():
        hour=6
        minute=9
        seconds=34
time1=Time()
time2=Time()
time2.hour=7
time2.minute=7
time2.seconds=47
def print_time(t):
        return ('{:02}:{:02}:{:02}'.format(t.hour,t.minute,t.seconds))

t1=print_time(time1)
t2=print_time(time2)
print(t1)
print(t2)

def is_after(n1,n2):
	return n1 > n2
print(is_after(t1,t2))

