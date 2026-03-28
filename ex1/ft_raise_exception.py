#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_cases = ["25", "abc", "100", "-50"]
    for test in test_cases:
        print(f"Input data is '{test}'")
        try:
            temp: int = input_temperature(test)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print("Caught input_temperature error:", e)
        print()


if __name__ == "__main__":
    test_temperature()
