"""
  Reachable Py
"""

from enum import Enum

class VisitStatus(Enum):
  WHITE = 0 # visited'
  RED   = 1 # visiting
  BLACK = 2 # visited

def dfs_visit(adj_list, visit_status, curr_node, answer):
  if visit_status[curr_node] is not VisitStatus.WHITE:
    return answer
  visit_status[curr_node] = VisitStatus.RED
  answer.add(curr_node)
  for next_node in adj_list[curr_node]:
    if (visit_status[next_node] is VisitStatus.WHITE):
      answer = dfs_visit(adj_list, visit_status, next_node, answer)
  visit_status[curr_node] = VisitStatus.BLACK
  return answer

def reachable(adj_list, start_node):
  """ Compute the nodes reachable from a start node

  For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
  and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

  Parameters:
  -----------
  adj_list : the adjacency list of the graph
  start_node: the index of the start node

  Returns:
  --------
  reachable: set(int) the set of nodes reachable from start_node
  """
  # Basically DFS
  if start_node >= len(adj_list) or start_node < 0:
    return {}
  answer = {start_node}
  visit_status = {}
  for i in range(0, len(adj_list)):
    visit_status[i] = VisitStatus.WHITE

  for next_node in adj_list[start_node]:
    if (visit_status[next_node] == VisitStatus.WHITE):
      answer = dfs_visit(adj_list, visit_status, next_node, answer)

  return answer

def main():
  assert reachable([[1, 3], [2], [0], [4], [3], []], 0) == {0, 1, 2, 3, 4}
  print("Passed 1")
  assert reachable([[1, 3], [2], [0], [4], [3], []], 3) == {3, 4}
  print("Passed 2")
  assert reachable([[0]], 0) == {0}
  print("Passed 3")
  assert reachable([], -1) == {}
  print("Passed 4")
  assert reachable([[1], [2], [3], [4], [5], [6], []], -1) == {}
  print("Passed 5")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 6) == {6}
  print("Passed 6")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 5) == {6, 5}
  print("Passed 7")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 4) == {6, 5, 4}
  print("Passed 8")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 3) == {6, 5, 4, 3}
  print("Passed 9")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 2) == {6, 5, 4, 3, 2}
  print("Passed A")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 1) == {6, 5, 4, 3, 2, 1}
  print("Passed B")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 0) == {6, 5, 4, 3, 2, 1, 0}
  print("Passed C")
  assert reachable([[], [2], [3], [4], [5], [6], []], 0) == {0}
  print("Passed D")
  assert reachable([[1], [], [3], [4], [5], [6], []], 0) == {0, 1}
  print("Passed E")
  assert reachable([[1], [2], [], [4], [5], [6], []], 0) == {0, 1, 2}
  print("Passed F")
  assert reachable([[1], [2], [3], [], [5], [6], []], 0) == {0, 1, 2, 3}
  print("Passed G")
  assert reachable([[1], [2], [3], [4], [], [6], []], 0) == {0, 1, 2, 3, 4}
  print("Passed H")
  assert reachable([[1], [2], [3], [4], [5], [], []], 0) == {0, 1, 2, 3, 4, 5}
  print("Passed I")
  assert reachable([[1], [2], [3], [4], [5], [6], []], 0) == {6, 5, 4, 3, 2, 1, 0}
  print("Passed J")
  assert reachable([[1], [2], [3], [4], [5], [6], [0]], 0) == {6, 5, 4, 3, 2, 1, 0}
  print("Passed K")

if __name__ == "__main__":
  main()