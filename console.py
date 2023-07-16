#!/usr/bin/python3
"""Cmd program to create a console"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        the cmd class
    """
    cmd.Cmd.prompt = '(hbnb) '
    def default(self, line):
        tup = self.parseline(line)
        if tup[1].startswith(".all()"):
            self.do_all(tup[0])
        elif tup[1].startswith(".show("):
            if tup[1].endswith(")"):
                to_tuple = eval(tup[1][5:])
                if type(to_tuple) == str:
                    self.do_show(tup[0] + " " + to_tuple)
                else:
                    if len(to_tuple) > 0:
                        show_instance = tup[0] + " " + str(to_tuple[0])
                    else:
                        self.do_show(tup[0])
            else:
                super().default(line)
        else:
            super().default(line)

    def do_fBaseModel(self, args):
        """Handles all BaseModel commands"""
        show = args[:5]
        destroy = args[:8]
        update = args[:7]
        if args == '.all()':
            self.do_all("BaseModel")
        elif args == '.count()':
            self.count('BaseModel')
        elif show == '.show':
            to_tuple = eval(args[5:])
            if len(to_tuple) > 0:
                if type(to_tuple) == str:
                    show_instance = "BaseModel " + to_tuple
                else:
                    show_instance = "BaseModel " + str(to_tuple[0])
                self.do_show(show_instance)
            else:
                self.do_show('BaseModel')
        elif destroy == '.destroy':
            destroy_instance = "BaseModel " + args[8:]
            self.do_destroy(destroy_instance)
        elif update == '.update':
            turn_totuple = (tuple)(args[7:])
            print(turn_totuple)
            dict_checker = self.dictionary_checker(turn_totuple[1])
            print(turn_totuple[0])
            if dict_checker == 0:
                word_nobrackets = self.bracket_remover(args[7:])
                update_instance = "BaseModel " + word_nobrackets
                self.do_update(update_instance)
            else:
                update_with_dict("BaseModel", dict_checker, turn_totuple(0))

    def bracket_remover(self, arg):
        """
            function to remove brackets around string
        """
        word = ""
        for letter in arg:
            if letter != "(" and letter != ")" and letter != ",":
                word += letter
        return (word)

    def dictionary_checker(self, args):
        """function to extract dict from string"""
        try:
            dictionary = (dict)(args)
            return (dictionary)
        except Exception as e:
            return (0)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return (True)

    def emptyline(self):
        """handles no input in prompt"""
        pass

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return (True)

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel
        """
        if arg:
            if arg == 'BaseModel':
                new = BaseModel()
                new.save()
                print(new.id)
            elif arg == 'User':
                new = User()
                new.save()
                print(new.id)
            elif arg == 'Place':
                new = Place()
                new.save()
                print(new.id)
            elif arg == 'State':
                new = State()
                new.save()
                print(new.id)
            elif arg == 'City':
                new = City()
                new.save()
                print(new.id)
            elif arg == 'Amenity':
                new = Amenity()
                new.save()
                print(new.id)
            elif arg == 'Review':
                new = Review()
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
        if arg:
            pass
        else:
            arg = None
        if arg is None:
            print("** class name missing **")
            return (0)
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
        inst = []
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
                            inst.append(instances.get(key).__str__())
                        break
                    else:
                        word += letter
            if status == 0:
                print("** class doesn't exist **")
            else:
                print(len(inst))
        else:
            for value in instances.values():
                inst.append(value.__str__())
            print(len(inst))

    def do_destroy(self, arg=None):
        """
            Deletes an instance based on the class name and id
        """
        status = 0
        instance_present = 0
        if arg:
            pass
        else:
            arg = None
        if arg is None:
            print("** class name missing **")
            return (0)
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
        inst = []
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
                            inst.append(instances.get(key).__str__())
                        break
                    else:
                        word += letter
            if status == 0:
                print("** class doesn't exist **")
            else:
                if len(inst) > 0:
                    print(inst)
        else:
            for value in instances.values():
                inst.append(value.__str__())
            if len(inst) > 0:
                print(inst)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id
        """
        status = 0
        instance_present = 0
        if arg:
            pass
        else:
            arg = None
        if arg is None:
            print("** class name missing **")
            return (0)
        else:
            args = self.check_args(arg)
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
                if name == args[0]:
                    status = 1
            if status == 0:
                print("** class doesn't exist **")
            else:
                if len(args) >= 2:
                    classname = args[0] + "." + args[1]
                    for classandid in instances.keys():
                        if classname == classandid:
                            if len(args) == 2:
                                print("** attribute name missing **")
                                return
                            else:
                                if len(args) == 3:
                                    print("** value missing **")
                                    return
                                else:
                                    instance_present = 1
                                    d = instances.get(classname).to_dict()
                                    if d.get(args[2]):
                                        typeof = type(d.get(args[2]))
                                        d.update({args[2]: (typeof)(args[3])})
                                        obj = BaseModel(**d)
                                    else:
                                        d.update({args[2]: args[3]})
                                        obj = BaseModel(**d)
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
        if id is None:
            print("** instance id missing **")
            return (0)
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
