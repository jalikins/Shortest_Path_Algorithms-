## Runtime and Complexity Analysis

The performance of each algorithm varies based on its approach to exploring the 50x50 grid environment. Below is a comparison of their theoretical time and space complexities, where V represents the number of vertices and E represents the number of edges.

| Algorithm | Theoretical Time Complexity | Space Complexity | 
| :--- | :--- | :--- |
| A\* | $O(E + V \log V)$ | $O(V)$ |
| Dijkstra | $O(E + V \log V)$ | $O(V)$ |
| Bellman-Ford | $O(V \times E)$ | $O(V)$ |

### Theoretical vs. Practical Performance

*   A\* Search: A* shares the same worst case theoretical time complexity as Dijkstra, its runtime is drastically faster. By using a heuristic function to estimate the distance to the target, A* prioritizes nodes that move closer to the goal. On an open grid, it explores a narrow corridor directly toward the destination rather than searching uniformly, minimizing the actual number of nodes evaluated.
*   Dijkstra's Algorithm: Dijkstra expands uniformly in all directions. Because it lacks a heuristic to guide it toward a specific target, it calculates the shortest path to all surrounding nodes until it blindly encounters the destination. This guarantees an accurate shortest path but requires evaluating significantly more of the 2,500 available grid nodes than A*, leading to a slower practical runtime. 


### Empirical Benchmarks

*   A\* Runtime: ~0.008s
*   Dijkstra Runtime: ~0.045s
*   Bellman-Ford Runtime: Didn't do this one
