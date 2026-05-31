class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int) or capacity < 0: 
            raise ValueError("Invalid input")
        self._capacity = capacity
        self._size=0

    def __str__(self):
        streng=""
        for i in range(self._size):
            streng=streng+"🍪"
        return streng
    
    def deposit(self, n):
        if self._size+n > self._capacity:
            raise ValueError("Exceeds capacity")
        self._size+=n

    def withdraw(self, n):
        if self._size-n < 0:
            raise ValueError("More than we have")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size