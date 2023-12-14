class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.frequency_set = {}
    
    def add(self, number: int) -> None:
        if number in self.freq and self.freq[number] in self.frequency_set:
            self.frequency_set[self.freq[number]] -= 1
            if self.frequency_set[self.freq[number]] == 0:
                del self.frequency_set[self.freq[number]]

        self.freq[number] = self.freq.get(number, 0) + 1
        self.frequency_set[self.freq[number]] = self.frequency_set.get(self.freq[number], 0) + 1
        
    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.frequency_set[self.freq[number]] -= 1
            if self.frequency_set[self.freq[number]] == 0:
                del self.frequency_set[self.freq[number]]
            self.freq[number] -= 1
            if self.freq[number] == 0:
                del self.freq[number]
            else:
                self.frequency_set[self.freq[number]] = self.frequency_set.get(self.freq[number], 0) + 1

    
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequency_set:
            return True
        
        return False

    # 3: 2


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)