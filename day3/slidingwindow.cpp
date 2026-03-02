//sliding window maximum subarray of size k using C++
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    vector <int> arr;
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
    int wsum=0;
    for (int i=0; i<k;i++){
        wsum+=arr[i];
    }
    int msum=wsum;
    for (int i=k;i<n;i++){
        wsum+=arr[i];
        wsum-=arr[i-k];
        msum=max(wsum,msum);

    }
    cout<<msum;
}




