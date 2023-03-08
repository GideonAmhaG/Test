#!/usr/bin/python3
""" module for entry point of the command interpreter """
import cmd
import shlex
import models
from models.base_model import BaseModel
from datetime import datetime


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

    def do_create(self, class_name):
        """ creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id """
        cls_name = self.parseline(class_name)[0]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in self.cls:
            print("** class doesn't exist **")
        else:
            new_obj = eval(cls_name)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, cls_and_id):
        """ prints the string representation of an instance based on the
        class name and id """
        cls_name = self.parseline(cls_and_id)[0]
        cls_id = self.parseline(cls_and_id)[1]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in self.cls:
            print("** class doesn't exist **")
        elif cls_id is None:
            print("** instance id missing **")
        else:
            key = cls_name + "." + cls_id
            obj = models.storage.all().get(key, "** no instance found **")
            print(obj)

    def do_destroy(self, cls_and_id):
        """ deletes an instance based on the class name and id """
        cls_name = self.parseline(cls_and_id)[0]
        cls_id = self.parseline(cls_and_id)[1]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in self.cls:
            print("** class doesn't exist **")
        elif cls_id is None:
            print("** instance id missing **")
        else:
            key = cls_name + "." + cls_id
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, class_name):
        """ prints all string representation of all instances based or not
        on the class name """
        cls_name = self.parseline(class_name)[0]
        objs = models.storage.all()
        if cls_name is None:
            for value in objs.values():
                print(str(value))
        elif cls_name in self.cls:
            keys = objs.keys()
            for key in keys:
                if key.startswith(cls_name):
                    print(str(objs[key]))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ updates an instance based on the class name and id by adding or
        updating attribute """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print("** class name missing **")
        elif args[0] not in self.cls:
            print("** class doesn't exist **")
        elif args_size == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif args_size == 2:
                print("** attribute name missing **")
            elif args_size == 3:
                print("** value missing **")
            else:
                if args[3].isdigit():
                    args[3] = int(args[3])
                elif args[3].replace(".", "", 1).isdigit():
                    args[3] = float(args[3])
                setattr(obj, args[2], args[3])
                setattr(obj, "updated_at", datetime.now())
                models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
