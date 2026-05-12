class Path {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashSet<Integer> visited = new HashSet<>();
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        Stack<Integer> stack = new Stack<>();

        if (edges.length == 0) {
            return source == destination;
        }

        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];

            graph.putIfAbsent(a, new ArrayList<>());
            graph.get(a).add(b);

            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(b).add(a);
        }

        stack.push(source);
        while (!stack.isEmpty()) {
            int currentVertex = stack.pop();
            for (int neighbor : graph.get(currentVertex)) {
                if (neighbor == destination) {
                    return true;
                }
                if (!visited.contains(neighbor)) {
                    stack.push(neighbor);
                    visited.add(neighbor);
                }
            }
        }

        return false;
    }
}