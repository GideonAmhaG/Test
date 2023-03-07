#!/usr/bin/python3
""" module for entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """
    prompt = "(hbnb) "
    cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """ quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ Ctrl-D command to exit the program"""
        print()
        return True

    def emptyline(self):
        """ an empty line + ENTER will not execute anything """
        pass

    def do_create(self, line):
        """ creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id """
        command = self.parseline(line)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.cls:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
