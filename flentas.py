from collections import Counter

def check_permutation(pattern, text):
    pattern_counter = Counter(pattern)
    text_length = len(text)
    pattern_length = len(pattern)
    
    for i in range(text_length - pattern_length + 1):
        substring = text[i:i+pattern_length]
        substring_counter = Counter(substring)
        
        if pattern_counter == substring_counter:
            return True
    
    return False

# Main function
def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for _ in range(t):
        pattern = input().strip()
        text = input().strip()
        
        # Check if any permutation of pattern exists in the text
        if check_permutation(pattern, text):
            print("YES")
        else:
            print("NO")

# Run the main function
if __name__ == "__main__":
    main()
