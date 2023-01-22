#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<iostream>
using namespace std;

int main( int argc , char *argv[] , char *envp[] )
{
   extern char **environ;

   
   //USING THE ENVORNMENT LIST
   /*cout<<"\n USING THE ENVORNMENT LIST\n";
   for ( int i = 0 ; envp[i] != (char *) 0 ; i++ )
   {
   cout<<envp[i]<<"\n";

   }*/

   //USING THE ENVORNMENT POINTER

   cout<<" USING POINTER \n"; 
  /*   for( int i = 0 ; environ[i] != ( char * ) 0 ; i++ )
       {
		 cout<<environ[i]<<"\n";
       }
*/

//USING THE GETENV FUNCTION FOR A SPECIFIC ENVIRONMENT VARIABLE

   cout<<" \n USING getenv  \n";
   char *env = getenv("HOME");
     cout<<"HOME=" << env << "\n";

// PUTT AND SET ENVIRON
      putenv("UMK");
      setenv("UMK","klsgit",0);  
   cout<<" \n USING getenv  \n";
   char *env1 = getenv("UMK");
      cout<<"UMK=" << env1 << "\n";
   cout<<"BEFORE UNSET\n";
      cout<<"UMK=" << env1 << "\n";
   unsetenv("UMK");
   cout<<"AFTER UNSET\n";
   char *env2 = getenv("UMK");
 cout<<"UMK=\n" << env2 << "\n";





   return 0;
}
