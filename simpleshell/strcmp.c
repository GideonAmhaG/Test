#include "sshell.h"

/**
 * _strcmp - compares 2 strings
 * @s1: 1st string
 * @s2: 2nd string
 *
 * Return: difference between the 2 strings
 */

int _strcmp(char *s1, char *s2)
{
	while (*s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
	}

	return (*s1 - *s2);
}
