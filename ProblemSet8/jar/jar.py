class Jar:
    def __init__(self, capacity=12):
        if type(capacity)!=int or capacity<0:
            raise ValueError("Wrong input")
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return ("🍪"*self.size)

    def deposit(self, n):
        if type(n)!=int or n<0 or self.size+n>self.capacity:
            raise ValueError("Not enough capacity to store cookies")
        self.size+=n

    def withdraw(self, n):
        if type(n)!=int or n<0 or self.size-n<0:
            raise ValueError("Not enough cookies")
        self.size-=n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,n):
        self._capacity=n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,n):
        self._size=n
