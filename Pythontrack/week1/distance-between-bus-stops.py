class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        minimum = min(start, destination)
        maximum = max(start, destination)
        return min(sum(distance[minimum: maximum]), sum(distance[:minimum] + distance[maximum:]))