# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:06:18 2018

@author: narendra
"""

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg

my_car = Car("DeLorean", "silver", 88)

print(my_car.model)
print(my_car.color)
print(my_car.mpg)