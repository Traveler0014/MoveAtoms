import numpy as np

class Space:
    # def __init__(self):
    #     self.space = 
    #     pass
    def separate(self, i):
        if self.status[i]:
            # try:
            self.status[i-1:i+1] += np.array([1,-1,1])
            # except ValueError and self.status[i-1:i+1].shape != (3,):
            #     try:
            #         statusa[]
            #     self.status
        pass
    def merge(self, i):
        if self.status[i-1] and self.status[i+1]:
            self.status[i-1:i+1] += np.array([-1,1,-1])
        pass