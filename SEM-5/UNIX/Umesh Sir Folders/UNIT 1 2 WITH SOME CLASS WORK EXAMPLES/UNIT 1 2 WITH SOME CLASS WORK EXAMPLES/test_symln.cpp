			#include <iostream>
			using namespace std;
			#include <sys/types.h>

			#include <unistd.h>

			#include <string.h>



			/* Emulate the UNIX ln command */

			int main (int argc, char* argv[])

			{					

				char*	buf[256], tname[256];

				if ((argc< 3 && argc > 4) || (argc==4 && strcmp(argv[1],"-s"))) {

					cout << "usage: " << argv[0] << " [-s] <orig_file> <new_link>\n";

					return 1;

				}

				if (argc==4) 	

					return symlink( argv[2], argv[3]);		/* create a symbolic link */

				else

					return link(argv[1], argv[2]);		/* create a hard link */


				return 0;
			}
