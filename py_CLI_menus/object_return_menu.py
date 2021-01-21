class ObjectReturnMenu:
# Prints to the terminal a menu of the __str__ of each in a list of objects and returns the object that the user chooses

    def __init__(self, object_list, menu_header = "Select one of the following options: "):
        
        self.object_list = object_list
        self.menu_header = menu_header
        
    def choose(self):

        choice_index = 0
        choice_made = False

        while not choice_made:

            print(f"{self.menu_header}\n")
            for choice in self.object_list:
                choice_index += 1
                print(f"{choice_index} - {choice}")

            option = input(f"Choose an option (1-{choice_index}) or Q to quit: ")

            if option.lower() == 'q':
                return None
            
            try:
                option_int = int(option)
                choice_made = True
            except:
                choice_index = 0
                continue
        
        return self.object_list[option_int - 1]
