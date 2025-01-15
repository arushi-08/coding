class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # hashset not optimal
        #   because we can prune/eliminate some numbers from nums that don't result in required prefix
        # e.g. we infer after 2 bits that 25 elem xor with 5 or 3 will give max xor
        #   and we can remove checking 10, 25 from nums
        # so we can prune prefixes set
        # this is done using bitwise trie

        # form bitwise trie for each element
        # to get max xor, see if the opposite bit is present in the trie at each step
        # if it is, add 1 to maxxor
        # else don't add 1 to maxxor

        maxelem = max(nums)
        L = len(bin(maxelem)) - 2
        trie = {}
        bin_nums = []
        for num in nums:
            # L = 5
            # 1 << L left shift 1 L times -> 100000 (6 zero's)
            bits = []
            for i in range(L-1,-1,-1):
                bits.append((num >> i) & 1)
            bin_nums.append(bits)

            self.add_to_trie(bits, trie)
            
        max_xor = 0
        for num in bin_nums:
            curr_xor = 0
            xnode = trie
            for bit in num:
                opp_bit = 1 - bit
                if opp_bit in xnode:
                    curr_xor = curr_xor << 1 | 1
                    xnode = xnode[opp_bit]
                else:
                    curr_xor <<= 1
                    xnode = xnode[bit]
            
            max_xor = max(max_xor, curr_xor)

        return max_xor
        # for i in range(L-1,-1,-1):
        #     if 
            
    
    def add_to_trie(self, bits, trie):
        for bit in bits:
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]
        trie['#'] = {}

