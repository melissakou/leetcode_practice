from utils import timer

class Solution:
    
    # Solution 1: Count & Sort
    @timer
    def frequencySort(self, s):
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        count = sorted(list(count.items()), key=lambda x: -x[1])
        
        return ''.join([c[0] * c[1] for c in count])


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))
    print(sol.frequencySort("cccaaa"))
    print(sol.frequencySort("Aabb"))