#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test_cases = ["25", "abc"]
    for test in test_cases:
        print(f"Input data is '{test}'")
        try:
            temp: int = input_temperature(test)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print("Caught input_temperature error:", e)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
