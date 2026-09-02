class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer = []

        def isNumber(num) :
            try :
                int(num)
                return True
            except :
                return False

        for t in tokens :
            if isNumber(t) :
                answer.append(t)
                

            else :
                num2 = int(answer.pop())
                num1 = int(answer.pop())

                if t == '+':
                    ans = num1+num2
                elif t == '-':
                    ans = num1-num2
                elif t == '*':
                    ans = num1*num2
                else :
                    ans = int(num1/num2)

                answer.append(ans)
            
        return int(answer[0])
