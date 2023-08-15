import requests

key = "<OpenAI API Key>"
context = text = "The following is a conversation with Dr. Plants. Dr. Plants knows everything in botany and hence, the Chatbot should NOT ask the human to consult another botanist. The chatbot should act like a professional botanist and ask the human many questions regarding the problem with the plant/tree and prescribe medicines and safety measures to treat the plant or maintain the plant with good health. It should introduce itself at the beginning of the conversation and enquire the human about the problem with the plant.\nThe chatbot also has an assistant, which is a computer vision based model which predicts the type of leaf and its disease with the help of a picture already uploaded by the human, without the notice of the chatbot. The chatbot may use the result of this model to generate prescriptions for the plant/tree.\nThe assistant predicted that the plant/tree and its disease are 'Apple - Cedar Apple Rust'. \n\nAI: "

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + key
}


def botanist(text, context):
    json_data = {
        'model': 'text-davinci-003',
        'prompt': context + text,
        'temperature': 0.9,
        'max_tokens': 1000,
        'stop': ["Human: ", "AI: "],
    }
    response = requests.post('https://api.openai.com/v1/completions', auth=(
        '', key), json=json_data, headers=headers)
    response = response.json()
    return response['choices'][0]['text']


while text != "bye":
    reply = botanist(text, context)
    context = context + reply
    print("\nDr. Plants: " + reply)
    text = input("\nYou: ")
    context = context + "\nHuman: " + text + "\nAI: "

print("\n\n")
print(context)
