#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int i,b;
    cin>>i>>b;
    for(int a=i;a<=b;a++)
    {
    if(a<10)
    {
        if(a==1)
            cout<<"one";
        else if (a==2)
            cout<<"two";
        else if (a==3)
            cout<<"three";
        else if (a==4)
            cout<<"four";
        else if (a==5)
            cout<<"five";
        else if (a==6)
            cout<<"six";
        else if (a==7)
            cout<<"seven";
        else if (a==8)
            cout<<"eight";
        else if (a==9)
            cout<<"nine";
    }
    else
    {
        if(a%2==0)
            cout<<"even";
        else
            cout<<"odd";
    }
        cout<<"\n";
    }
    // Complete the code.
    return 0;
}

