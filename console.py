#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models import storage
class HBNBCommand(cmd.Cmd):
    cmd.Cmd.prompt = '(hbnb) '
    def do_User(self, args):
        """Handles all User commands"""
        show = args[:5]
        destroy = args[:8]
        update = args[:7]
        if args == '.all()':
            self.do_all("User")
        elif args == '.count()':
            self.count('User')
        elif show == '.show':
            show_instance = "User " + args[5:]
            self.do_show(show_instance)
        elif destroy == '.destroy':
            destroy_instance = "User " + args[8:]
            self.do_destroy(destroy_instance)
        elif update == '.update':
            turn_totuple = (tuple)(args[7:])
            print(turn_totuple)
            dict_checker = self.dictionary_checker(turn_totuple[1])
            print(turn_totuple[0])
            if dict_checker == 0:
                word_nobrackets = self.bracket_remover(args[7:])
                update_instance = "User " + word_nobrackets
                self.do_update(update_instance)
            else:
                update_with_dict("User", dict_checker, turn_totuple(0))
    def bracket_remover(self, arg):
        word = ""
        for letter in arg:
            if letter != "(" and letter != ")" and letter != ",":
                word += letter
        return (word)
    def dictionary_checker(self, args):
        try:
            dictionary = (dict)(args)
            return (dictionary)
        except Exception as e:
            return (0)
    def do_BaseModel(self, args):
        """Handles all BaseModel commands"""
        print(self.check_args(args))
        if args == '.all()':
            self.do_all("BaseModel")
        elif args == '.count()':
            self.count('BaseModel')
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
                new = BaseModel()
                new.save()
                print(new.id)
            elif arg == 'User':
                new = User()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    def check_args(self, arg):
        """
            a function to tokenize the arguments
        """
        first = ""
        status = 0
        args = []
        for i in arg:
            if i == '"':
                status += 1
                continue
            if i == " ":
                if status == 1:
                    first += i
                elif status == 2:
                    args.append(first)
                    first = ""
                else:
                    args.append(first)
                    first = ""
            else:
                if i == '"':
                    args.append(first)
                    first = ""
                else:
                    first += i
        args.append(first)
        return (args)
    def do_show(self, arg=None):
        """
            Prints the string representation of an instance
        """
        status = 0
        instance_present = 0
        if arg == None:
            print("** class name missing **")
            return(0)
        else:
            arguments = self.check_args(arg)
            classnames = []
            instances = storage.all()
            for key in instances.keys():
                word = ""
                for letter in key:
                    if letter == ".":
                        classnames.append(word)
                        break
                    else:
                        word += letter
            for name in classnames:
                if name == arguments[0]:
                    status = 1
            if status == 0:
                print("** class doesn't exist **")
            else:
                if len(arguments) >= 2:
                    classname = arguments[0] + "." + arguments[1]
                    for classandid in instances.keys():
                        if classname == classandid:
                            instance_present = 1
                            print(instances.get(classname).__str__())
                    if instance_present == 0:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
    def count(self, args):
        """
            Prints number of instances
        """
        instances = storage.all()
        instances_array = []
        status = 0
        if args:
            arguments = self.check_args(args)
            instances = storage.all()
            for key in instances.keys():
                word = ""
                for letter in key:
                    if letter == ".":
                        if word == arguments[0]:
                            status = 1
                            instances_array.append(instances.get(key).__str__())
                        break
                    else:
                        word += letter
            if status == 0:
                print("** class doesn't exist **")
            else:
                print(len(instances_array))
        else:
            for value in instances.values():
                instances_array.append(value.__str__())
            print(len(instances_array))

    def do_destroy(self, arg=None):
        """
            Deletes an instance based on the class name and id
        """
        status = 0
        instance_present = 0
        if arg == None:
            print("** class name missing **")
            return(0)
        else:
            arguments = self.check_args(arg)
            classnames = []
            instances = storage.all()
            for key in instances.keys():
                word = ""
                for letter in key:
                    if letter == ".":
                        classnames.append(word)
                        break
                    else:
                        word += letter
            for name in classnames:
                if name == arguments[0]:
                    status = 1
            if status == 0:
                print("** class doesn't exist **")
            else:
                if len(arguments) >= 2:
                    classname = arguments[0] + "." + arguments[1]
                    for classandid in instances.keys():
                        if classname == classandid:
                            instance_present = 1
                            instances.pop(classname)
                            storage.save()
                            break
                    if instance_present == 0:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")

    def do_all(self, args):
        """
            Prints all string representation of all instances
        """
        instances = storage.all()
        instances_array = []
        status = 0
        if args:
            arguments = self.check_args(args)
            instances = storage.all()
            for key in instances.keys():
                word = ""
                for letter in key:
                    if letter == ".":
                        if word == arguments[0]:
                            status = 1
                            instances_array.append(instances.get(key).__str__())
                        break
                    else:
                        word += letter
            if status == 0:
                print("** class doesn't exist **")
            else:
                print(instances_array)
        else:
            for value in instances.values():
                instances_array.append(value.__str__())
            print(instances_array)
    def do_update(self, arg):
        """
            Updates an instance based on the class name and id
        """
        status = 0
        instance_present = 0
        if arg == None:
            print("** class name missing **")
            return(0)
        else:
            arguments = self.check_args(arg)
            classnames = []
            instances = storage.all()
            for key in instances.keys():
                word = ""
                for letter in key:
                    if letter == ".":
                        classnames.append(word)
                        break
                    else:
                        word += letter
            for name in classnames:
                if name == arguments[0]:
                    status = 1
            if status == 0:
                print("** class doesn't exist **")
            else:
                if len(arguments) >= 2:
                    classname = arguments[0] + "." + arguments[1]
                    for classandid in instances.keys():
                        if classname == classandid:
                            if len(arguments) == 2:
                                print("** attribute name missing **")
                                return
                            else:
                                if len(arguments) ==3:
                                    print("** value missing **")
                                    return
                                else:
                                    instance_present = 1
                                    instance_dict = instances.get(classname).to_dict()
                                    if instance_dict.get(arguments[2]):
                                        typeof = type(instance_dict.get(arguments[2]))
                                        instance_dict.update({arguments[2]:(typeof)(arguments[3])})
                                        obj = BaseModel(**instance_dict)
                                    else:
                                        instance_dict.update({arguments[2]:arguments[3]})
                                        obj = BaseModel(**instance_dict)
                                    storage.new(obj)
                                    storage.save()
                                    break
                    if instance_present == 0:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")  
    def update_with_dict(classname, dictionary, instance_id=None):
        """
            Updates an instance based on the class name and id
        """
        status = 0
        instance_present = 0
        if id == None:
            print("** instance id missing **")
            return(0)
        else:
            classnames = []
            instances = storage.all()
            for key in instances.keys():
                word = ""
                for letter in key:
                    if letter == ".":
                        classnames.append(word)
                        break
                    else:
                        word += letter
            for name in classnames:
                if name == classname:
                    status = 1
            if status == 0:
                print("** class doesn't exist **")
            else:
                classname = classname + "." + instance_id
                for classandid in instances.keys():
                    if classname == classandid:
                        instance_present = 1
                        instance_dict = instances.get(classname).to_dict()
                        instance_dict.update(dictionary)
                        obj = BaseModel(**instance_dict)
                        storage.new(obj)
                        storage.save()
                        break
                if instance_present == 0:
                    print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
