"""
Author:     Calvin Henggeler
Date:       April 10, 2023
Course:     CS 399 Intermediate Python

Description:
            This python file is made to complete the Module 4 homework on the
            topic of metaprogramming
Disclaimers:
            None, No Artificial Intelligence tools used
Sources:
            Given starting code from assignment
"""

# =========================================================================== #
#                               Module Imports                                #
# =========================================================================== #


# =========================================================================== #
#                                   Classes                                   #
# =========================================================================== #
class DocMeta(type):

    @staticmethod
    def __new__(mcs, *args, **kwargs):
        """
        Ensures that all callable attributes have a __doc__ attribute.
        If an attribute is callable but does not have a __doc__ attribute,
        it should be given a default docstring of "No documentation available."
        :param args:
        :param kwargs:
        """
        #dynamically adding __doc__ to atrtributes that dont have it.
        modified_attr =

        pass


class MyClass(DocMeta):

    class_var = "I am a class variable"

    def my_method(self):
        """
        A method that prints a method
        :return: None
        """
        print('I am a method')

    def my_undocumented_method(self):
        print('I am an undocumented method')


# =========================================================================== #
#                              Module Test Code                               #
# =========================================================================== #
"""
This code was provided in the assignment
"""
if __name__ == "__main__":
    my_obj = MyClass()
    print(MyClass.class_var)  # prints "I am a class variable."
    my_obj.my_method()  # prints "I am a method."
    my_obj.my_undocumented_method()  # prints "I am an undocumented method."

    print(help(my_obj.my_method))  # prints ".... A method that prints a message ...."
    print(MyClass.my_method.__doc__)  # prints "A method that prints a message."

    print(help(my_obj.my_undocumented_method))  # prints " .... No documentation available ...."
    print(MyClass.my_undocumented_method.__doc__)  # prints "No documentation available."