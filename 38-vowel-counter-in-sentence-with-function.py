"""
Task 38: Vowel Counter in a Sentence with Function
Repository: python-basics
"""

def count_vowels(sentence):
    """
    Counts the number of vowels in a given sentence.
    Returns: A dictionary with each vowel and its count.
    """
    vowels = "aeiouAEIOU"
    vowel_count = {}

    for char in sentence:
        if char in vowels:
            lower_char = char.lower()
            vowel_count[lower_char] = vowel_count.get(lower_char, 0) + 1

    return vowel_count


def main():
    print("=" * 40)
    print("   Vowel Counter in a Sentence")
    print("=" * 40)

    sentence = input("Enter a sentence: ")
    result = count_vowels(sentence)

    total = sum(result.values())
    print(f"\nTotal vowels found: {total}")
    print("Breakdown:")
    for vowel in "aeiou":
        count = result.get(vowel, 0)
        if count > 0:
            print(f"  '{vowel}' -> {count}")
if __name__ == "__main__":
    main()