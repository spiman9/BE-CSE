	#include <iostream>
	using namespace std;
	#include <stdio.h>

	#include <sys/types.h>

	#include <sys/stat.h>

	#include <unistd.h>

	#include <fcntl.h>

	#include <stdlib.h>


	int main( int argc, char* argv[]) 	

	{

		if (argc !=4)

		{

			cout << "usage: " << argv[0] << " <file> <major no> <minor no>\n";

			return 0;

		}

		int major = atoi(argv[2]), minor = atoi(argv[3]);

		(void)mknod(argv[1],S_IFCHR|S_IRWXU|S_IRWXG|S_IRWXO, 

				(major <<8) | minor);

		int rc=1, fd = open(argv[1],O_RDWR|O_NONBLOCK|O_NOCTTY);

		char buf[256];

		while (rc && fd!=-1) 

			if ((rc=read(fd,buf,sizeof(buf))) < 0)

					perror("read");

			else if (rc)	 cout << buf << endl;

		close(fd);

		return 0;
	} 	/* main */
