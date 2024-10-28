#include "iostream"
#include "string"
#include "fstream"
using namespace std;
// function name hdou with 3 variables (2 variables:int,1 string variable)
void hdou(int p,int o,string jo)
{
	cout<<"    ========= BURP  FORCE ==========      ";
	cout<<"\nFIRST NUMBER: ";
	cin>>p;
	cout<<"SECOND NUMBERS: ";
	cin>>o;
	printf("do you creat file yes/no :");
	cin>>jo;
if(jo=="yes" or jo== "y"){
	string in;
	   if(p<o){
	   	ofstream iu("brupforce.txt");
	   	cout<<"name file : brupforce.txt";
	       for(int i=p;i<=o;i++){
	  	     iu<<i<<endl;
		}
		cout<<endl<<"thank you for creat "<<endl;
		
	    printf("\ndo delet file y/n :");
	    cin>>in;
	    	}
	   else if(p>o){
	   	cout<<"\nbhima "<<p<<">"<<o;
	  } 
	   else if(p==o){
	  	cout<<"\alhmar "<<p<<"="<<o;
	  } 
	   else{
	     cout<<"\nERROR ";
	  }
	if(in=="y"){
	    remove("brupforce.txt");
	
}

    else if(in=="n" or in == "no"){
    	printf("ok no delete file");
    	}
    else{
	cout<<"\n <<error<<"<<in;
}	
}
else if (jo=="no"){
    cout<<"\nno creat file";
}
else{
	cout<<"\n error<<<<<< "<<jo;
}
}
int main(){
  int p; char o;
  string jo;
  hdou(p,o,jo);
}

