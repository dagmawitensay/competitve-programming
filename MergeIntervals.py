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





