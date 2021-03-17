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
        theta = random.uniform(0, 1) * 2 * math.pi
        r = math.sqrt(random.uniform(0, 1)) * self.radius
        x = self.x_center + (r * math.cos(theta))
        y = self.y_center + (r * math.sin(theta))
        return [x, y]
