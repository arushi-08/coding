class Solution {
    public int minMeetingRooms(int[][] intervals) {
        // idea: need to check if booked room with min end time has freed up before next meeting
        // use min heap -> store end time of curr meeting
        if (intervals.length == 0) return 0;

        Arrays.sort(intervals,
        new Comparator<int[]> () {
            public int compare(int [] a, int [] b){
                return a[0] - b[0];
            }
        } );

        PriorityQueue<Integer> booked_endtimes = new PriorityQueue<>(
            intervals.length,
            new Comparator<Integer> () {
                public int compare(Integer a, Integer b){
                    return a-b;
                }
            }
        );

        booked_endtimes.add(intervals[0][1]);

        for (int i=1; i < intervals.length; i++){
            if (intervals[i][0] >= booked_endtimes.peek()){
                booked_endtimes.poll();
            }
            booked_endtimes.add(intervals[i][1]);
        }
        return booked_endtimes.size();
    }
}
