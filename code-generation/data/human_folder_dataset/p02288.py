n = int(input())
tree = list(map(int, input().split()))

def main() :
    createHeap(n)
    print('', ' '.join(map(str, tree)))

def createHeap(x):
    for i in range((x - 1) // 2, -1, -1) :
        maxHeap(i)

def maxHeap(i) :
    if i * 2 + 1 >= n:
        return

    tmp = i * 2 + 1

    if i * 2 + 2 < n :
        if tree[i * 2 + 1] < tree[i * 2 + 2] :
            tmp = i * 2 + 2

    if tree[i] < tree[tmp] :
        tree[i], tree[tmp] = tree[tmp], tree[i]
        maxHeap(tmp)

if __name__ == '__main__':
    main()

