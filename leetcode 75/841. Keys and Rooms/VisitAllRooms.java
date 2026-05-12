class VisitAllRooms {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        HashSet<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(0);
        visited.add(0);

        while (!stack.isEmpty()) {
            int vertex = stack.pop();

            for (int v : rooms.get(vertex)) {
                if (!visited.contains(v)) {
                    visited.add(v);
                    stack.push(v);
                }
            }
        }

        return visited.size() == rooms.size();
    }
}