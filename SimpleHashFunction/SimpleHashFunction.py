def simple_hash(text):
    """Simple hash function that sums ASCII values of characters."""
    return sum(ord(char) for char in text)

# Example usage
if __name__ == "__main__":
    text = input("Enter text: ")
    hash_value = simple_hash(text)
    print(f"Hash value: {hash_value}")
