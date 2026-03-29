#!/usr/bin/env python3

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 123
    else:
        print("Operation completed successfully!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operations = [0, 1, 2, 3, 4]
    for i in operations:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print("Caught ValueError:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except TypeError as e:
            print("Caught TypeError:", e)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
