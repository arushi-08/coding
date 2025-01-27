class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();
        int[][] dp = new int[numCourses][numCourses];

        for(int i=0; i < prerequisites.length; i++){
            int p = prerequisites[i][0];
            int c = prerequisites[i][1];
            graph.putIfAbsent(c, new ArrayList<>());
            graph.get(c).add(p);
            dp[c][p] = 1;
        }

        for (int i=0; i<numCourses; i++){
            queue.offer(i);
            Set<Integer> visited = new HashSet<>();
            visited.add(i);

            while (!queue.isEmpty()){
                int course = queue.poll();
                if (graph.containsKey(course)){
                    List<Integer> prereqs = graph.get(course);
                    for(int j=0; j<prereqs.size(); j++){
                        int prereq = prereqs.get(j);
                        if (!visited.contains(prereq)){
                            queue.offer(prereq);
                            dp[i][prereq] = 1;
                            visited.add(prereq);
                        }
                    }
                }
            }
        }

        List<Boolean> ans = new ArrayList<>(queries.length);

        for (int i=0; i<queries.length; i++){
            int p = queries[i][0];
            int c = queries[i][1];
            if (dp[c][p] == 1){
                ans.add(true);
            }else{
                ans.add(false);
            }
            
        }

        return ans;
    }
}
