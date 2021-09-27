#include<bits/stdc++.h>
#define ll long long int
using namespace std;
void nn()
{
 ll n,x,y;
 cin>>n>>x;
 ll cost=x;
 int count=0;
 std::vector<ll> v(n),a(n),b(n);
 for(int i=0;i<n;i++)
 {
  cin>>v[i];
 }
 sort(v.begin(),v.end());
 int i=0;

 if(v[0]<x){
    for(int j=0;j<n;j++){
        if(v[j]<cost){
            y = y + 1;
        }
        else{
            break;
        }
    }

    if(y>0){
        for(int k=0;k<y;k++){
            a[k] = v[k];
        }
        for(int m=y;m<0;m++){
            b[m] = v[m];
        }
    }
 }
 
 while(i<n)
 {
  if(cost>=v[i])
  {
   cost = 2 * v[i];
   i++;
   count++;
  }
 /* else if(cost>v[i]/2)
  {
   v[i] = 2*(v[i] - cost);
   count++;
   cost = 2*cost;
  }*/
  else{
   cost = 2*cost;
   count++;
  }
 }

 count = count + b.size();
 
 cout<<count<<endl;

}
int main()
{
 ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;

    while(t--){

     nn();

    }

    return 0;
}