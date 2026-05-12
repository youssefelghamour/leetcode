class FindProvinces {
    public int findCircleNum(int[][] isConnected) {
        int count = 0;
        HashSet<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < isConnected.length; i++) {
            if (!visited.contains(i)) {
                count++;
                stack.push(i);
                visited.add(i);
                while (!stack.isEmpty()) {
                    int iNode = stack.pop();
                    int[] iConnections = isConnected[iNode];
                    for (int j = 0; j < iConnections.length; j++) {
                        if (!visited.contains(j)) {
                            if (isConnected[iNode][j] == 1) {
                                stack.push(j);
                                visited.add(j);
                            }
                        }
                    }
                }
            }
        }

        return count;
    }
}