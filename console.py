import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True  # Returning True will exit the command loop

    def do_EOF(self, arg):
        pass

    def help_EOF(self):
        print("EOF command to exit the program")

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()