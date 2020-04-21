

    #include<bits/stdc++.h>
    using namespace std;
    const int N=4e5+5;
    int t,n,a[N];
    int main(){
    	cin>>t;
    	while(t--){
    		cin>>n;
    		int pos=0;
    		for(int i=1;i<=n;i++){
    			cin>>a[i];
    			if(a[i]%2==0)pos=i;
    		}
    		if(pos){
    			cout<<"1\n"<<pos<<endl;
    			continue;
    		}
    		if(n==1)puts("-1");
    		else cout<<"2\n1 2\n"; 
    	} 
        return 0;
    }
