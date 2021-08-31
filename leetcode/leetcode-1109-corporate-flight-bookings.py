from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n
        for booking in bookings:
            flights[booking[0] - 1] += booking[2]
            if booking[1] < n:
                flights[booking[1]] -= booking[2]
        for i in range(1, n):
            flights[i] += flights[i - 1]
        return flights
