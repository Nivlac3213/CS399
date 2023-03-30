"""
Author:     Calvin Henggeler
Date:       March 3, 2023
Course:     SUSlist_HW Intermediate Python

Description:
            This python file is made to complete Homework 3 on the topic of
            Decorators
Disclaimers:
            None, No Artificial Intelligence tools used
Sources:
            Given starting code from assignment
"""

# =========================================================================== #
#                               Module Imports                                #
# =========================================================================== #
from random import randint
from time import sleep, asctime


# =========================================================================== #
#                                  Decorators                                 #
# =========================================================================== #
def backoff(initial_delay: float = 0.1, backoff_factor: float = 2, max_delay: int = 3):
    def original_backoff(func: callable) -> callable:

        delay = 0
        attempts = 0

        def inner(*args, **kwargs):

            nonlocal delay, attempts

            # Call the function after current delay time
            print(f'{asctime()} Calling {func.__name__} after {delay} s delay')
            sleep(delay)
            result = func(*args, **kwargs)

            # if the function returns false -> back off
            if not result:
                delay = initial_delay * backoff_factor ** attempts
                attempts += 1
            # if the call passes OR max_delay exceeded, reset backoff time
            elif result or delay > max_delay:
                delay = 0
                attempts = 0

            return result

        return inner

    return original_backoff


# =========================================================================== #
#                                  Functions                                  #
# =========================================================================== #
@backoff(initial_delay=0.3, backoff_factor=2, max_delay=2.4)
def call_shaky_service():
    """
    Models an unstable remote service
    :return:  bool
    """
    return 6 == randint(1, 6)


# =========================================================================== #
#                              Execution/Test Code                            #
# =========================================================================== #
if __name__ == '__main__':

    while True:
        print(call_shaky_service())
