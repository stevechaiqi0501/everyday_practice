class SolutionFor77:
    def climbstairs(self,n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbstairs(n-1) + self.climbstairs(n-2)
    
    