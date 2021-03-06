// { Driver Code Starts
// Counts Palindromic Subsequence in a given String
#include<iostream>
#include<cstring>
using namespace std;
 
// Function return the total palindromic subsequence
int countPS(string str);
 
// Driver program
int main()
{
   int t;
	cin>>t;
   while(t--)
	{
	string str;
cin>>str;
cout<<countPS(str)<<endl;
} 
}// } Driver Code Ends


/*You are required to complete below method */

int dp[1001][1001];

int func(int i, int j, string s){
    
    if(i>j) return 0;
    
    if(i==j) return 1;
    
    if(dp[i][j]!=-1) return dp[i][j];
    
    if(s[i]==s[j]) return dp[i][j] = func(i+1,j,s) + func(i,j-1,s) + 1;
    else return dp[i][j] = func(i+1,j,s) + func(i,j-1,s) - func(i+1,j-1,s);
}

int countPS(string str)
{
   //Your code here
   int n = str.length();
   dp[n][n];
   memset(dp,-1,sizeof(dp));
   return func(0,n-1,str);
}
 