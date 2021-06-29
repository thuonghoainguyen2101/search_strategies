import handleFile
import search
numNodes, initial, goal, searchType, adjMatrix = handleFile.inputFile("input.txt")
print("BFS: ")
visited, path = search.BFS(numNodes, initial, goal, adjMatrix)
print(visited)
print(path)

print("DFS: ")
visited, path = search.DFS(numNodes, initial, goal, adjMatrix)
print(visited)
print(path)

print("UCS: ")
visited, path = search.UCS(numNodes, initial, goal, adjMatrix)
print(visited)
print(path)

print("GBFS: ")
visited, path = search.GBFS(numNodes, initial, goal, adjMatrix)
print(visited)
print(path)

print("A Star: ")
visited, path = search.Astar(numNodes, initial, goal, adjMatrix)
print(visited)
print(path)