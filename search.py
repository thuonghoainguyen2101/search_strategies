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
    for i in range(1, len(frontier)):
        key = frontier[i]
        j = i-1
        while j >=0 and key[1] < frontier[j][1] :
                frontier[j + 1][1] = frontier[j][1]
                j -= 1
        frontier[j + 1] = key
    
    return frontier.pop(0)    

def find_node(find_value, f):
    for i in range(0, len(f)):
        if f[i][0] == find_value: return i
    return "cant find value"

def UCS(numNodes, initial, goal, adjMatrix):
    frontier = [[initial, 0, "none"]] #priority queue: node, cost, father_node
    visited = []
    # contain nodes and its fredecessor
    father_list = {initial: "none"}
    previous_node = initial #used to update father node of goal

    while(len(frontier) != 0):
        node, cost, father_node = priority_queue_pop(frontier) #chooses the lowest-cost node in frontier
        if node == goal: 
            father_list.update({node : father_node})
            path = back(father_list, goal, initial)
            return visited, path

        visited.append(node)
        for i in range(0, numNodes):
            if adjMatrix[node][i] != 0 and (i in visited) == False:
                index = find_node(i, frontier)
                if index == "cant find value":
                    frontier.append([i, cost + adjMatrix[node][i], node])
                    father_list.update({i : node})

                else:
                    if frontier[index][1] > (cost + adjMatrix[node][i]):
                        frontier[index][1] = cost + adjMatrix[node][i] #replace that frontier node with child
                        frontier[index][2] = node

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
    trash_value = 0 # unused value
    visited = []
    children_list = [] #list of successor of considered node and their heuristic
                       #[node, h(node)], [node, h(node)],...

    # contain nodes and its fredecessor
    father_list = {initial: "none"}
    temp = 0
    
    heuristic = adjMatrix[numNodes]
    node = initial #node being considered
    while(node != goal):
        visited.append(node)
    #     #create sucessor list
        for i in range(0, numNodes):
            if adjMatrix[node][i] != 0:
                children_list.append([i, heuristic[i]]) #f(n) = h(n)
        
        # find the sucessor has min heuristic
        trash_value, next_node = min_heuristic(children_list) #next considered node
        father_list.update({next_node : node})
        node = next_node
        children_list.clear()

    path = back(father_list, goal, initial)
    return visited, path

def Astar(numNodes, initial, goal, adjMatrix): #Graph-search A* -> No repeat!!!
    visited = []
    path_to_node = [] #avoid loop

    path = [] #path from initial -> considered node
    for i in range (0, numNodes):
        path.append(0)
    heuristic = adjMatrix[numNodes]
    print(heuristic)

    frontier = [] #list of hold node and their cost
                       #[node, f(node), father_node], [node, f(node), father_node],...

    # contain nodes and its fredecessor
    father_list = {initial: "none"}
    node = initial #node being considered
    while (node != goal):
        visited.append(node)
        
        #delete node from frontier
        index = find_node(node, frontier)
        while index != "cant find value":
            frontier.pop(index)
            index = find_node(node, frontier)
        #path_to_node = back(father_list, node, initial)
        
        #create sucessor list
        for i in range(numNodes-1, -1, -1):
            if adjMatrix[node][i] != 0 and (i in path_to_node) == False:
                path[i] = path[node] + adjMatrix[node][i] #update path to that node
                frontier.append([i, path[i] + heuristic[i], node]) #f(node) = path(initial -> father_node) + h(node)

                #print(node, children_list)
        min_heuristic = priority_queue_pop(frontier) #next considered node
        next_node = min_heuristic[0]
        print(index, next_node)
        print(path)
        print(frontier)
        print(path[next_node])
        print(min_heuristic[1] - heuristic[node])
        if path[next_node] == 0 or path[next_node] > (min_heuristic[1] - heuristic[node]):
            father_list.update({next_node : min_heuristic[2]})
        #father_list.update({next_node : frontier[index][2]})
        node = next_node
        print(father_list)

    path = back(father_list, goal, initial)
    return visited, path

def recursive_DLS(numNodes, node, goal, adjMatrix, depth, visited, current_path, on_current_path): #visited, path, CutOff
    print(node)
    
    visited.append(node)
    current_path.append(node)
    on_current_path[node] = True

    print(on_current_path)
    if node == goal:
        return visited, current_path
    elif depth == 0:
        return visited, None

    cutOff_occured = False
    children_list = []
    # children_list = adjMatrix[node]
    # for i in children_list:
    for i in range(0, numNodes):
        if adjMatrix[node][i] != 0:
            children_list.append(i)

    for i in children_list:
        if on_current_path[i] == False:
            visited_list, path = recursive_DLS(numNodes, i, goal, adjMatrix, depth - 1, visited, current_path, on_current_path)
            print(visited_list)
            if len(visited) == 0 and path is None:
                on_current_path[current_path.pop()] = False

            elif len(visited) != 0 and path is None:
                cuttOff_occured = True
            
            else:
                return visited_list, path

        if cutOff_occured:
            return visited, None
        
    else: return visited, None


def DLS(numNodes, initial, goal, adjMatrix, depth = 10):
    visited = []
    current_path = []
    on_current_path = []
    for i in range(0, numNodes):
        on_current_path.append(False)
    print(on_current_path)
    return recursive_DLS(numNodes, initial, goal, adjMatrix, depth, visited, current_path, on_current_path)

def IDS(numNodes, initial, goal, adjMatrix):
    depth = 0
    visited = []

    while True:
        r_visited, path = DLS(numNodes, initial, goal, adjMatrix, depth)
    
        if len(r_visited) == 0: return visited, None

        visited.append(r_visited)
        depth += 1

        if path is not None:
            return visited, path
