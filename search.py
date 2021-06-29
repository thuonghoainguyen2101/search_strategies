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
    return visited, "No path"

def DFS(numNodes, initial, goal, adjMatrix):
    frontier = [initial] 
    visited = [] 
    path_to_node = [] #advoid loop
    # contain nodes and its fredecessor
    father_list = {initial: "none"}

    while(len(frontier) != 0):
        node = frontier.pop() #stack
        visited.append(node)
        path_to_node = (father_list, node, initial)

        for i in range(numNodes - 1, -1, -1):

            if adjMatrix[node][i] != 0 and (i in path_to_node) == False and (i in frontier) == False and (i != father_list[node]): #advoid loop in undirected graph

                father_list.update({i : node})
                if i == goal: 
                    path = back(father_list, goal, initial)
                    return visited, path
                frontier.append(i)
                
    return visited, "No path."

def priority_queue_pop(priority_queue): #[node, cost], [node, cost],[node, cost],...
    min = 9223372036854775807
    index = -1
    for i in range(0, len(priority_queue)):
        #find min cost
        if priority_queue[i][1] < min:
            min = priority_queue[i][1]
            index = i
    return priority_queue.pop(index)

def UCS(numNodes, initial, goal, adjMatrix):
    frontier = [[initial, 0]]
    visited = []
    # contain nodes and its fredecessor
    father_list = {initial: "none"}
    previous_node = initial #used to update father node of goal

    while(len(frontier) != 0):
        node, cost = priority_queue_pop(frontier) #priority queue
        print("goal: ", node, cost)
        if node == goal: 
            #father_list.update({node : previous_node})
            path = back(father_list, goal, initial)
            return visited, path

        visited.append(node)
        for i in range(0, numNodes):
            if adjMatrix[node][i] != 0 and (i in visited) == False:
               
                if  ([i, cost + adjMatrix[node][i]] in frontier) == False:
                    frontier.append([i, cost + adjMatrix[node][i]])
                    father_list.update({i : node})
                    print("a")

                else:
                    index = frontier.index([i, cost + adjMatrix[node][i]])
                    #previous_node = i #use to update father node of goal
                    frontier[index][1] = min (frontier[index][1], cost + adjMatrix[node][i])
                    #father_list.update({i : node})
                    print(father_list)
                    print("b")
                
                previous_node = node

    return visited, "No path."

def min_heuristic(L):
    index = -1
    min = 9223372036854775807
    for i in range(0, len(L)):
        if L[i][1] < min:
            min = L[i][1]
            index = L[i][0]
    return index

def GBFS(numNodes, initial, goal, adjMatrix):
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
        next_node = min_heuristic(children_list) #next considered node
        father_list.update({next_node : node})
        node = next_node
        children_list.clear()

    path = back(father_list, goal, initial)
    return visited, path

def Astar(numNodes, initial, goal, adjMatrix):
    visited = []

    path = [] #path from initial -> considered node
    for i in range (0, numNodes):
        path.append(0)
    heuristic = adjMatrix[numNodes]

    children_list = [] #list of successor of considered node and their cost
                       #[node, f(node)], [node, f(node)],...

    # contain nodes and its fredecessor
    father_list = {initial: "none"}
    node = initial #node being considered
    while (node != goal):
        visited.append(node)
        
        #create sucessor list
        for i in range(0, numNodes):
            if adjMatrix[node][i] != 0:
                path[i] += adjMatrix[node][i] #update path to that node
                children_list.append([i, path[i] + heuristic[i]]) #f(node) = path(initial -> father_node) + h(node)

        next_node = min_heuristic(children_list) #next considered node
        father_list.update({next_node : node})
        node = next_node
        children_list.clear()
                
    path = back(father_list, goal, initial)
    return visited, path