	#include <iostream>
using namespace std;
	#include <stdio.h>
	#include <sys/types.h>
	#include <unistd.h>
	#include <fcntl.h>
	#include <string.h>
	#include <sys/stat.h>

	#if defined (BSD) && !_POSIX_SOURCE
		#include <sys/dir.h>
		typedef struct direct Dirent;
	#else
		#include <dirent.h>
		typedef struct dirent Dirent;
	#endif
	
	int main (int argc, char* argv[]) 		
	{
		Dirent*	dp;
		DIR*	dir_fdesc;
		while (--argc > 0) 		{	/* do the following for each file */
			if (!(dir_fdesc=opendir(*++argv))) 						
			{
				if (mkdir(*argv, S_IRWXU|S_IRWXG|S_IRWXO)==-1)
					perror("opendir"); 
				continue;
			}
			/* scan each directory file twice */
			int i = 0;
			for ( ; i < 1; i++) 
			{	cout<<"FNO. FILENAME\n";
				int cnt = 0;
				for (; dp=readdir(dir_fdesc); )
				{
				cout<<cnt+1<<".  "<<dp->d_name<<endl;
				//if (strcmp(dp->d_name,".") && strcmp(dp->d_name,".."))
				{ 
				cnt++;

				/* count how many files in directory*/
				}
				}
				cout<<"NO. OF FILES IN THE DIRECTORY"<<cnt<<endl;
				if (!cnt) { rmdir(*argv); break; }	/* empty directory */
				rewinddir(dir_fdesc);			/* reset file pointer for second round */
			}
			closedir(dir_fdesc);
		}	/* for each file */
		return 0;
	}	/* main */
