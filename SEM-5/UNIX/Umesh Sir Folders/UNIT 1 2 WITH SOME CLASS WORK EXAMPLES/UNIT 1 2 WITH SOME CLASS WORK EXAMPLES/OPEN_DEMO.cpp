#include <iostream>
using namespace std;
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/stat.h>

int main()
{
    // assume that foo.txt is already created
    int fd1 = open("t1.txt", O_RDONLY, 0);
    close(fd1);
     
    // assume that baz.tzt is already created
    int fd2 = open("t1.txt", O_RDONLY, 0);
     
    printf("fd2 = % d\n", fd2);


    char c;
     fd1 = open("t1.txt", O_RDONLY, 0);
     fd2 = open("t1.txt", O_RDONLY, 0);
  read(fd1, &c, 1);
  read(fd2, &c, 1);
 printf("c = %c\n", c);



    exit(0);
}
