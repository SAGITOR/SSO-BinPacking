import math
import random
from Problem import Problem

class Salp( Problem ):

    def __init__( self ):
        super().__init__()
        self.x = [ random.randint(0, 1) for x in range(self.n_vars) ]
    
    def leader_move( self, food, c1 ):
        for index in range( 0, self.n_vars ):
            c2 = random.uniform(0, 1)
            c3 = random.uniform(0, 1) - 0.5
            self.x[index] = self.__to_binary( food.x[index] + c1*((1 - 0)*c2 + 0) if c3 >= 0 else food.x[index] - c1*((1 - 0)*c2 + 0) )

    def follower_move( self , previus_follower ):
        for index in range( 0, self.n_vars ):
            self.x[index] = self.__to_binary( 0.5*( self.x[index] + previus_follower.x[index] ) )
            #self.x[index] = self.__to_binary( random.random() * ( self.x[index] + previus_follower.x[index] ) + random.random() )
    
    def is_feasible( self ):
        return self.check_constraint(self.x)
    
    def compute_values_fitness( self ):
        return self.compute_fitness(self.x)
    
    def is_better_than( self, g ):
        return self.compute_values_fitness() < g.compute_values_fitness()
    
    def copy( self, object ):
        #if ...
        self.x = object.x.copy()
    
    def __to_binary( self, x: float ):
        return 1 if random.uniform(0.5, 0.731059) <= (1 / (1 + math.pow(math.e, -x))) else 0
