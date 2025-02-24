class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjacent_map = defaultdict(list)
        distance_from_bob = {}
        for edge in edges:
            adjacent_map[edge[0]].append(edge[1])
            adjacent_map[edge[1]].append(edge[0])
        
        print(adjacent_map)
        def find_paths(source_node: int, root_node: int, time: int, bob: int, amount: List[int]):
            max_profit, max_child_profit = 0, -2**31

            distance_from_bob[source_node] = 0 if source_node == bob else len(amount)
            
            for adjacent_node in adjacent_map[source_node]:
                if adjacent_node != root_node:
                    max_child_profit = max(max_child_profit, find_paths(adjacent_node, source_node, time + 1, bob, amount))
                    distance_from_bob[source_node] = min(distance_from_bob[source_node], distance_from_bob[adjacent_node] + 1)

            if distance_from_bob[source_node] > time:
                max_profit+= amount[source_node]
            elif distance_from_bob[source_node] == time:
                max_profit+= (amount[source_node] / 2)
            
            return max_profit if max_child_profit == -2**31 else max_profit + max_child_profit

        return int(find_paths(0,0,0,bob,amount))


        