class Time: 
    def __init__(self, h = 0, m= 0 ):
        self.hrs = h 
        self.min = m

    def __add__(self, rhs):
        result = Time(0, 0)
        result.hrs = self.hrs + rhs.hrs # could replace lhs with self 
        result.min = self.min + rhs.min 
        if result.min > 60: 
            result.min -= 60 
            result.hrs += 1

        return result
        

t = Time(4, 50)
t1 = Time(3, 20)
t2 = Time(1, 45)

t = t1 + t2 # ULTIMATE OBJECTIVE  to get this to work 
#t = Time.__add__(t1, t2)
print(t)