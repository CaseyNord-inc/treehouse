def test_var_args(f_arg, *args):
    print("First normal arg: ", f_arg)
    for arg in args:
        print("Another arg through *args: ", arg)


test_var_args("potato", "muffin", "road", "5", 22, (2, 3, 4), "banana", False, [7, 8, 9], {"key": "value"})
