"""
Author: Jordan Wallschlaeger
Date: 3/13/2023
Description: Completed version of the backoff decorator with the improved implementation. This creates a timer to
"backoff" so the system does not get overwhelmed, the time between calls grows exponentially. This also simulates a
service, in which, if it is true the timer gets reset. Copilot was used in assistance
"""

from random import randint
from time import sleep, asctime


def backoff(initial_delay: float = 0.01, backoff_factor: float = 2.0, max_delay: float = 2.5) -> callable:
    def decor(func: callable) -> callable:
        delay = initial_delay

        def inner(*args, **kwargs):
            nonlocal delay
            next_call_time = asctime()
            if delay is not None:
                next_call_time += f": will be calling {func.__name__} after {delay:.2f} sec delay"
            else:
                next_call_time += f": will be calling {func.__name__} after None sec delay"
            print(next_call_time)
            result = func(*args, **kwargs)
            while result in (False, None):
                delay *= backoff_factor
                if max_delay is not None:
                    delay = min(delay, max_delay)
                sleep(delay)
                next_call_time = asctime() + f": will be calling {func.__name__} after {delay:.2f} sec delay"
                print(next_call_time)
                result = func(*args, **kwargs)
            delay = initial_delay
            return result

        return inner

    return decor


@backoff(initial_delay=0.1, backoff_factor=1.5, max_delay=2.5)
def call_shaky_service():
    return 6 == randint(1, 6)


while True:
    print(call_shaky_service())
