# import openai
# from openai import OpenAI

# client = OpenAI(api_key="")  #  Put your API key here 

# def ask_chatgpt(prompt):
#     print("Asking ChatGPT...")
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # or "gpt-4" if you have access
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error: {e}"

# # Test mode
# if __name__ == "__main__":
#     while True:
#         question = input("You: ")
#         if question.lower() in ["exit", "quit"]:
#             break
#         print("JARVIS:", ask_chatgpt(question))
