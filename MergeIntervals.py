def  merge(intervals):
    new_intervals = []
    for interval in intervals:
        if interval not in new_intervals:
            new_intervals.append(interval)
    new_intervals.sort()
    ctr = 0
    if len(new_intervals) == 1:
        return new_intervals
    else:
        for  i in range(1,len(new_intervals)):
            if new_intervals[i-1][-1] >= new_intervals[i][0]:
                if new_intervals[i-1][-1] >= new_intervals[i][-1]:
                    first = new_intervals[i-1][0]
                    last = new_intervals[i-1][-1]
                    new_intervals[i-1],new_intervals[i] = new_intervals[i],new_intervals[i-1]
                else:
                    first = new_intervals[i-1][0]
                    last = new_intervals[i][-1]
                new_intervals[i]= [first,last]
                new_intervals[i-1]=0
                merged = [interval for interval in new_intervals if interval != 0]
                ctr += 1
        if ctr == 0:
            return new_intervals
        return merged





print(merge([[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]))
# values =[[0,2],[1,4],[3,5]]
# i = values.index([0,2])
# values[i:i+2]=[[0,4]]
# print(values)
# values = [[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]
