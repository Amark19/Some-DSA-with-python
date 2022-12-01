"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        we have 3 approaches
        1. Two forloops
            1. create duplicate linked list whose next pointer is set
            2. create a loop which iterate over duplicate list
                2.1 another loop to find random pointer to point
            3. TC :- O(n^2)
        2. Dictinary/hashmaps
            1. create duplicate linked list of original and map original nodes with new created
                1.1 e.g { 1 [next:2 , random:4] : 1 [next : None ,random : None] }
            2. Then we can easily map next & random pointer of each node in duplicate
                2.1 curr = 1
                2.2 dic[curr] is 1[next : None , random: None]
                2.3 set next by copy.next = dic[curr.next] & copy.random = dic[curr.random]
                    2.3.1 dic[curr.next] is 1.next i.e 4 from 1.1 i.e 1.next(dup) = 4
                    2.3.2 same with random
            3. TC :- O(N)
            4. SC :- O(N) we r storing N nodes in hashmap
        3. by setting up zig-zag relation
            3.1 link :- https://www.youtube.com/watch?v=4apaOcK586U
        '''

        dic = {None:None}
        curr = head
        while curr:
            dup = Node(curr.val)
            dic[curr] = dup
            curr = curr.next
        curr = head
        while curr:
            dup = dic[curr]
            dup.next = dic[curr.next]
            dup.random = dic[curr.random]
            curr = curr.next
        return dic[head]
