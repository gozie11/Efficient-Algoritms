class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tm = {}
        tt = {}

        #trusts me tracker
        for x in range(n):
            tm[x+1] = 0
            tt[x+1] = 0

        #if someone has n-1 trusters 
        #and 0 trustees they are the judge

        for person in trust:
            tm[person[1]] += 1
            tt[person[0]] += 1
        
        valid_judge = 0

        for person in tt:
            if tt[person] == 0:
                valid_judge += 1
# one person trusts nobody but the are not trusted by all
        if valid_judge:
            for person in tt:
                print(tt[person],"how many i trust")
                if tt[person] == 0 and tm[person] == n-1:
                    print(tt[person],"how many i trust")
                    return person



        return -1
