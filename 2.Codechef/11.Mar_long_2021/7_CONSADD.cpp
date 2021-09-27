#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--){
        int r,c,x,f;
        cin>>r;
        cin>>c;
        cin>>x;
        long long int arr1[r][c];
        long long int arr2[r][c];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cin>>arr1[i][j];
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0; j<c; j++){
                cin>>arr2[i][j];
            }
        }

        //main code logic
        if(r<x and c<x){
            f=0;
            for(int i=0; i<r; i++){
                for(int j=0; j<c; j++){
                    if(arr1[i][j]!=arr2[i][j]){
                        f=1;
                        break;
                    }
                }
                if(f==1) break;
            }
        }
        else if(c<x){
            //Only for row
            f = 0;
            for(int i=0; i<c; i++){
                    int j;
                for(j=0; j<r-x+1; j++){
                    if(arr1[j][i]!=arr2[j][i]){
                        long long dif = arr2[j][i]-arr1[j][i];
                        for(int k=j; k<j+x; k++){
                            arr1[k][i]+=dif;
                        }
                    }
                }
                if(j==r-x){
                    for(int k=r-x+1; k<r; k++){
                        if(arr1[k][i]!=arr2[k][i]){
                            f=1;
                            break;
                        }
                        if(f==1) break;
                    }
                }
                if(f==1) break;
            }
        }
        else if(r<x){
            //Only for col
            f = 0;
            for(int i=0; i<r; i++){
                    int j;
                for(j=0; j<c-x+1; j++){
                    if(arr1[i][j]!=arr2[i][j]){
                        long long dif = arr2[i][j]-arr1[i][j];
                        for(int k=j; k<j+x; k++){
                            arr1[i][k]+=dif;
                        }
                    }
                }
                if(j==c-x){
                    for(int k=c-x+1; k<c; k++){
                        if(arr1[i][k]!=arr2[i][k]){
                            f=1;
                            break;
                        }
                        if(f==1) break;
                    }
                }
                if(f==1) break;
            }
        }
        else if(r>=x and c>=x){
            //for row and col both
            //Only for row
            f = 0;
            for(int i=0; i<c; i++){
                for(int j=0; j<r-x+1; j++){
                    if(arr1[j][i]!=arr2[j][i]){
                        long long dif = arr2[j][i]-arr1[j][i];
                        for(int k=j; k<j+x; k++){
                            arr1[k][i]+=dif;
                        }
                    }
                }
                /*if(j==r-x){
                    for(int k=r-x+1; k<r; k++){
                        if(arr1[k][i]!=arr2[k][i]){
                            f=1;
                            break;
                        }
                        if(f==1) break;
                    }
                }
                if(f==1) break;*/
            }


            //Only for col
            //int f = 0;
            for(int i=0; i<r; i++){
                for(int j=0; j<c-x+1; j++){
                    if(arr1[i][j]!=arr2[i][j]){
                        long long dif = arr2[i][j]-arr1[i][j];
                        for(int k=j; k<j+x; k++){
                            arr1[i][k]+=dif;
                        }
                    }
                }
                /*if(j==c-x){
                    for(int k=c-x+1; k<c; k++){
                        if(arr1[i][k]!=arr2[i][k]){
                            f=1;
                            break;
                        }
                        if(f==1) break;
                    }
                }
                if(f==1) break; */
            }

            //checking if both matrix are equal python gives TLE
            //int f=0;
            for(int i=0; i<r; i++){
                for(int j=0; j<c; j++){
                    if(arr1[i][j]!=arr2[i][j]){
                        f=1;
                        break;
                    }
                }
                if(f==1) break;
            }
        }

        if(f==1){
            cout<<"No"<<"\n";
        }
        else{
            cout<<"Yes"<<"\n";
        }

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cout<<arr1[i][j];
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0; j<c; j++){
                cout<<arr2[i][j];
            }
        }



        //end of code
    }
    return 0;
}
