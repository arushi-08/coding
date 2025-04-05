class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # given a string s
        # paritition string into as many parts as possible so that each letter appears in at most one part
        # e.g. ababcc into [abab, cc]
        # this is similar to yesterday's session question

        # ababcbacadefegdehijhklij

        """
        use hashmap of { letter : [partition, partition_start] }
        for letter in s:
            if letter already seen previously:
                letter is part of partition
                calculate size from idx to partition start
                remove any partitions added to hashmap after this partition
            else:
                possibly new partition start, add it to hashmap

        for start in s:
            for end in (start+1, s):
                for i in (start, end):
                    for j in s:
        
        sliding window?

        letter: [minidx1, maxidx3]
        the min and max idx is the partition size for that letter
        a:[0,8]
        b:[1,3]
        left to right record first idx
        right to left record last idx
        
        left to right iterate and check each element when does element start, end
        [8,9,8,3,7,...]
        
        n^2, for i in s:
                for j in i, s[i]
        """

        # first_idx = [0] * len(s)
        last_idx = [0] * len(s)
        visited = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in visited:
                visited[s[i]] = i
            last_idx[i] = visited[s[i]]

        partition_count_list = []
        i = 0
        print('last_idx', last_idx)
        # partition list has the subset of last idx from 1st to its last idx
        # there can be another char not at 0th idx who last idx is later
        start = i
        while i < len(s):
            # print('last_idx[i]', last_idx[i], 'i', i)
            # 
            partition_list = last_idx[ i:last_idx[i]+1 ]
            # print('partition_list', partition_list)
            
            max_elem = max(partition_list)
            while max_elem != last_idx[ last_idx[i] ]:
                partition_list = last_idx[ last_idx[i]:max_elem+1 ]
                i = max_elem
                max_elem = max(partition_list)
                # print('max_elem', max_elem, 'i', i)

            partition_count_list.append(
                max_elem + 1 - start
            )
            i = max_elem + 1
            start = i
            # print('max_elem', max_elem, i, len(s))
        
        return partition_count_list


