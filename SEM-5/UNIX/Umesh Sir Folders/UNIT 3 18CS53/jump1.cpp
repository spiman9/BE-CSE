#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<iostream>
using namespace std;

#include <setjmp.h>
jmp_buf buf;
main() {
   int x = 1;
   setjmp(buf); //set the jump position using buf
  // printf("5"); // Prints a number
   x++;
   if (x <= 10)
	{
	    cout<<"BEFORE LONG JUMP\n";
	    longjmp(buf, 1); // Jump to the point located by setjmp
	     cout<<"AFTER LONG JUMP";
	}
}


