#User function Template for python3
import math

class Solution:
    def switchCase(self, choice, arr):
        # Code here
        if choice == 1:
                R = arr[0]
                return math.pi * R * R
        elif choice == 2:
                L = arr[0]
                B = arr[1]
                return L * B