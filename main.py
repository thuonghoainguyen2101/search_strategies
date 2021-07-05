import search

def inputFile(filePath):
    file = open(filePath, "r")
    fileContent = file.read().split('\n')
    file.close()

    numNodes = int(fileContent[0])

    line = fileContent[1].split(' ')
    initial = int(line[0])
    goal = int(line[1])
    searchType = int(line[2])

    # input matrix
    matrix=[]
    for line1 in fileContent[2:]:
        matrix.append(line1.split(' '))

    for i in range(0, numNodes + 1):
        for j in range(0, numNodes):
            matrix[i][j] = int(matrix[i][j])

    return numNodes, initial, goal, searchType, matrix

def search_type(numNodes, initial, goal, searchType, adjMatrix):
    visited = []
    path = []
    if searchType == 0:
        visited, path = search.BFS(numNodes, initial, goal, adjMatrix)
    elif searchType == 1:
        visited, path = search.DFS(numNodes, initial, goal, adjMatrix)
    elif searchType == 2:
        visited, path = search.UCS(numNodes, initial, goal, adjMatrix)
    elif searchType == 3:
        visited, path = search.IDS(numNodes, initial, goal, adjMatrix)
    elif searchType == 4:
        visited, path = search.GBFS(numNodes, initial, goal, adjMatrix)
    elif searchType == 5:
        visited, path = search.AStar(numNodes, initial, goal, adjMatrix)
    elif searchType == 6:
        visited, path = search.HC(numNodes, initial, goal, adjMatrix)
    else: 
        print("invalid search type")

    return visited, path
    
def outputFile(visited, path, filePath):
    file = open(filePath, "a")
    if visited == None:
        file.write("No visited.\n")
    else:
        for i in visited:
            file.write(str(i) + ' ')
    file.write('\n')

    if path == None:
        file.write("No path.\n")
    else:
        for i in path:
            file.write(str(i) + ' ')
    file.write('\n' +'\n')
    file.close()

if __name__ == "__main__":
    in_file = "test/input2.txt"
    out_file = "test/output2.txt"
    numNodes, initial, goal, searchType, adjMatrix = inputFile(in_file)
    for i in range (0, 7):
        visited, path = search_type(numNodes, initial, goal, i, adjMatrix)
        outputFile(visited, path, out_file)
    # visited, path = search_type(numNodes, initial, goal, searchType, adjMatrix)
    # outputFile(visited, path, out_file)