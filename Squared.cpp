//this code prints squares based on user's desired size 5 times
// The code will then sum the total of numbers entered 

#include <iostream>

using namespace std;

int main(int,char**) {
	int z=0;
	int c=0;
	double sum;
	while(z!=5){
	    int x;
	    cout << "Enter length between 0 and 64 (-1 to exit): ";
	    cin >> x;
	    int n=x;
	    if (x>=-1&&x<=64){
	    if (x==-1){
	            break;
	    }
	    if (x==0){
	        c+=1;
	        sum+=x;
	        continue;
	    }
	    if (x==1){
	        c+=1;
	        sum+=x;
	        cout << "+" << endl;
	    }
	    if(x>1&&x<64){
	        c+=1;
	        sum+=x;
	        for (n;n!=0;--n){
	            cout << "|";
	            int z =x;
	            for (z;z!=0;--z){
	                cout << " ";
	            }
	            cout << "|" << endl;
	        }
	    }
	    }
	   else {
	    cout << "Length must be between 0 and 64 inclusive, or enter -1 to exit." << endl;
	    }

	    }
	    cout << c << " squares printed and the sum was " << int(sum/c) << endl;
	}