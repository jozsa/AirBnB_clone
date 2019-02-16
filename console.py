#!/usr/bin/python3
import cmd
import readline
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = [
        'BaseModel',
        'User',
        'State',
        'Amenity',
        'Place',
        'Review'
    ]
    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """returns another empty line if an emptyline is passed in
            Otherwise it'd repeat the last command given
            """
        pass

    def do_create(self, arg):
        """ creates a new instance of BaseModel
            and saves to JSON file
            """
        if arg is None:
            print("** class name missing **")
            pass
        if arg == "BaseModel":
            new = BaseModel(arg)
            new.save()
            print(new)
        else:
            print("** class name doesn't exist **")

    def do_show(self, arg):
        if len(arg) < 1:
            print("** class name missing **")
            pass
        else:
            arg = arg.split(' ')
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                if len(arg) < 2:
                    print('** instance id missing **')
                    return
                key = arg[0] + '.' + arg[1]
                if key in FileStorage._FileStorage__objects:
                    print(FileStorage._FileStorage__objects[key])
                else:
                    print('** no instance found **')

    def do_destroy(self, arg):
        if len(arg) < 1:
            print("** class name missing **")
            pass
        else:
            arg = arg.split(' ')
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                if len(arg) < 2:
                    print('** instance id missing **')
                    return
                key = arg[0] + '.' + arg[1]
                if key in FileStorage._FileStorage__objects:
                    FileStorage._FileStorage__objects.pop(key)
                    models.storage.save()
                else:
                    print('** no instance found **')

    def do_all(self, arg):
        if len(arg) < 1:
            all_items = []
            for value in FileStorage._FileStorage__objects.values():
                all_items.append(str(value))
            print(all_items)
        else:
            arg = arg.split(' ')
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                all_items = []
                for value in FileStorage._FileStorage__objects.values():
                    if value.__class__.__name__ == arg[0]:
                        all_items.append(str(value))
                print(all_items)

    def do_update(self, arg):
         if len(arg) < 1:
            print("** class name missing **")
            pass
         else:
            arg = arg.split(' ')
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                if len(arg) < 2:
                    print('** instance id missing **')
                    return
                key = arg[0] + '.' + arg[1]
                if key in FileStorage._FileStorage__objects:
                    dict_to_update = FileStorage._FileStorage__objects[key].__dict__
                    if len(arg) < 3:
                        print('** attribute name missing **')
                    elif len(arg) < 4:
                        print('** value missing **')
                    else:
                        k = arg[2]
                        v = arg[3]
                        dict_to_update[k] = v
                else:
                    print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
