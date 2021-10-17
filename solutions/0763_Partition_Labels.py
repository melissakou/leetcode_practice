from utils import timer
import collections

class Solution:

    # Solution 1: Greedy, counting frequency
    # @timer
    # def partitionLabels(self, s):
    #     if len(s) == 1:
    #         return 1

    #     s = list(s)
    #     freq = collections.Counter(s)
    #     current_freq = {k: 0 for k in freq.keys()}
    #     partitions_size = []
    #     size = 0
    #     for letter in s:
    #         current_freq[letter] += 1
    #         size += 1
    #         if current_freq[letter] == freq[letter]: current_freq[letter] = 0
    #         if sum(current_freq.values()) == 0:
    #             partitions_size.append(size)
    #             size = 0

    #     return partitions_size

    # Solution 2: Greedy, last appear
    @timer
    def partitionLabels(self, s):
        if len(s) == 1:
            return 1

        last_appear = {letter: i for i, letter in enumerate(s)}
        partitions_size, cur_end = [], 0
        for i, letter in enumerate(s):
            cur_end = max(cur_end, last_appear[letter])
            if i == cur_end:
                partitions_size.append(i - sum(partitions_size) + 1)

        return partitions_size


if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    print(sol.partitionLabels("eccbbbbdec"))