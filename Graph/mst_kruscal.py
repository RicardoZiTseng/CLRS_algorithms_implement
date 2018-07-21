"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 366 in chapter 23

Discription of the algorithms:
MST-KRUSKAL(G, w)
1   A = φ
2   for each vertex v ∈ G.V
3       MAKE-SET(v)
4   sort the edges of G.E in nonincreasing order by weight w
5   for each edge(u, v) ∈ G.E, taken in nondecreasing order by weight
6       if FIND-SET(u) ≠ FIND-SET(v)
7           A = A ∪ {(u, v)}
8           UNION(u, v)
9   return A
"""