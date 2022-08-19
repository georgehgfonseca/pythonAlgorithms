import searchSort
from binaryTree import TreeNode
from graph import Graph
from weightedGraph import WeightedGraph
import combinatorics
import strings


# Array algorithms
array = [2, 4, 6, 7, 9]
searchSort.pushInOrder(array, 1)
searchSort.pushInOrder(array, 5)
searchSort.pushInOrder(array, 10)
print(array)
print(searchSort.binarySearchRec(array, 8))

# # String algorithms
# s = "araras"
# print(strings.palindrome(s))

# # Tree algorithms
# tree = TreeNode(2)
# tree.addNode(tree, 5)
# tree.addNode(tree, 4)
# tree.addNode(tree, 1)
# tree.addNode(tree, 7)
# print(tree.traversePreorder(tree))
# print(tree.traverseOrder(tree))
# print(tree.traversePostorder(tree))

# # Graph algorithms
# graph = WeightedGraph(6)
# graph.addUndirectedEdge(0, 1, 1)
# graph.addUndirectedEdge(0, 3, 1)
# graph.addUndirectedEdge(3, 2, 1)
# graph.addUndirectedEdge(1, 4, 1)
# graph.addUndirectedEdge(2, 4, 1)
# graph.addUndirectedEdge(1, 5, 1)
# print(graph.adjList)
# print(graph.bfs(0))
# print(graph.dfs(0))
# print(graph.connected())
# print(graph.dijkstra_pq(0, 5))

# # Combiantorics algorithms
# print(combinatorics.findSubsets([1, 2, 3, 4], 2))
# print(combinatorics.allSubsets([1, 2, 3, 4]))
