import groq

# Initialize Groq API client
client = groq.Client(api_key="gsk_c8kH9pyHPexcVjbhg4KAWGdyb3FYz9FCVOrvOxfyajuNOrqy8kTBM")

# Function to get AI response from Groq API
def get_ai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content  # Corrected access
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
if __name__ == "__main__":
    print("Welcome to your AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! 👋")
            break
        response = get_ai_response(user_input)
        print("AI:", response)