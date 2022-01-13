# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:48:41 2022

@author: Sehan
"""

class Item:
    
    pay_rate=0.8 #The pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, value: float, quantity=0):
        
        #run validations to the received arguments
        assert quantity>=0, f"Quantity {quantity} is not greater than or euqal to 0"
        assert value >0, f"Value {value} is not greater than 0"
        
        
        # assign to self object
        self.name = name
        self.value=value
        self.quantity=quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.value * self.quantity
    
    def apply_discount(self):
        self.value = self.value * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}', {self.quantity}, {self.value})"



item1=Item('phone', 30, 500)
item2=Item('laptop', 100, 500)
item3=Item('tablet', 50, 500)
item4=Item('headphone', 10, 500)
item5=Item('speaker', 20, 500)

print(Item.all)



