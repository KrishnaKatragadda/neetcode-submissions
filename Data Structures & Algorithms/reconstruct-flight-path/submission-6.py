# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = {src: [] for src, dst in tickets}
#         tickets.sort()
#         for src, dst in tickets:
#             adj[src].append(dst)

#         res = ["JFK"]
#         def dfs(src):
#             if len(res) == len(tickets) + 1:
#                 return True
#             if src not in adj:
#                 return False

#             temp = list(adj[src])
#             for i, v in enumerate(temp):
#                 adj[src].pop(i)
#                 res.append(v)
#                 if dfs(v): return True
#                 adj[src].insert(i, v)
#                 res.pop()
#             return False

#         dfs("JFK")
#         return res
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # reverse sorting lets pop() take the smallest destination.
        tickets.sort(reverse=True)

        for src, dst in tickets:
            graph[src].append(dst)

        route = []

        def dfs(node):
            # use every outgoing ticket from this airport.
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)

            # added while recursion returns, so route is backward.
            route.append(node)

        dfs("JFK")

        return route[::-1]