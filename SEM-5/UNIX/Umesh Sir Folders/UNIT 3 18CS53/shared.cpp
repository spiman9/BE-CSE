#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<iostream>
using namespace std;

int main( int argc , char *argv[] , char *envp[] )
{
extern char **environ;
//USING THE ENVORNMENT LIST
cout<<"\n USING THE ENVORNMENT LIST\n";
for ( int i = 0 ; envp[i] != (char *) 0 ; i++ )
{
cout<<envp[i]<<"\n";

}

//USING THE ENVORNMENT POINTER

cout<<" USING POINTER \n";
     for( int i = 0 ; environ[i] != ( char * ) 0 ; i++ )
       {
		 cout<<environ[i]<<"\n";
       }


//USING THE GETENV FUNCTION FOR A SPECIFIC ENVIRONMENT VARIABLE

cout<<" \n USING getenv  \n";
char *env = getenv("HOME");
     cout<<"HOME=" << env << "\n";







return 0;
}
