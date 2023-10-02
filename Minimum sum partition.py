'''
Given an array arr of size n containing non-negative integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference.
'''
class Solution:
	def minDifference(self, arr, n):
		def solve(arr,n,total,cursum,dp):
		    if(n==0):
		        return (abs((total-cursum)-cursum))
		        
		    if(dp[n][cursum]!=-1):
		        return dp[n][cursum]
	        
	        else:
	            dp[n][cursum]=min(solve(arr,n-1,total,arr[n-1]+cursum,dp),solve(arr,n-1,total,cursum,dp))
	            return dp[n][cursum]
		total=sum(arr)
		cursum=0
		dp=[[-1 for i in range(total+1)] for j in range(n+1)]
		return solve(arr,n,total,cursum,dp)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)
