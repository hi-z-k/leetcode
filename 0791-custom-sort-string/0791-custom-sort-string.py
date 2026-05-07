class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordermap = defaultdict(int)
        string = set(list(s))
        for i,l in enumerate(list(order)):
            ordermap[l] = i+1
        new_order = list(s)
        new_order.sort(key=lambda x: ordermap[x])
        return "".join(new_order)
