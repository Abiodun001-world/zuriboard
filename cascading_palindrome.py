import re

class CascadingPalindrome:
    
    def __init__(self, input_string):
        # Validate input_string
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def find_palindrome(self):
        # Split the input into components separated by space
        components = self.input_string.split()

        # Initialize variables to track the longest palindrome
        longest_palindrome = ""

        for component in components:
            if not isinstance(component, str):
                raise ValueError("Input components must be strings")

            if self.is_palindrome(component) and len(component) > len(longest_palindrome):
                longest_palindrome = component

        return longest_palindrome

    @staticmethod
    def is_palindrome(word):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
        return cleaned_word == cleaned_word[::-1]

