class Solution:
    def __init__(self):
        self.min_cost = None
        self.dist_limit = 0

    def dfs(self, source, flight_dict, dist, cur_cost, cur_dist):
        if (self.min_cost is not None and cur_cost > self.min_cost
                or cur_dist > self.dist_limit):
            return
        if source == dist:
            self.min_cost = cur_cost
            return
        if source not in flight_dict:
            return
        for n_flight in flight_dict[source]:
            self.dfs(n_flight[1], flight_dict, dist, cur_cost + n_flight[2],
                     cur_dist + 1)

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        flight_dict = {}
        avail_dist = set()
        for flight in flights:
            avail_dist.add(flight[1])
            if flight[0] not in flight_dict:
                flight_dict[flight[0]] = [flight]
            else:
                flight_dict[flight[0]].append(flight)
        if dst not in avail_dist:
            return -1

        self.dist_limit = k + 1
        self.dfs(src, flight_dict, dst, 0, 0)
        return self.min_cost if self.min_cost is not None else -1
