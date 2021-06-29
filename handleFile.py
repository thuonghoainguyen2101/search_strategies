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
