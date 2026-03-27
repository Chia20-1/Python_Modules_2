#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp: int = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)


def ft_first_exception() -> None:
    print("=== Garden Exception ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
