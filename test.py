# Simple Python program to print a message

def main():
    try:
        # Define the message
        message = "Hello, World! v2"
        
        # Print the message to the console
        print(message)
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
