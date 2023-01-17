#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "error.h"

int main(int argc, char *argv[])
{
    int      i;
    for (i = 0; i < argc+1; i++)      /* echo all command-line args */
        printf("argv[%d]: %s\n", i, argv[i]);
    exit(0);
}

