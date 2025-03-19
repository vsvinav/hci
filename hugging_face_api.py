from transformers import pipeline


def get_hello_world():
    """
    Function to generate a creative "Hello World" message using Hugging Face's Transformers library.
    """
    generator = pipeline('text-generation', model='gpt2')
    result = generator("Hello, world!", num_return_sequences=1)
    return result[0]['generated_text']

if __name__ == "__main__":
    print("Generated 'Hello World' message:")
    print(get_hello_world())