from basic_calculator import BasicCalculator


import math

class ScientificCalculator(BasicCalculator):
    def __init__(self, first_num, second_num):
        self.num_1 = first_num
        self.num_2 = second_num
    
    
    def logarithm(self):
        m = math.log(self.num_1, self.num_2)
        return m 
    
    def power(self):
        return math.pow(self.num_1, self.num_2)
