class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) if (arrivalTime + delayedTime) < 24 else (arrivalTime + delayedTime) % 24