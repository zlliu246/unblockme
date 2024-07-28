import heapq
from .state_utils import get_next_states

def dijkstra_search(state):
    d = {state: dict(prev=None, cost=0)}
    pq = [(0,state)]
    while pq:
        priority, current = heapq.heappop(pq)

        # checkwin
        if current[2][-2:] == 'XX':
            out = []
            while current:
                out.append(current)
                current = d[current]['prev']
            out = out[::-1]
            return out

        neighbours = get_next_states(current)
        for n in neighbours:
            n_cost = d[current]['cost'] + 1
            if n not in d:
                d[n] = dict(prev=current, cost=n_cost)
                pq.append((n_cost, n))
            else:
                c_cost = d[current]['cost']
                if n_cost < c_cost:
                    d[n] = dict(prev=current, cost=n_cost)
                    pq.append((n_cost, n))

    raise Exception('no solution')   