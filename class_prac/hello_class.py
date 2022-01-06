class my_class:
    a = 1
    b = 2
    def print_member(self):
        print("abc")
    def set_value(self, a, b):
        self.a = a
        self.b = b
clazz = my_class()
clazz.print_member()