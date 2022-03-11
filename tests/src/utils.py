import time
from typing import Callable, TypeVar


RV = TypeVar('RV')
G = Callable[[], RV]


def wait_for(generator: G, validator=lambda obj: obj, delay: float = 0.1, timeout: float = 5.0) -> RV:
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError(timeout)
        result = generator()
        if validator(result):
            return result
        else:
            time.sleep(delay)
            continue
