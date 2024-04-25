class node:
    def __init__(self,data)->None:
        self.data=data                                                                       
        self.next=None
class sll:
    def __init__(self)->None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
           self.head=node(data) 
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
           self.head=node(data)   
        else:
            temp=node(data)
            i=self.head
            while i.next:
                i=i.next
            i.next=temp
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i!=None:
            print(i.data,end=" ")
            i=i.next
    def length(self):
        c=0
        i=self.head
        while i:
            c+=1
            i=i.next
        return c
l=[1,2,3,4,5] 
o=sll()
for i in l:
    o.insertatbeg(i)
    o.insertatend(i)
o.printing()
print(o.length())                   



