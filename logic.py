from numpy import zeros, pad, array, uint8

class Space:
    def __init__(self):
        self.status = zeros(9, dtype=uint8)
        self.status[1] = 1
    #     pass
    def separate(self, i):
        if self.status[i]:
            if i == 0:
                self.status = pad(self.status, (1,0), 'constant', constant_values=(0,0))
            elif i == self.length - 1:
                self.status = pad(self.status, (0,1), 'constant', constant_values=(0,0))
            # try:
            # print(f"i:{i}, {self.status[i-1:i+1]}")
            else:
                self.status[i-1:i+2] += array([1,-1,1], dtype=uint8)
            # except ValueError and self.status[i-1:i+1].shape != (3,):
            #     try:
            #         statusa[]
            #     self.status
        pass
    def merge(self, i):
        if self.status[i-1] and self.status[i+1]:
            self.status[i-1:i+2] += array([-1,1,-1], dtype=uint8)
        pass
    
    @property
    def length(self):
        return len(self.status)