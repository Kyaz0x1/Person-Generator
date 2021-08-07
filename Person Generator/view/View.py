from colorama import Fore, Back

class View:

    @staticmethod
    def show_menu(title, *options):
        print(f'\t\t{Back.MAGENTA} {title} {Back.RESET}')
        for option in range(len(options)):
            print(f'\t{Fore.YELLOW}[{option + 1}] {options[option]}')
    
    @staticmethod
    def show_menu_coptions(title, **options):
        print(f'\t\t{Back.MAGENTA} {title} {Back.RESET}')
        for key, value in options.items():
            print(f'\t{Fore.YELLOW}[{key}] {value}')
