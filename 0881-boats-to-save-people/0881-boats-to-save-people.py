class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        beg =  0
        end =  len(people) - 1
        boats = 0
        bweight = limit
        people.sort()
        while beg  <= end:
            if (beg ==  end):
                boats += 1
                beg += 1
            elif (people[beg] +  people[end] <= limit):
                boats += 1
                beg += 1
                end -= 1
            else:
                if people[beg] >= people[end]:
                    beg += 1
                else:
                    end -= 1
                boats += 1
        return boats
