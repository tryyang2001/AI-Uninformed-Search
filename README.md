# AI-Uninformed-Search
This repo contains the code for the implementation of uninformed search in AI such as Breadth First Search (BFS), Depth First Search (DFS), Uniformed Cost Search (UCS) ad A* Search.

## Problem

Given a chess piece _King_, try to find a path for it to escape from the chess board. The chess board will include some obstacles and enemies. The _King_ cannot step on any obstacle, 
and it is also disallowed to step on the positions where the enemy is guarding. 

The input will be given as a text file (.txt). Examples can be found under the folder _Public Testcases_. 

The output is a tuple with the first element being a list which shows the movement of position for the _King_, and the second element being the nodes explored by the _King_ during its
searching algorithm. Note that for UCS and AStar there are also a third element which indicates the path cost required for the path found. This path cost should be optimal.

The moment of each piece is as follow:

![Movement of each piece](image.png)
