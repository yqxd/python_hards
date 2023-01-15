class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        @cache
        def max_route(node_idx, drop):
            result = 0
            for leaf_idx in A[node_idx]:
                if leaf_idx != drop:
                    result = max(result, max_route(leaf_idx, node_idx))
            return result + price[node_idx]

        A = [[] for _ in range(n)]
        is_leaf = [1 for _ in range(n)]
        for begin, end in edges:
            A[begin].append(end)
            A[end].append(begin)
            is_leaf[begin] += 1
            is_leaf[end] += 1
        result = 0
        for node_idx in range(n):
            if is_leaf[node_idx] == 2:
                result = max(result, max_route(A[node_idx][0], node_idx))
        return result