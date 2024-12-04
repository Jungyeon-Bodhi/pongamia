#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:03:27 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

import pandas as pd
import numpy as np


class Indicator:
    
    def __init__(self, df, name, number, var, i_cal, i_type, description, period, target):
        """
        - Initialise the Indicator class
        name: str, Name of the indicator
        number: int, Number corresponding to the indicator
        var: list, Variables of the indicator (Questions)
        i_cal: str, How to calculate the indicator
        i_type: str, Type of the indicator ('Count' or 'Percentage')
        description: str, Description of the indicator
        period: str, Period during which the indicator is measured (e.g., 'baseline,' 'midline,' or 'endline')
        targets: int, Target number for the indicator
        score_map: dic, Way to calculate the score for this indicator
        """
        self.df = df
        self.name = name
        self.number = number
        self.var = var
        self.var_type = 'single'
        if len(self.var) == 1:
            self.var_type = 'single'
        else: 
            self.var_type = 'multi'
        self.indicator_name = f'{name}'
        self.i_cal = i_cal
        self.i_type = i_type.capitalize()
        self.description = description
        self.period = period
        self.target = target
        self.baseline = None
        self.midline = None
        self.var_order = None
        self.var_change = None
        self.score_map = None
        self.valid_point = None
        self.breakdown = None
        self.condition = None
        self.kap_label = None

    def info(self):
        """
        - Display the details of the indicator
        """
        print(f"Indicator: {self.name}.{self.number} | Indicator type: {self.i_type} ({self.i_cal})\nDescription: {self.description} \nPeriod: {self.period} | Target: {self.target}")
        if self.baseline != None:
            print(f"This indicator's baseline value was {self.baseline}")
        if self.midline != None:
            print(f"This indicator's midline value was {self.midline}")

    def get_target(self):
        """
        - Get the target value
        """
        print(f"The target value for {self.period} is {self.target}")
        return self.target
    
    def update_target(self, value):
        """
        - Update the target value
        value: int, New target value
        """
        self.target = value
        print("Target value has been updated")

    def add_baseline(self, value):
        """
        - Add the baseline value
        value: int, Baseline value
        """
        self.baseline = value

    def add_midline(self, value):
        """
        - Add the midline value
        value: int, Midline value
        """
        self.midline = value

    def add_var_order(self, order):
        """
        - Define the sequence of responses from the variable
        order: list, Sequence of responses from the variable
        """
        self.var_order = order

    def add_score_map(self, score_map):
        """
        - Define how to calculate the indicator
        score_map: dic, Way to calculate the score for this indicator {'A':3, 'B':-1, etc}
        """
        self.score_map = score_map

    def add_valid_point(self, point):
        """
        - Set the valid point for the indicator (treat from this point as the numerator)
        point: int, valid point for the indicator
        """
        self.valid_point = point

    def add_breakdown(self, breakdown):
        """
        - Add the condition for the breakdown of the data
        breakdown: dic, Combination of breakdown columns and its name: {'col1':'gender'}
        """
        self.breakdown = breakdown
        print(f"{self.indicator_name} will be broken down by {', '.join(self.breakdown.values())}")

    def add_condition(self, conditions):
        """
        - Add the condition for the indicator
        conditions: series, Filtering criteria for the indicator: (df['2'] > 25) & (df['4'] == 'Male')
        """
        self.condition = conditions
        
    def add_var_change(self, new_var):
        """
        - Add the condition for index change
        - Specify the values from the dictionary instead of the Pass and Not Pass (Keys)
        new_var: dic, New index: {"Pass": "New name1", "Not Pass": "New name2"} 
        """
        self.var_change = new_var # Should be {"Pass": "New name1", "Not Pass": "New name2"}
        
    def add_label(self, labels):
        """
        - Add the condition for column label change
        labels: list, New column labels for the multiple response questions in the survey
        """
        self.kap_label = labels