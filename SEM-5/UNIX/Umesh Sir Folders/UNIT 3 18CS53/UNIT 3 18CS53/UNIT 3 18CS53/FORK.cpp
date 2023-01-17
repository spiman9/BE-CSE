#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<iostream>
using namespace std;

int	glob = 6;		
/* external variable in initialized data */
char	buf[ ] = "a write to stdout\n";
int main()
{
	int		var;		
/* automatic variable on the stack */
	pid_t	pid;
var = 88;
	if (write(STDOUT_FILENO, buf, sizeof(buf)-1) != sizeof(buf)-1)
		printf("write error");
	
        printf("before fork\n");
        printf("pid = %d, glob = %d, var = %d\n", getpid(), glob, var);	
	if ( (pid = fork()) < 0)
		printf("fork error");
	else if (pid == 0)
  	{	                  	/* child */
		glob++;	    /* modify variables */
		var++;
	   printf("INSIDE CHILD pid = %d, glob = %d, var = %d\n", getpid(), glob, var);
	}



	else
		sleep(5);			
    	/* parent */

	printf("pid = %d, glob = %d, var = %d\n", getpid(), glob, var);
	exit(0);
}

