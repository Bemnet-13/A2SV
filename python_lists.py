if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        inputs = input().split()
        if inputs[0] == 'print':
            print(lst)
        elif inputs[0] == "reverse":
            lst.reverse()
        elif inputs[0] == 'sort':
            lst.sort()
        elif inputs[0] == 'pop':
            lst.pop()
        elif inputs[0] == 'insert':
            lst.insert(int(inputs[-2]), int(inputs[-1]))
        elif inputs[0] == 'remove':
            lst.remove(int(inputs[-1]))
        else:
            lst.append(int(inputs[-1]))