class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // Build Frequence Map
        Map<Integer, Integer> freq_map = new HashMap<>();

        for (int n : nums) {
            freq_map.put(n, freq_map.getOrDefault(n, 0) + 1);
        }

        // Use Heap to maintain the top k elements
        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
            (a, b) -> a.getValue() - b.getValue()
        );

        for (Map.Entry<Integer, Integer> entry : freq_map.entrySet()) {
            heap.offer(entry);

            if (heap.size() > k) {
                heap.poll(); // remove the least freq
            }
        }

        // Extract result
        int[] result = new int[k];
        int i = 0;
        while ( !heap.isEmpty() ) {
            result[i++] = heap.poll().getKey();
        }

        return result;
    }
}
