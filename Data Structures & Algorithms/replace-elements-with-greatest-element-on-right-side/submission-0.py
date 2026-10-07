class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxcurr = -1
        for i in range(len(arr)-1, -1, -1):
            newmax = max(arr[i], maxcurr)
            arr[i] = maxcurr
            maxcurr = newmax
        return arr