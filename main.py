import sys

def main():
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
        print(f"Hello, {name}!")
    else:
        print("Hello World!")

if __name__ == "__main__":
    main()