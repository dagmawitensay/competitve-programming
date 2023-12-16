class ATM:

    def __init__(self):
        self.bank = [0] * 5
        self.amounts = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount):
            self.bank[i] += v

    def withdraw(self, amount: int) -> List[int]:
        self.withdraw_vals = [0] * 5
    
        for i in range(4, -1, -1):
            self.withdraw_vals[i] = min(self.bank[i], amount // self.amounts[i])
            amount -= self.withdraw_vals[i] * self.amounts[i]
        
        if amount == 0:
            for i in range(5):
                self.bank[i] -= self.withdraw_vals[i]
            return self.withdraw_vals
        
        return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)