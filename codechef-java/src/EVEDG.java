import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Node {
    int id;
    int value;

    Node(int id, int value){
        this.id = id;
        this.value = value;
    }
}

class Graph {
    private final HashMap<Node, LinkedList<Node>> adjacencyMap;

    public Graph() {
        adjacencyMap = new HashMap<>();
    }

    public void addEdgeHelper(Node a, Node b) {
        LinkedList<Node> tmp = adjacencyMap.get(a);

        if (tmp != null) {
            tmp.remove(b);
        }
        else tmp = new LinkedList<>();
        tmp.add(b);
        adjacencyMap.put(a,tmp);
    }

    public void addEdge(Node source, Node destination) {
        // We make sure that every used node shows up in our .keySet()
        if (!adjacencyMap.containsKey(source))
            adjacencyMap.put(source, null);

        if (!adjacencyMap.containsKey(destination))
            adjacencyMap.put(destination, null);

        addEdgeHelper(source, destination);
        addEdgeHelper(destination, source);
    }

    public void printEdges() {
        for (Node node : adjacencyMap.keySet()) {
            System.out.print("The " + node.id + " has an edge towards: ");
            if (adjacencyMap.get(node) != null) {
                for (Node neighbor : adjacencyMap.get(node)) {
                    System.out.print(neighbor.id + " ");
                }
                System.out.println();
            }
            else {
                System.out.println("none");
            }
        }
    }

    public boolean hasEdge(Node source, Node destination) {
        return adjacencyMap.containsKey(source) && adjacencyMap.get(source) != null && adjacencyMap.get(source).contains(destination);
    }


    public int dfsAndCut(Node start, int sum) {
        Stack<Node> stack = new Stack<>();
        int sumA = 0;
        int sumB = sum;
        int minSum = sumB;

        // System.out.println("sumA = " + sumA);
        // System.out.println("sumB = " + sumB);

        boolean[] isVisited = new boolean[adjacencyMap.size() + 1];
        stack.push(start);
        while (!stack.isEmpty()) {
            // System.out.println("stack = " + stack);
            Node current = stack.pop();
            isVisited[current.id] = true;
             System.out.println("current.id = " + current.id);
            sumB -= current.value;
            sumA += current.value;

            minSum = Math.min(Math.abs(sumB-sumA), minSum);

            if (minSum == 525) {
                System.out.println("sumA = " + sumA);
                System.out.println("sumB = " + sumB);
                System.out.println("current = " + current.id);
            }

            // System.out.println("sumA = " + sumA);
            // System.out.println("sumB = " + sumB);

            if (adjacencyMap.get(current) != null) {
                for (Node dest : adjacencyMap.get(current)) {
                    // System.out.println("LINE 97");
                    // System.out.println("isVisited = " + Arrays.toString(isVisited));
                    // System.out.println("dest = " + dest);
                    if (!isVisited[dest.id]) {
                        // System.out.println("Push");
                        stack.push(dest);
                    }
                }
            }
        }
        return minSum;
    }

}



class EVEDGResult {
    public static int EVEDG(List<Integer> data, List<List<Integer>> edges, int numberOfNodes) {
        Graph g = new Graph();

        Node[] nodes = new Node[numberOfNodes + 1];
        int sum = 0;

        for (int i = 1; i <= numberOfNodes; i++) {
            nodes[i] = new Node(i, data.get(i-1));
            sum += data.get(i-1);
        }

        for (List<Integer> edge: edges){
            g.addEdge(nodes[edge.get(0)], nodes[edge.get(1)]);
        }

//        g.printEdges();

        return g.dfsAndCut(nodes[1], sum);
    }

}

class EVEDG {
    public static void main(String[] args) throws IOException {
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int input = 1;
        BufferedReader bufferedReader = new BufferedReader(new FileReader("io/EVEDG/input."+input+".txt"));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("io/EVEDG/output."+input+".txt"));

        int test_cases = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> data = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<List<Integer>> edges = new ArrayList<>();

        System.out.println("edges = " + edges);

        IntStream.range(0, test_cases - 1).forEach(i -> {
            try {
                edges.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = EVEDGResult.EVEDG(data, edges, test_cases);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
