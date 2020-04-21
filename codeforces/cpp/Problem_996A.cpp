#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    std::vector<int> v = {100,20,10,5,1};
    int amt,ret=0;
    cin>>amt;
    for(auto i = v.begin(); i!=v.end(); ++i){
        ret+= amt/(*i);
        amt%=(*i);
    }
    cout<<ret;
}
