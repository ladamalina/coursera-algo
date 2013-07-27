# Kosaraju's Two-Pass Algorithm
# Input is a directed graph, G
# Computes strongly connected components in O(m + n) time,
# where n and m  are the number of nodes and edges, respectively
import sys, resource, time

# Increase recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

# Establish source of directed graph, G
# Source file has one directed edge per line, e.g. "1 5" is one line
source = "source.txt"
# Number of nodes
n = 875714 

def Kosaraju(G,G_rev):
    global leader, finish
    # Set leader for strongly connected group
    leader = {}
    # Set finishing time for each element
    finish = {}
    # Run first DFS Loop
    DFS_Loop(G_rev)
    # Reorder graph with nodes numbered according to finish time
    G_reordered = {}
    g_values = G.values()
    for i in range(1,n+1):
        temp = g_values[i-1]
        G_reordered[finish[i]] = [finish[x] for x in temp]
    # Run second DFS Loop with reordered graph
    DFS_Loop(G_reordered)
    return leader

def DFS_Loop(G):
    global t,s, explored
    t = 0 # Number of nodes processed so far (only useful for pass 1)
    s = 0 # Current source vertex (only useful for pass 2)
    # Initialize all nodes as unexplored
    explored = {}
    for i in range(1,n+1):
        explored[i] = 0 
    # Explore each adjacent node i (if unexplored)
    for i in range(n,0,-1):
        if explored[i] == 0:
            s = i
            DFS(G,i)
    return

def DFS(G,i):
    # Run Depth First Search
    global t
    explored[i] = 1 # Mark node i as explored
    leader[i] = s # Sets leader as node s (useful for second pass only)
    # For each arc (i,j) in G, if j is not yet explored, recurse on j
    for j in G[i]:
        if explored[j] == 0:
            DFS(G,j)
    t = t + 1
    finish[i] = t
    return
   
def get_graph():
    # Grabs graph from input file
    # Create dictionary with a key for each node
    G, G_rev = {}, {}
    for i in range(1,n+1):
        G[i], G_rev[i]  = [], []
    # Populate dictionary with information from file
    file = open(source)
    for line in file:
        list = line.split()
        i = int(list[0])
        j = int(list[1])
        G[i].append(j)
        G_rev[j].append(i)
    file.close()
    return G, G_rev

def most_common(lst,x):
    # This functions returns the 'x' most common elements from 'lst' 
    from collections import Counter
    c = Counter(lst)
    result = []
    for number,count in c.most_common(x):
        result.append(count)
    return result

if __name__=="__main__":
    start = time.time()
    G, G_rev = get_graph()
    print "Graph grabbed in", time.time() - start,"seconds"

    start = time.time()
    leader = Kosaraju(G,G_rev)
    print "Kosaraju's Algorithm ran in", time.time() - start,"seconds"

    print "Size of the top 5 strongly connected components:"
    print most_common(leader.values(),5)
