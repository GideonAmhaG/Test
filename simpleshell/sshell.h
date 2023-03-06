#ifndef SSHELL_H
#define SSHELL_H
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/*
 * File : sshell.h
 * Functions
 */

void _ext(char *s);
void _env(char *s, char **envp);
int _strcmp(char *s1, char *s2);
int _strlen(char *s);

#endif /* #ifndef SSHELL_H */
