class BasicCalculator():
    def __init__(self, first_num, second_num):
        self.num_1 = first_num
        self.num_2 = second_num
        
        
    def add(self):
        return (self.num_1 + self.num_2)
    
    def sub(self):
        return self.num_1 - self.num_2
    
    def multiple(self):
        return self.num_1*self.num_2
    
    
    def division(self):
        return self.num_1 / self.num_2
