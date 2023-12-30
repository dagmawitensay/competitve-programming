class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.curr_pos = (0, 0)
        self.curr_dir = "East"
        self.directions = {"East": (1, 0), "West": (-1, 0), "South": (0, -1), "North": (0, 1)}

    def step(self, num: int) -> None:
        num %= (2 * (self.width + self.height - 2))
        if num == 0:
            num = 2 * (self.width + self.height - 2)
        while num > 0:
            direct = self.directions[self.curr_dir]   
            if self.isValid(direct[0] + self.curr_pos[0], direct[1] + self.curr_pos[1]):
                self.curr_pos = (direct[0] + self.curr_pos[0], direct[1] + self.curr_pos[1])
                num -= 1
            else:
                if self.curr_dir == "East":
                    self.curr_dir = "North"
                elif self.curr_dir == "West":
                    self.curr_dir = "South"
                elif self.curr_dir == "South":
                    self.curr_dir = "East"
                elif self.curr_dir == "North":
                    self.curr_dir = "West"

    def getPos(self) -> List[int]:
        return self.curr_pos

    def getDir(self) -> str:
        return self.curr_dir
    
    def isValid(self, i, j):
        return 0 <= i < self.width and 0 <= j < self.height
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()