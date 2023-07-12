#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    cmd.Cmd.prompt = '(hbnb) '
    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        exit()
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg: 
            if arg == 'BaseModel':
                newinst = BaseModel() 
                with open("file.json", 'w+') as fd:
                    print(json.dumps(newinst.to_dict()))
                print(newinst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
