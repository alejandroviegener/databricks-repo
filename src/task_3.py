# Dummy task
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some parameters.")
    parser.add_argument('--param1', type=str, help='The first parameter')
    parser.add_argument('--param2', type=str, help='The second parameter')

    args = parser.parse_args()

    # Now you can use args.param1 and args.param2 in your script
    print("Hello from task 3")
    print(f"Parameter 1: {args.param1}")
    print(f"Parameter 2: {args.param2}")

if __name__ == "__main__":
    main()