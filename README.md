###Graph algorithms

##DIJKSTRA's Algorithm:

#OUTPUT

    Shortest Path Lengths:
    {'s1': 0, 's2': 2, 's10': 1, 's12': 2, 's5': 3}
    	This dictionary represents the shortest path lengths from the source vertex 's1' to all other vertices in the graph. The keys are the vertex names, and the values are the shortest path lengths.

    The shortest path from 's1' to 's1' is 0 (since it's the same vertex).
    The shortest path from 's1' to 's2' is 2.
    The shortest path from 's1' to 's10' is 1.
    The shortest path from 's1' to 's12' is 2.
    The shortest path from 's1' to 's5' is 3.
    Shortest Paths:

    {'s1': {'s1': [], 's2': ['s2'], 's10': ['s10'], 's12': ['s10', 's12'], 's5': ['s5']}}
    	This nested dictionary represents the actual paths taken to reach each vertex from the source vertex 's1'. The outer key is the source vertex 's1', and the inner keys are the destination vertices. The values are lists representing the paths.

    	The shortest path from 's1' to 's1' is an empty list [], as no path is needed to reach the same vertex.
    	The shortest path from 's1' to 's2' is ['s2'], which means you go directly from 's1' to 's2'.
    	The shortest path from 's1' to 's10' is ['s10'], which means you go directly from 's1' to 's10'.
    	The shortest path from 's1' to 's12' is ['s10', 's12'], which means you go from 's1' to 's10' and then from 's10' to 's12'.
    	The shortest path from 's1' to 's5' is ['s5'], which means you go directly from 's1' to 's5'.
