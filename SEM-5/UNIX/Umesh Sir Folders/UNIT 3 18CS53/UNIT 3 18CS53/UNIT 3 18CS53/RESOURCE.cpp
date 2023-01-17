#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<iostream>
using namespace std;


#if defined(BSD) || defined(MACOS)
#include <sys/time.h>

#define FMT "%10lld "
#else
#define FMT "%10ld "
#endif

#include <sys/resource.h>
#define doit(name) pr_limits(#name, name)
#define doit_change(name) pr_limits_change(#name, name)

static void pr_limits_change(char *, int );
static void pr_limits(char *, int);

int main(void)
{
printf("RESOURCE_NAME SOFT_LIMIT   HARD_LIMIT\n\n");
#ifdef RLIMIT_AS
doit(RLIMIT_AS);
#endif
doit(RLIMIT_CORE);
doit(RLIMIT_CPU);
doit(RLIMIT_DATA);
doit(RLIMIT_FSIZE);
#ifdef RLIMIT_LOCKS
doit(RLIMIT_LOCKS);
#endif
#ifdef RLIMIT_MEMLOCK
doit(RLIMIT_MEMLOCK);
#endif
doit(RLIMIT_NOFILE);
#ifdef RLIMIT_NPROC
doit(RLIMIT_NPROC);
#endif

#ifdef RLIMIT_RSS
doit(RLIMIT_RSS);
#endif

#ifdef RLIMIT_SBSIZE 
doit(RLIMIT_SBSIZE);
#endif

#ifdef RLIMIT_STACK
doit_change(RLIMIT_STACK);
#endif

#ifdef RLIMIT_VMEM
doit_change(RLIMIT_VMEM);
#endif

exit(0);
}
static void pr_limits(char *name, int resource)
{
struct rlimit limit;
if (getrlimit(resource, &limit) < 0)
printf("getrlimit error for %s", name);

//DISPLAY RESOURCE NAME 

printf("%-14s ", name);

//DISPLAY RESOURCES SOFT LIMIT 
if (limit.rlim_cur == RLIM_INFINITY)
printf("(infinite) ");
else
printf(FMT, limit.rlim_cur);

//DISPLAY RESOURCES HARD LIMIT
if (limit.rlim_max == RLIM_INFINITY)
printf("(infinite)");
else
printf(FMT, limit.rlim_max);
putchar((int)'\n');
}

static void pr_limits_change(char *name, int resource)
{
struct rlimit limit;
if (getrlimit(resource, &limit) < 0)
printf("getrlimit error for %s", name);

//DISPLAY RESOURCE NAME 

printf("%-14s ", name);

//DISPLAY RESOURCES SOFT LIMIT 
//if (limit.rlim_cur == RLIM_INFINITY)
// printf("(infinite) ");
//else

printf("\n\nBEFORE RESOURCE CHANGE \n");
printf(FMT, limit.rlim_cur);
printf(FMT, limit.rlim_max);

// NOW CHANGE THE LIMIT
limit.rlim_cur=99;
limit.rlim_max=99999;

printf("\n\nAFTER RESOURCE CHANGE \n");
printf("%-14s ", name);
printf(FMT, limit.rlim_cur);
printf(FMT, limit.rlim_max);
printf("\n\n ");

}
