"""
LeetCode :: March 2021 Challenge :: Generate Random Point in a Circle
jramaswami
"""
from typing import *
import math
import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
        r = math.sqrt(random.random() * self.radius)
        theta = random.random() * 2 * math.pi
        x = x_center + r * math.cos(theta)
        y = y_center + r * math.sin(theta)
        return [x, y]
