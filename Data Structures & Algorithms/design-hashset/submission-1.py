class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.L = 999
        self.hashMap = [ListNode(0) for i in range(999)]
    def add(self, key: int) -> None:
        
        head = self.hashMap[key % self.L]

        while head.next:
            if head.next.val == key:
                return 

        head.next = ListNode(key)

        



    def remove(self, key: int) -> None:
        
        head = self.hashMap[key % self.L]

        while head.next:
            if head.next.val == key:
                head.next = head.next.next
                return 

        
    def contains(self, key: int) -> bool:
        head = self.hashMap[key % self.L]

        while head.next:
            if head.next.val == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)