import numpy as np

class Problem:
    def __init__ ( self ):
        self.n_vars = 250
        self.capacity = 150
        self.weight = [
            42, 69, 67, 57, 93, 90, 38, 36, 45, 42, 33, 79, 27, 57, 44, 84, 86, 92, 46, 38, 85,
            33, 82, 73, 49, 70, 59, 23, 57, 72, 74, 69, 33, 42, 28, 46, 30, 64, 29, 74, 41, 49, 55, 98, 80, 32, 25, 38,
            82, 30, 35, 39, 57, 84, 62, 50, 55, 27, 30, 36, 20, 78, 47, 26, 45, 41, 58, 98, 91, 96, 73, 84, 37, 93, 91,
            43, 73, 85, 81, 79, 71, 80, 76, 83, 41, 78, 70, 23, 42, 87, 43, 84, 60, 55, 49, 78, 73, 62, 36, 44, 94, 69,
            32, 96, 70, 84, 58, 78, 25, 80, 58, 66, 83, 24, 98, 60, 42, 43, 43, 39, 97, 57, 81, 62, 75, 81, 23, 43, 50,
            38, 60, 58, 70, 88, 36, 90, 37, 45, 45, 39, 44, 53, 70, 24, 82, 81, 47, 97, 35, 65, 74, 68, 49, 55, 52, 94,
            95, 29, 99, 20, 22, 25, 49, 46, 98, 59, 98, 60, 23, 72, 33, 98, 80, 95, 78, 57, 67, 53, 47, 53, 36, 38, 92,
            30, 80, 32, 97, 39, 80, 72, 55, 41, 60, 67, 53, 65, 95, 20, 66, 78, 98, 47, 100, 85, 53, 53, 67, 27, 22, 61,
            43, 52, 76, 64, 61, 29, 30, 46, 79, 66, 27, 79, 98, 90, 22, 75, 57, 67, 36, 70, 99, 48, 43, 45, 71, 100, 88,
            48, 27, 39, 38, 100, 60, 42, 20, 69, 24, 23, 92, 32 
        ]
    
    def check_constraint(self, x: list):#first fit
        chosen_bin = self.compute_fitness(x)

        if ( not chosen_bin ): return False

        remaining = np.full((chosen_bin, ), self.capacity)
        
        if ( remaining[0] < self.weight[0] ): return False

        remaining[0] -= self.weight[0]

        index_weight = 1
        index_remaining = 0

        while ( index_weight < self.n_vars ):
            if ( remaining[index_remaining] - self.weight[index_weight] >= 0 ):
                remaining[index_remaining] -= self.weight[index_weight]
                index_remaining = 0
            else:
                index_remaining += 1
                if ( index_remaining == chosen_bin ):
                    return False
                index_weight -= 1
            index_weight += 1

        return True
        
    def compute_fitness(self, bin: list):
        return sum(bin)