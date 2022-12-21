#include "sshell.h"

/**
  * _strlen - returns string length
  * @s: input string
  *
  * Return: string length
  */

int _strlen(char *s)
{
	int len = 0;

	while (s[len])
		len++;

	return (len);
}
