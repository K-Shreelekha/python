class node:
    def __init__(self,data)->None:
        self.data=data
        self.next=None
        self.prev=None
class cll:
    def __init__(self)->None:
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
        self.tail.next=self.head
        self.head.prev=self.tail
    def insertatend(self,data):
        if self.head==None:
           self.head=node(data)
           self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        print(self.head.data)
        i=self.head.next
        while i!=self.head:
            print(i.data)
            i=i.next
o=cll()
for i in range(1,6):
    o.insertatbeg(i)
    o.insertatend(i)
o.printing()
