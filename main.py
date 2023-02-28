# solution is programmed using Dijkstra's algorithm

import heapq

Romania = {
    "Oradea": {("Zerind", 71), ("Sibiu", 151)},
    "Zerind": {("Oradea", 71), ("Arad", 75)},
    "Arad": {("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)},
    "Sibiu": {("Fagaras", 99), ("Rimicu_Vilcea", 80), ("Arad", 140), ("Oradea", 151)},
    "Fagaras": {("Sibiu", 99), ("Bucharest", 211)},
    "Timisoara": {("Arad", 118), ("Lugoj", 111)},
    "Rimicu_Vilcea": {("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)},
    "Lugoj": {("Timisoara", 111), ("Mehadia", 70)},
    "Pitesti": {("Rimicu_Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)},
    "Mehadia": {("Lugoj", 70), ("Dobreta", 75)},
    "Dobreta": {("Mehadia", 75), ("Craiova", 120)},
    "Craiova": {("Rimicu_Vilcea", 146), ("Pitesti", 138), ("Dobreta", 120)},
    "Bucharest": {("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)},
    "Giurgiu": {("Bucharest", 90)},
    "Urziceni": {("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)},
    "Hirsova": {("Urziceni", 98), ("Eforie", 86)},
    "Eforie": {("Hirsova", 86)},
    "Vaslui": {("Urziceni", 142), ("Iasi", 92)},
    "Iasi": {("Vaslui", 92), ("Neamnt", 87)},
    "Neamnt": {("Iasi", 87)},
}

start = input("Enter starting city: ")
end = input("Enter destination: ")
visited = [] # all visited locations
path = {} # keeps track of most efficient path
pri = [] # list of unvisited locations
heapq.heappush(pri, (0, start)) # priority queue of unvisited locations

def printPath():
    route = ""
    current = end
    distance = path[end][1]
    while current != start:
        route = " > " + current + route
        current = path[current][0]
    route = start + route
    print("The shortest route from " + start + " to " + end + " is " + str(distance) + " kms:")
    print(route)

def visit(curr): # curr is a pair of (dist from start, curr) from queue
    if curr[1] == end: # if the current city is the destination, print the path from start to finish
        printPath()
    connections = Romania[curr[1]] # connections is a set of pairs (city, distance) of all connected cities to current city
    for con in connections:
        if con[0] not in visited: # if connected city is an unvisited city  and not in path, add it to path and priority queue
            if path.get(con[0], "none") == "none":
                heapq.heappush(pri, (curr[0] + con[1], con[0]))
                path[con[0]] = (curr[1], curr[0]+con[1])
            else: # if connected city is already in path update path if the current distance is less than saved distance
                index = pri.index((path[con[0]][1], con[0]))
                if pri[index][0] > curr[0] + con[1]:
                    pri[index] = (curr[0]+con[1], con[0])
                    path[con[0]] = (curr[1], curr[0]+con[1])
                    heapq.heapify(pri)
    visited.append(curr[1]) # add current city to visited list
    if len(pri) != 0: # if there are cities left to visit, recursively visit them
        curr = heapq.heappop(pri)
        visit(curr)

# pop the top element in priority queue
curr = heapq.heappop(pri)
visit(curr)