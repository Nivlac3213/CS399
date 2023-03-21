from random import randint
from time import sleep, asctime


def parameters(i, b, m):
    def backoff(func: callable) -> callable:
        delay = 0
        inital_delay = i
        back_off_factor = b
        max_delay = m

        def inner():
            t = asctime()
            tf = func()
            previous_delay = 0
            delay_amount = delay + back_off_factor * previous_delay
            print(f"{t}: will be calling call_shaky_service after {delay} sec delay")
            print(tf)
            sleep(delay_amount)

            while tf == False:
                # Allow initial delay to be used on its own.
                if delay_amount == 0:
                    t = asctime()
                    delay_amount = delay + inital_delay
                    previous_delay = delay_amount
                    tf = func()
                    print(f"{t}: will be calling call_shaky_service after {delay_amount} sec delay")
                    print(tf)
                    sleep(delay_amount)
                # Continue running through with back off factor.
                delay_amount = delay + back_off_factor * previous_delay
                previous_delay = delay_amount
                # Make sure max delay is not exceeded
                if delay_amount > max_delay:
                    delay_amount = max_delay
                tf = func()
                t = asctime()
                print(f"{t}: will be calling call_shaky_service after {delay_amount} sec delay")
                print(tf)
                sleep(delay_amount)
        return inner            # I am having a problem that inner prints "None" when tf == True. I do not understand why.
    return backoff


@parameters(0.1, 1.5, 2.5)
def call_shaky_service():
    return 6 == randint(1, 6)


while True:
    print(call_shaky_service())
