#include "sshell.h"

/**
 * _env - prints environmental variables when env is typed
 * @s: first argument indicating typed "env"
 * @envp: env vector of strings
 */
void _env(char *s, char **envp)
{
	int i;

	if ((_strcmp(s, "env")) == 0)
	{
		for (i = 0; envp[i] != NULL; i++)
		{
			write(STDOUT_FILENO, envp[i], _strlen(envp[i]));
			write(STDOUT_FILENO, "\n", 1);
		}
	}

}
