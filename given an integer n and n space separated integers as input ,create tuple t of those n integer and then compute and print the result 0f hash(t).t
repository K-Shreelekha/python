if __name__ == '__main__':
    n = int(input())
    #integer_list = map(int, input().split())
    #n=int(input())
    tuple1=map(int,input().split())
    t=tuple(tuple1)
    print(hash(t))

