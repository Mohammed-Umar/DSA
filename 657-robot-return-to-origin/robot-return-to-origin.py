class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cur_pos = [0,0]
        copy_initial = cur_pos
        for move in moves:
            if move == "U":
                cur_pos[1] += 1
            elif move == "D":
                cur_pos[1] -= 1
            elif move == "L":
                cur_pos[0] -= 1
            elif move == "R":
                cur_pos[0] += 1
        return cur_pos == [0,0]
        
        