class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # [3,4,4,5] # Limit = 6
        res = 0
        people.sort()
        L , R = 0 , len(people)-1
        while L <= R:
            if people[L] + people[R] <= limit:
                L +=1
                R-=1
            else:
                R-=1
            res +=1
        return res