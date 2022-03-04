#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:53:23 2022

@author: dfost
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#set chart table and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=24)

#set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()


