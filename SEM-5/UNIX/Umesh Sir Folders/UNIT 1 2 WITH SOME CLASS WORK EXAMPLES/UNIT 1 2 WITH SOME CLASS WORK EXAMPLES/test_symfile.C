	#include "symfile.h"

	int main() 		

	{			// Example for symfile

	char	buf[256];	

	symfile nsym;

        nsym.setlink( "/usr/file/chap10", "/usr/xyz/sym.lnk" );

	nsym.open( ios::in );

	while (nsym.getline(buf,256))

		cout << buf << endl;		// read /usr/file/chap10

	cout << nsym.ref_path() << endl;			// echo "/usr/file/chap10"

	nsym.close();			// close the symbolic link file

	return 0;

	}
