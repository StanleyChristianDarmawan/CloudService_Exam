import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--bye":
            name = ' '.join(sys.argv[2:]) if len(sys.argv) > 2 else 'You'
            print(f"Good Bye, {name}!")
        else:
            name = ' '.join(sys.argv[1:])
            print(f"Hello, {name}!")
    else:
        print("Hello World!")

if __name__ == "__main__":
    main()