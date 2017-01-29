class InputParser():
    @classmethod
    def take_args(cls, user_input):
        args = user_input.split(' ')
        func_args = []
        if "show movie projection" in user_input:
            func_args.append(args[0] + ' ' + args[1] + ' ' + args[2])
            start_point = 3
        else:
            func_args.append(args[0] + ' ' + args[1])
            start_point = 2

        for indx in range(start_point, len(args)):
            func_args.append(args[indx])

        return func_args

    @classmethod
    def call_function(cls, func_args, fucn_dict):
        if type(func_args) is list:
            if func_args[0] in fucn_dict.keys():
                fucn_dict[func_args[0]](func_args[1:])
            else:
                print("Wrong input!")
        else:
            if func_args in fucn_dict.keys():
                fucn_dict[func_args]()
            else:
                print("Wrong input!")
