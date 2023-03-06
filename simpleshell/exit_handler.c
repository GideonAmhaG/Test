#include "sshell.h"

/**
 * _ext - exits when exit is typed
 * @s: first argument of the argument vector (typed "exit")
 */
void _ext(char *s)
{
	if ((_strcmp(s, "exit\n")) == 0)
	{
		free(s);
		exit(0);
	}
}
