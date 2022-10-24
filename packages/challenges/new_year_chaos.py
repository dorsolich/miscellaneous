def minimumBribes(q):
    # Write your code here
    bribes = 0
    bool_break = False
    for i in range(1, len(q)):
        jump = 0
        prev = q[i-1]
        latest = q[i]
        if prev > latest:
            jump = 1
        if prev > i:
            jump = prev - i
            if jump > 2:
                print("Too chaotic")
                bool_break = True
                break
        bribes += jump
    if not bool_break:
        print(bribes)
        
# if __name__ == "main":
q = [1,2,3,5,4,6,7,8]
q = [1,2,5,3,7,8,6,4]
minimumBribes(q)
print("done")