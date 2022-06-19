import sys
input = sys.stdin.readline

def start(storage):
    btarget, bcnt = [], 0
    for r in range(R):
        for c in range(C):
            sq = storage[r][c]
            if sq in ["b"]:
                bcnt += 1
            if sq in ["W","w"]:
                sx, sy = r, c
            if sq in ["W", "B", "+"]:
                btarget.append([r,c])
    return bcnt, sx, sy, btarget

def carry(storage, dir):
    global res
    cnt, x, y, target = start(storage)
    empty, box = [".","+"], ["B", "b"]
    for m in move:
        dx, dy = dir[m]
        cx, cy = x+dx, y+dy
        s1 = storage[cx][cy]
        if s1 in empty:
            x, y = cx, cy
        elif s1 in box:
            fx, fy = cx+dx, cy+dy
            s2 = storage[fx][fy]
            if s2 in empty:
                x, y = cx, cy
                storage[fx][fy] = "b"  
                if [fx,fy] in target:
                    storage[fx][fy] = "B"
                    cnt -= 1
                storage[cx][cy] = "w"
                if [cx,cy] in target:
                    storage[cx][cy] = "W"
                    cnt += 1
        if not cnt:
            res = "complete"
            return res
    return res


tc = 0
dir = {
    "U" : (-1, 0),
    "D" : (1, 0),
    "L" : (0, -1),
    "R" : (0, 1),
}
res = "incomplete"
while True:
    tc += 1
    R, C = map(int, input().split())
    if not (R*C):
        break
    storage = [list(input()) for _ in range(R)]
    move = list(input())
    status = carry(storage, dir)
    print("Game %d: %s"%(tc,status))
    for row in storage:
        print("".join(row))