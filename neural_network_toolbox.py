# -*- coding: utf-8 -*-
import numpy as np
import os

def Neural_Netowrks():
    def __init__(self):
        pass

    def activation_functions(self):
        """Contains diffrent activation functions
        for example: simgoid(self,x) or relu(self,x)"""
        def simgoid(self, x):
            """The sigmoid activation function; takes x as input"""
            return 1/(1+np.exp(-x))

        def relu(self,x):
            """The relu activation function; takes x as input"""
            return np.maximum(0,x)

    def derivatives(self):
        """Contains the derivatives of diffrent activation activation_functions
        for exmaple sigmoid_deriviative(self,x) or relu_deriviative(self,x)"""
        def simgoid_deriviative(self,x):
            """The simgoid derivative"""
            return x*(1-x)

        def relu_deriviative(self,x):
            """The relu derivative"""
            return 1

    def error_calculation(self):
        """Contains diffrent error calcultion functions like mean_squarred_error(self,x,y)
        or normal_error(self,x,y)"""
        def mean_squarred_error(self,x,y):
            return 0.5*(y-x)**2

        def normal_error(self,x,y):
            return y-x
