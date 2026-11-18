import string

# 1. Clean the text by removing punctuation and converting to lowercase
def clean_text(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower()

# 2. Analyze text statistics and word frequencies
def analyze_text(text):
    if not text.strip():
        print("Error: No text provided for analysis.")
        return

    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    
    cleaned = clean_text(text)
    words = cleaned.split()
    total_words = len(words)
    
    # Count frequency of each word using a dictionary
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
        
    # Sort words by frequency from highest to lowest
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Display the final report
    print("\n=== Text Analysis Report ===")
    print(f"Total Characters (with spaces): {char_count_with_spaces}")
    print(f"Total Characters (no spaces)  : {char_count_no_spaces}")
    print(f"Total Words                   : {total_words}")
    print(f"Unique Words                  : {len(word_freq)}")
    print("\n--- Word Frequencies ---")
    for word, count in sorted_words:
        print(f"- {word}: {count}")
    print("=" * 28)

# Main Application Execution Loop
if __name__ == "__main__":
    print("=== Welcome to Python Text Analyzer ===")
    while True:
        user_text = input("\nEnter a paragraph to analyze (or type 'exit' to quit):\n> ")
        
        if user_text.lower() == 'exit':
            print("Goodbye!")
            break
            
        analyze_text(user_text)
