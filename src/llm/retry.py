import random
import time
from collections.abc import Callable
from typing import TypeVar

from groq import APIConnectionError, InternalServerError, RateLimitError

T = TypeVar("T")

RETRYABLE_ERRORS = (
    APIConnectionError,
    RateLimitError,
    InternalServerError,
)


def call_with_retry(request: Callable[[], T], max_attempts: int = 3) -> T:
    for attempt in range(max_attempts):
        try:
            return request()

        except RETRYABLE_ERRORS as error:
            is_last_attempt = attempt == max_attempts - 1

            if is_last_attempt:
                raise

            delay_seconds = (2 ** attempt) + random.random()

            print(
                f"{type(error).__name__}; retrying in "
                f"{delay_seconds:.1f} seconds..."
            )
            time.sleep(delay_seconds)

    raise RuntimeError("Unreachable")