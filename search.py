import random

depth_limit = 10

def back(father_list, goal, initial):
    visited = [] #advoid loop
    path = [goal]
    temp = goal
    while(temp!= initial): 
        path.append(father_list[temp])
        temp = father_list[temp]
        
    path.reverse()
    return path

def BFS(numNodes, initial, goal, adjMatrix):
    frontier = [initial] 
    visited = []
    # contain nodes and its fredecessor
    father_list = {initial: "none"}

    while(len(frontier) != 0):
        node = frontier.pop(0) #queue
        visited.append(node)
        
        for i in range(0, numNodes):
            if adjMatrix[node][i] != 0 and (i in visited) == False and (i in frontier) == False:
                father_list.update({i : node})
                if i == goal: 
                    
                    path = back(father_list, goal, initial)
                    return visited, path
                frontier.append(i)
    return visited, None

def DFS(numNodes, initial, goal, adjMatrix):
    frontier = [initial] 
    visited = [] 
    path_to_node = [] #advoid loop
    # contain nodes and its fredecessor
    father_list = {initial: "none"}

    while(len(frontier) != 0):
        node = frontier.pop() #stack
        visited.append(node)
        path_to_node = back(father_list, node, initial)

        for i in range(numNodes - 1, -1, -1):

            if adjMatrix[node][i] != 0 and (i in path_to_node) == False and (i in frontier) == False and (i != father_list[node]): #advoid loop in undirected graph

                father_list.update({i : node})
                if i == goal: 
                    path = back(father_list, goal, initial)
                    return visited, path
                frontier.append(i)
                
    return visited, None

def priority_queue_pop(frontier): #function sorts queue ascending, then pop the min value and return it
    min = 9223372036854775807
    index = -1
    for i in range(0, len(frontier)):
        #find min cost
        if frontier[i][1] < min:
            min = frontier[i][1]
            index = i
    return frontier.pop(index)

def find_node(node, f):
    for i in range(0, len(f)):
        if f[i][0] == node: 
            
            return i
    return "cant find node"

def UCS(numNodes, initial, goal, adjMatrix):
    frontier = [[initial, 0, [initial]]] #priority queue: node, cost, father_node
    visited = []
    # contain nodes and its fredecessor
    path_to_node = [] #avoid loop

    while(len(frontier) != 0):
        index, node = min_heuristic(frontier)
        node, cost, path_to_node = frontier.pop(index)

        if (node in visited) == True:
            continue

        visited.append(node)
        if node == goal:
            return visited, path_to_node

        for i in range(0, numNodes):
            if adjMatrix[node][i] != 0 and (i in visited) == False:
                path_to_node.append(i)
                frontier.append([i, cost + adjMatrix[node][i], path_to_node.copy()])
                path_to_node.pop()

    return visited, None

def min_heuristic(L): #return node has min heuristic and it's index in frontier
    value = -1
    index = -1
    min = 9223372036854775807
    for i in range(0, len(L)):
        if L[i][1] < min:
            min = L[i][1]
            value = L[i][0]
            index = i
    return index, value

def GBFS(numNodes, initial, goal, adjMatrix):
    visited = [[]]
    visited.append([])
    node = None
    f_node = None
    path_to_node = [] #avoid loop

    path = []

    heuristic = adjMatrix[numNodes]

    frontier = [[initial, heuristic[initial], [initial]]] #list of hold node and their cost
                       #[node, f(node), path_to_node[]], [node, f(node), path_to_node[]],...

    
    while (len(frontier) != 0):
        
        index, node = min_heuristic(frontier)
        node, f_node, path_to_node = frontier.pop(index)
        while (node in visited[0]) == True and visited[1][node] <= f_node:
            index, node = min_heuristic(frontier)
            node, f_node, path_to_node = frontier.pop(index)
        
        visited[0].append(node)
        visited[1].append(f_node)
        
        if (node == goal):
            return visited[0], path_to_node
        
        for i in range(0, numNodes, 1):
            
            if adjMatrix[node][i] != 0 and (i in visited[0]) == False:
                path_to_node.append(i)

                frontier.append([i, heuristic[i], path_to_node.copy()]) #f(node) = path(initial -> father_node) + h(node)

                path_to_node.pop()

    return visited[0], None

def AStar(numNodes, initial, goal, adjMatrix): #Graph-search A* -> No repeat!!!
    visited = [[]]
    visited.append([])
    node = None
    f_node = None
    path_to_node = [] #avoid loop

    cost = [] #cost from initial -> considered node
    path = []

    for i in range (0, numNodes):
        cost.append(0)
    heuristic = adjMatrix[numNodes]

    frontier = [[initial, heuristic[initial], [initial]]] #list of hold node and their cost
                       #[node, f(node), path_to_node[]], [node, f(node), path_to_node[]],...

    
    while (len(frontier) != 0):
        
        index, node = min_heuristic(frontier)
        node, f_node, path_to_node = frontier.pop(index)
        while (node in visited[0]) == True and visited[1][node] <= f_node:
            index, node = min_heuristic(frontier)
            node, f_node, path_to_node = frontier.pop(index)
        
        visited[0].append(node)
        visited[1].append(f_node)
        
        if (node == goal):
            return visited[0], path_to_node
        
        for i in range(0, numNodes, 1):
            
            if adjMatrix[node][i] != 0 and (i in visited[0]) == False:
                path_to_node.append(i)

                cost[i] = cost[node] + adjMatrix[node][i] #update path to that node
                frontier.append([i, cost[i] + heuristic[i], path_to_node.copy()]) #f(node) = path(initial -> father_node) + h(node)

                path_to_node.pop()

    return visited[0], None
    

def recursive_DLS(numNodes, node, goal, adjMatrix, depth, visited, current_path, on_current_path): 
    
    visited.append(node)
    current_path.append(node)
    on_current_path[node] = True

    if node == goal:
        return visited, current_path
    elif depth == 0:
        return visited, None

    cutOff_occured = False
    children_list = []

    for i in range(0, numNodes):
        if adjMatrix[node][i] != 0:
            children_list.append(i)

    for i in children_list:
        if on_current_path[i] == False:
            visited_list, path = recursive_DLS(numNodes, i, goal, adjMatrix, depth - 1, visited, current_path, on_current_path)
            if path is None:
                on_current_path[current_path.pop()] = False

            elif len(visited) != 0 and path is None:
                cuttOff_occured = True
            
            else:
                return visited_list, path

        if cutOff_occured:
            on_current_path[i] = False
            return visited, None
        
    else: 
        on_current_path[i] = False
        return visited, None


def DLS(numNodes, initial, goal, adjMatrix, depth = depth_limit):
    visited = []
    current_path = []
    on_current_path = []
    for i in range(0, numNodes):
        on_current_path.append(False)
    return recursive_DLS(numNodes, initial, goal, adjMatrix, depth, visited, current_path, on_current_path)

def IDS(numNodes, initial, goal, adjMatrix):
    depth = 0
    visited = []

    while True:
        r_visited, path = DLS(numNodes, initial, goal, adjMatrix, depth)
    
        if len(r_visited) == 0: 
            return visited, None

        visited.append(r_visited)
        depth += 1

        if path is not None or depth > depth_limit:
            return visited, path

def HC(numNodes, initial, goal, adjMatrix): #first-choice hill climbing
    heuristic = adjMatrix[numNodes]
    current_state = 9223372036854775807
    step = 0
    limit = 50
    visited = []
    path = []

    node = initial #considered node
    visited.append(node)
    path.append(node)
    r_node = initial #random node
    while (step < limit):
        if (node == goal):
            return visited, path
        while (adjMatrix[node][r_node] == 0 or heuristic[r_node] >= current_state) and step < limit:
            r_node = random.randint(0, numNodes - 1)
            step += 1
        step = 0 #advoid infinity loop
        current_state = heuristic[r_node]
        visited.append(r_node)
        path.append(r_node)
        node = r_node
    
    return visited, None