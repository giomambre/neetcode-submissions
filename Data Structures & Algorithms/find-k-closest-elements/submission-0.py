class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        cur_min = float("inf")
        min_idx = 0
        for i,num in enumerate(arr):

            if abs(num-x) < cur_min:
                min_idx = i
                cur_min = abs(num-x)

        L, R = min_idx, min_idx

        while (R-L+1) < k:

            if(L-1) <0:
                R+=1
                continue
            if (R+1)>=len(arr):
                L-=1
                continue
            elif abs(arr[L-1]-x)<=abs(arr[R+1]-x):
                L-=1
            else:
                R+=1

        return arr[L:R+1] 

