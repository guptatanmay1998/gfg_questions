class Solution:
    def sort012(self,arr,n):
        # code here
        i=-1
        for j in range(n):
            if arr[j]==0:
                i=i+1
                temp=arr[i]
                arr[i]=0
                arr[j]=temp
        i=n
        for j in range(n-1,-1,-1):
            if arr[j]==2:
                i=i-1
                temp=arr[i]
                arr[i]=2
                arr[j]=temp
