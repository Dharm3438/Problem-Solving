#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	
	while(t--){
	    int n,m;
	    cin>>m>>n;
	    int a[m], b[n];
	    for(int i=0;i<m;i++) cin>>a[i];
	    for(int i=0;i<n;i++) cin>>b[i];
	    
	    unordered_map<int,int> m1;
	    for(int i=0;i<m;i++) m1[a[i]]++;
	    
	    int flg = 0;
	    
	    for(int i=0;i<n;i++){
	        if(m1[b[i]]){
	   
	        }
	        else{
	            flg=1;
	            break;
	        }
	    }
	    
	    if(flg==1){
	        cout<<"No\n";
	    }
	    else{
	        cout<<"Yes\n";
	    }
	    
	}
	
	return 0;
}