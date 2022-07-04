import networkx as nx
import matplotlib.pyplot as plt

# -------------------------------------------------------
global p
p=[]
 
def dfs(graph, start, goal):
    close, open, temp = [], [], []
    open.append([start])
    while open:  # not empty
        last_list_in_open = open.pop()  # get the last list([1, 2] OR [1] ...)
        # get the last node in the top list(2 OR 1 ...)
        visited_node = last_list_in_open[-1]
        close.append(visited_node)  # put the node in the expanded list
        if visited_node == goal:  # check if my current node is the goal or not
            global p
            p = last_list_in_open
            return close  # print the expanded nodes
        # if it is not the goal, get all the child of this node
        for child in graph[visited_node]:
            my_list = list(last_list_in_open)  # list
            my_list.append(child)
            temp.append(my_list)
        while temp:
            open.append(temp.pop())
# -------------------------------------------------------


def bfs(graph, start, goal):
    close, open, temp = [], [], []
    open.append([start])
    while open:
        last_list_in_open = open.pop()
        visited_node = last_list_in_open[-1]
        close.append(visited_node)
        if visited_node == goal:
            global p
            p = last_list_in_open
            return close
        for child in graph[visited_node]:
            my_list = list(last_list_in_open)
            my_list.append(child)
            temp.append(my_list)
        if len(open) == 0:
            while temp:
                open.append(temp.pop())
# -------------------------------------------------------

def change_node_color(i, myPath):
    color_map.clear()
    flage = True
    
    noOfRed=0    
    for node in G.nodes():
        if node in myPath:  # to make all the path red until the node i
            if flage:# if not the nodes befor node i is red
            
                if (myPath.index(node))<=(myPath.index(i)):#Make the nodes red in the order in the path
                    color_map.append('red')
                    noOfRed+=1
                    myIndex=myPath.index(i)+1
                    
                    if myIndex==noOfRed: # all the nodes befor node i is red
                        flage = False
                        
                else:
                    color_map.append('pink')
                    
            else:
                color_map.append('pink')
            
        else:
            color_map.append('pink')

# -------------------------------------------------------

def change_path(myPath,sup):
    color_map.clear()
    for node in G.nodes():
        if node in myPath:  # to make all the path violet
            color_map.append('violet')
        else:
            color_map.append('pink')
    plt.subplot(sup)#121,122
    draw_my_graph()
# -------------------------------------------------------


def draw_my_graph():
    nx.draw(G, pos=myPosition, with_labels=True, node_size=1100,
            node_color=color_map, font_weight='bold', font_size=10)
# -------------------------------------------------------


G = nx.Graph()
graph = {'start': [2, 3],
         2: [4, 5], 3: [6, 7],
         4: [8, 9], 5: [10, 11], 6: [12, 13], 7: [14, 15],
         8: [16], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [],
         16: []}

for i, j in graph.items():
    for k in j:
        G.add_edge(i, k)

# draw the graph
myPosition = nx.spring_layout(G)
color_map = []
for node in G:
    color_map.append('pink')

#half graph dfs and half bfs
subax1 = plt.subplot(121)
draw_my_graph()
subax2 = plt.subplot(122)
draw_my_graph()

# paint the expanded nodes with red

# dfs in the left
plt.pause(1)
myList = dfs(graph, 'start', 16)

for i in myList:
    change_node_color(i, myList)
    subax1 = plt.subplot(121)
    draw_my_graph()
    plt.pause(1)
change_path(p,121)#change the color of the whole path

# bfs in the right
myList = bfs(graph, 'start', 16)
for i in myList:
    change_node_color(i, myList)
    subax1 = plt.subplot(122)
    draw_my_graph()
    plt.pause(1)
change_path(p,122)

draw_my_graph()

plt.show()
