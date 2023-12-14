class Bitset:

    def __init__(self, size: int):
        self.original = ["0"] * size
        self.flipped = ["1"] * size
        self.size = size
        self.flips = 0
        self.zeros = size
        self.ones = size
        

    def fix(self, idx: int) -> None:
        if self.flips % 2 == 0:
            if self.original[idx] == "0":
                self.zeros -= 1
            if self.flipped[idx] == "1":
                self.ones -= 1
            self.original[idx] = "1"
            self.flipped[idx] = "0"
        else:
            if self.original[idx] == "1":
                self.zeros += 1
            if self.flipped[idx] == "0":
                self.ones += 1
            self.original[idx] = "0"
            self.flipped[idx] = "1"

    def unfix(self, idx: int) -> None:
        if self.flips % 2 == 0:
            if self.original[idx] == "1":
                self.zeros += 1
            if self.flipped[idx] == "0":
                self.ones += 1
            self.original[idx] = "0"
            self.flipped[idx] = "1"
        else:
            if self.original[idx] == "0":
                self.zeros -= 1
            if self.flipped[idx] == "1":
                self.ones -= 1
            self.original[idx] = "1"
            self.flipped[idx] = "0"

    def flip(self) -> None:
        self.flips += 1

    def all(self) -> bool:
        if self.flips % 2 == 0:
            if not self.zeros:
                return True
            return False
        else:
            if self.ones == self.size:
                return True
            return False

    def one(self) -> bool:
        if self.flips % 2 == 0:
            if self.zeros < self.size:
                return True
            return False
        else:
            if self.ones > 0:
                return True
            return False

    def count(self) -> int:
        if self.flips % 2 == 0:
            return self.size - self.zeros
        
        return self.ones

    def toString(self) -> str:
        # print("".join(self.original), "".join(self.flipped))
        if self.flips % 2 == 0:
            return "".join(self.original)
        
        return "".join(self.flipped)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()