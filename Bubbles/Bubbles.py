# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

from collections import defaultdict 
#This class represents a undirected graph using adjacency list representation 
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 


    # function to add an edge to graph 
    def addEdge(self,v,w): 
        self.graph[v].append(w) #Add w to v_s list 
        self.graph[w].append(v) #Add v to w_s list 

    # A recursive function that uses visited[] and parent to detect 
    # cycle in subgraph reachable from vertex v. 
    def isCyclicUtil(self,v,visited,parent): 

        #Mark the current node as visited  
        visited[v]= True

        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            # If the node is not visited then recurse on it 
            if  visited[i]==False :  
                if(self.isCyclicUtil(i,visited,v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=i: 
                return True

        return False


    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self): 
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
        for i in range(self.V): 
            if visited[i] ==False: #Don't recur for u if it is already visited 
                if(self.isCyclicUtil(i,visited,-1))== True: 
                    return True

        return False


num_of_testes = get_number()
for _ in range(num_of_testes):
    vertices = get_number()
    edges = get_number()

    g = Graph(vertices)

    for _ in range(edges):
        g.addEdge(get_number(), get_number())

    print(1 if g.isCyclic() else 0)
