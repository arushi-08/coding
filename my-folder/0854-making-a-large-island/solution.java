class Solution {
    public int largestIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int [][] islands = new int[m][n];
        int [] n_islands = {0};
        int max_island_size = 0;
        Map<Integer, Integer> island_num_to_size_map = new HashMap<>();

        for (int i=0; i < m; i++){
            for (int j=0; j < n; j ++){
                if (islands[i][j] == 0 && grid[i][j] == 1){
                    int island_size = bfs(i,j, grid, islands, n_islands, island_num_to_size_map);
                    max_island_size = Math.max(max_island_size, island_size);
                }
            }
        }

        for (int i=0; i < m; i++){
            for (int j=0; j < n; j ++){
                if (grid[i][j] == 1){
                    int island_size = island_num_to_size_map.get(islands[i][j]);
                    int new_island_size = get_islands_size_after_conversion(
                        i,j, grid, islands, n_islands, island_num_to_size_map
                        );

                    max_island_size = Math.max(
                        max_island_size, 
                        island_size + new_island_size)
                        ;
                }
            }
        }
        if (max_island_size == 0) return 1;
        return max_island_size;
    }

    public int bfs(int x, int y, int [][] grid, int [][] islands, int [] n_islands, Map<Integer, Integer> island_num_to_size_map){
        
        n_islands[0]++;
        islands[x][y] = n_islands[0];

        Queue<int[]> queue = new LinkedList<>();
        int [] pair = {x,y};
        queue.offer(pair);

        int [] rows = {1,0,-1,0};
        int [] cols = {0,1,0,-1};
        
        int island_size = 0;
        while (!queue.isEmpty()){
            int [] curr_pair = queue.poll();
            island_size++;

            int curr_x = curr_pair[0];
            int curr_y = curr_pair[1];
            
            for (int i=0; i < 4; i++){
                if (isSafe(curr_x+rows[i], curr_y+cols[i], grid, islands)){

                    int [] new_pair = {curr_x+rows[i], curr_y+cols[i]};
                    queue.offer(new_pair);
                    islands[curr_x+rows[i]][curr_y+cols[i]] = n_islands[0];
                }
            }
        }
        island_num_to_size_map.put(n_islands[0], island_size);
        return island_size;

    }
        // need to check if I convert 0 to 1,
        //          how much does each island size increase
        // iterate on each cell
        //          it belongs to some island
        //              see its sides,
        //                  whichever side is 0, make it 1
        //                          iterate on its adjacent if we can find 1, then 2 islands are merging -> add that island count also
        //          store island number : island size map
        //                   
    public int get_islands_size_after_conversion(int x, int y, int [][] grid, int [][] islands, int [] n_islands, Map<Integer, Integer> island_num_to_size_map){

        int [] rows = {1,0,-1,0};
        int [] cols = {0,1,0,-1};
        
        int new_island_size = 0;
        for (int i=0; i < 4; i++){
            if (isEdge(x+rows[i], y+cols[i], grid)){
                
                int zero_island_adj_size = 1;
                int zero_x = x + rows[i];
                int zero_y = y + cols[i];
                Set<Integer> seen_islands = new HashSet<>();
                seen_islands.add(islands[x][y]);

                for (int j=0; j < 4; j++){
                    int next_cell_x = zero_x + rows[j];
                    int next_cell_y = zero_y + cols[j];
                    
                    if (0 <= next_cell_x && next_cell_x < grid.length 
                    && 0 <= next_cell_y && next_cell_y < grid[0].length 
                    && grid[next_cell_x][next_cell_y]==1 
                    && !seen_islands.contains( islands[next_cell_x][next_cell_y] ) 
                    ){
                        
                        seen_islands.add(islands[next_cell_x][next_cell_y] );
                        zero_island_adj_size += island_num_to_size_map.get(
                            islands[next_cell_x][next_cell_y]
                        );

                    }
                }
                new_island_size = Math.max(new_island_size, zero_island_adj_size);
            }
        }
        return new_island_size;
    }

    public boolean isSafe(int x, int y, int [][] grid, int [][] islands){
        return (0 <= x && x < grid.length && 0 <= y && y < grid[0].length && grid[x][y]==1 && islands[x][y]==0);
    }

    public boolean isEdge(int x, int y, int [][] grid){
        return (0 <= x && x < grid.length && 0 <= y && y < grid[0].length && grid[x][y]==0);
    }
}
