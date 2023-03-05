"""
  GraphRepConvert Py
"""

def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph
    """
    # Convert
    adj_list = []
    v = 0
    for es in adj_mat:
      c = 0
      adj = []
      for e in es:
        if e == 1:
          adj.append(c)
        c += 1
      assert c == len(adj_mat) # sanity check matrix
      adj_list.append(adj)
      v += 1

    return adj_list

def main():
  assert mat_to_list([
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]]
    ) == [[1, 3], [2], [0], [4], [3], []]
  print("Passed 1")
  assert mat_to_list([
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1]
    ]) == [
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5]
    ]
  print("Passed 2")
  assert mat_to_list([
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 0]
    ]) == [
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4, 5],
      [0, 1, 2, 3, 4]
    ]
  print("Passed 3")
  assert mat_to_list([
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]
    ]) == [[], [], [], [], [], []]
  print("Passed 4")
  assert mat_to_list([
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 1]
    ]) == [[0], [1], [2], [3], [4], [5]]
  print("Passed 5")
  assert mat_to_list([
      [0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0]
    ]) == [[5], [4], [3], [2], [1], [0]]
  print("Passed 6")
  assert mat_to_list([
      [1, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 1, 0],
      [0, 0, 1, 1, 0, 0],
      [0, 0, 1, 1, 0, 0],
      [0, 1, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 1]
    ]) == [[0, 5], [1, 4], [2, 3], [2, 3], [1, 4], [0, 5]]
  print("Passed 7")
  assert mat_to_list([
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0]
    ]) == [[0], [0], [0], [0], [0], [0]]
  print("Passed 8")
  assert mat_to_list([
      [0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0]
    ]) == [[2], [2], [2], [2], [2], [2]]
  print("Passed 9")
  assert mat_to_list([]) == []
  print("Passed A")
  assert mat_to_list([[0]]) == [[]]
  print("Passed B")
  assert mat_to_list([[1]]) == [[0]]
  print("Passed C")
  try:
    assert mat_to_list([[1, 1]]) == [[0]]
    print("Failed D")
  except AssertionError:
    print("Passed D")

if __name__ == "__main__":
  main()