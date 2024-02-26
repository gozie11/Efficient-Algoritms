class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.times:
            self.times[key].append([value,timestamp])
        else:
            self.times[key]=[[value,timestamp]] #my biggest mistake was initializing this incorrectly with an empty list

    def get(self, key: str, timestamp: int) -> str:
        #returns the greatest value <= timestamp
        #binary serach the values at key

        res, values = "", self.times.get(key, []) 
        l,r = 0,len(values)-1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0] #I incrorrectly changed this +=
                l = m + 1
            else:
                r = m - 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# timebased ** All set timestamps are strictly increasing !! 
# This means the values at key are ordered
# {k:(v1,t1),(v2,t2)}
# {foo:(bar,1),(bar2,4)}
# get(foo@3) -> bar
# get(foo@4) -> bar2
# get(foo@5) -> bar2 # get reutrns the largest time stamp.prev value

