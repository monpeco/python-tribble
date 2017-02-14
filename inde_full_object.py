class SummableList(list):
    def suma( self ):
        s= 0
        for v in self.__iter__():
            s += v
            print("v: %s" % v)
        return s
        
m2 = SummableList()
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m2.append(n)
        
print(m2.suma())