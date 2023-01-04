# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        sum_total=0
        sum_so_far=0
        for i in range(N):
            sum_total=sum_total+A[i]
        for i in range(0,N-1,1):
            
            if sum_so_far==sum_total-sum_so_far-A[i]:
                return i+1
            sum_so_far=sum_so_far+A[i]
        if N==1:
            return 1
        return -1
        # Your code here



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
