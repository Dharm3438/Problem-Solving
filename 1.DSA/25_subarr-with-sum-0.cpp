// { Driver Code Starts
// A C++ program to find if there is a zero sum
// subarray
#include <bits/stdc++.h>
using namespace std;


bool subArrayExists(int arr[], int n);
// Driver code
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    for(int i=0;i<n;i++)
	    cin>>arr[i];
	    	if (subArrayExists(arr, n))
		cout << "Yes\n";
	else
		cout << "No\n";
	}
	return 0;
}// } Driver Code Ends


//Complete this function
bool subArrayExists(int arr[], int n)
{
    int i;
    int s = 0;
    int f = 0;
    unordered_map<int,int> m;
    for (i=0;i<n;i++)
    {
        s = s + arr[i];
        if(s==0 or m[s] or arr[i]==0){
            f = 1;
            break;
        }
        else{
            m[s] = 1;
        }
    }
    if(f==1){
        return 1;
    }
    else{
        return 0;  
    }
}


