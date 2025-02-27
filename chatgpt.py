#step 1
from openai import OpenAI

def summarize_assistant(first_name, last_name, transactions):
    #step 2
    client = OpenAI(OPENAI_API_KEY="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")
    transString = ""
    for tran in transactions:
        transString += (f"(transaction: {tran[0]}, description: {tran[1]}, Date:{tran[2]}")
    chat_content = f"(first_name: {first_name}, last_name: {last_name}), [{transString}]"
    
    
    #step 3
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a chat Assistant for financial bank system. Please respond as a telephone assistant with transaction details."},
            {
                "role": "user",
                "content": chat_content
            }
        ]
    )


    print(completion.choices[0].message.content)
    return completion.choices[0].message.content