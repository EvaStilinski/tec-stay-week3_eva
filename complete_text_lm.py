import random

# Sample text for language modeling
text = "Development of Genshin Impact began in 2017, and takes inspiration from a variety of sources, including The Legend of Zelda: Breath of the Wild, anime, Gnosticism, and an array of cultures and world mythologies. Genshin Impact has received generally positive reviews, with critics writing approving of its combat mechanics and its immersive open world. Conversely, some criticism has been directed at its simplistic endgame and its gacha-based monetization model. Across all platforms, the game is estimated to have grossed nearly $3.6 billion by September 2022, representing the highest ever first-year launch revenue for any video game."

# Introduction to the code
print("This code generates text completion based on a language model built from a sample text.\nThe sample text is a Wikipedia article about the video game Genshin Impact. \nThe language model is built using N-grams, and the text completion is generated using the language model.")

# N-gram size
n = int(input("Enter the N-gram size: "))

# Include data from user input
print("Want to add more data text? y/n")
answer = input()
if answer == 'y':
    text += input("Enter some text to include in the language model: ")
elif answer == 'n':
    print("Proceeding with the provided text.")


# Create N-grams from the sample text and locate the posible words that can follow a given prefix
def create_ngrams(text, n):
    ngrams = []
    words = text.split()
    for i in range(len(words) - n + 1):
        ngrams.append(words[i:i + n])
    return ngrams

# Build the language model based on the N-grams
def build_language_model(text, n):
    ngrams = create_ngrams(text, n)
    model = {}
    for ngram in ngrams:
        prefix = ' '.join(ngram[:-1])
        suffix = ngram[-1]
        if prefix in model:
            model[prefix].append(suffix)
        else:
            model[prefix] = [suffix]
    return model

# Generate text completion from the language model
def complete_text(model, input_text, n, max_length=50):
    input_words = input_text.split()
    if len(input_words) < n - 1:
        return "Input text is too short for completion."

    prefix = ' '.join(input_words[-n+1:])
    completion = input_text
    while len(completion.split()) < max_length:
        if prefix not in model:
            break
        next_word = random.choice(model[prefix])
        completion += " " + next_word
        prefix = ' '.join(completion.split()[-n+1:])
    return completion

if __name__ == "__main__":
    # User-provided partial text 
    partial_text = "Genshin Impact began in"

    # Build the language model 
    language_model = build_language_model(text, n)

    # Complete the partial text
    completed_text = complete_text(language_model, partial_text, n, max_length=20)

    print("Partial Text:")
    print(partial_text)
    print("\nCompleted Text:")
    print(completed_text)
