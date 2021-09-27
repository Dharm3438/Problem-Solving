if(c<x)
    {
        for(int i=0;i<c;i++)
        {
            for(int j=0;j<r-x+1;j++)
            {
                if(arr1[j][i]!=arr2[j][i])
                {
                    ll diff=arr2[j][i]-arr1[j][i];
                    for(int k=j;k<j+x;k++)
                    {
                        arr1[k][i]+=diff;
                    }
                }
                if(j==r-x)
                {
                    for(int k=r-x+1;k<r;k++)
                    {
                        if(arr1[k][i]!=arr2[k][i])
                        {
                            return false;
                        }
                    }

                }

            }


        }
        return true;
    }