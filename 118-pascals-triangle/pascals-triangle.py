class Solution(object):
    def fact(self,num):
        if num==0 or num==1:
            return 1
        else:
            return num*self.fact(num-1)


    def generate(self, numRows):
        a=[]
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                v=self.fact(i)//(self.fact(j)*self.fact(i-j))
                row.append(v)
            a.append(row)
        return a
            
                
        