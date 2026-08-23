class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        
        for value in gain:
            altitude += value
            highest = max(altitude,highest)

        return highest