#!/bin/usr/python3
import cmd
import readline

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

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
if __name__ == '__main__':
    HBNBCommand().cmdloop()

