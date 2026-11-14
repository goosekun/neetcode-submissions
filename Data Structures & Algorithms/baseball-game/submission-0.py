class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        record = []
        if not operations:
            return 0
        
        for i in range(len(operations)):
            if operations[i] == "+":
                score = record[-1] + record[-2]
                record.append(score)
            elif operations[i].upper() == "C":
                if not record:
                    continue
                record.pop()
            elif operations[i].upper() == "D":
                record.append(record[-1] * 2)
            else:
                record.append(int(operations[i]))
        
        return sum(record)


                
            