class Solution {
    public int minReorder(int n, int[][] connections) {
        Map<Integer, List<Pair<Integer, Boolean>>> graph = new HashMap<>();
        int count = 0;
        Stack<Integer> stack = new Stack<>();
        HashSet<Integer> visited = new HashSet<>();

        for (int[] connection: connections) {
            int a = connection[0];
            int b = connection[1];

            graph.putIfAbsent(a, new ArrayList<>());
            graph.get(a).add(
                new Pair<>(b, true)
            );

            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(b).add(
                new Pair<>(a, false)
            );
        }

        stack.push(0);
        visited.add(0);

        while (!stack.isEmpty()) {
            int current = stack.pop();

            for (Pair<Integer, Boolean> edge : graph.get(current)) {
                int neighbor = edge.getKey();
                boolean isOriginalDirection = edge.getValue();

                if (!visited.contains(neighbor)) {
                    stack.push(neighbor);
                    visited.add(neighbor);

                    count += isOriginalDirection ? 1 : 0;
                }
            }
        }

        return count;
    }
}