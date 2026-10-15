class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scorecard = []
        for op in operations:
            if op=="+":
                scorecard.append(scorecard[-1]+scorecard[-2])
            elif op=="D":
                scorecard.append(scorecard[-1]*2)
            elif op=="C":
                scorecard.pop()
            else:
                scorecard.append(int(op))
        return sum(scorecard)