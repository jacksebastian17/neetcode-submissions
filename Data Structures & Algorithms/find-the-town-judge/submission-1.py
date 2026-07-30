class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # iterate over n people (1->n)
        # check if ith person is town judge by going over trust list and seeing if trusted count
        #    (so number of times ai -> n) is equal to n-1
        # also check that ith person is never ai
        # that will be town judge if so
        for i in range (1,n+1):
            # check if person i is town judge
            print("checking person", i)
            numTrusts = 0
            for t in trust:
                ai = t[0]
                bi = t[1]
                print(ai, "trusts", bi)
                if ai == i:
                    print("break")
                    numTrusts = 0
                    break
                if bi == i:
                    numTrusts += 1
            print("numTrusts == ", numTrusts)
            if numTrusts == n - 1:
                print("found town judge! == ", i)
                return i
        return -1
