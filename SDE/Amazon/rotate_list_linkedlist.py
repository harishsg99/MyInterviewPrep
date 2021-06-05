class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
     def rotateRight(self, A, B):
        curr=A
        n=0
        while curr:
            n+=1
            curr=curr.next
        B=B%n
        if B==0:
            return A
        m=n-B
        s=1
        prev=curr=A
        while curr and s<=m:
            prev=curr
            curr=curr.next
            s+=1
        prev.next=None
        new=curr
        while curr.next!=None:
            curr=curr.next
        curr.next=A
        return new
