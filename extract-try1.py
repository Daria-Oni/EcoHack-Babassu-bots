import requests
import json

# OpenRouter API details
api_key = "key"  # Replace with your actual API key
base_url = "https://openrouter.ai/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
}

def extract_information(text):
    """
    This function takes a string of text as input and uses the OpenRouter model
    to extract information, organizing it into a structured JSON format.
    """
    prompt = f"""
    Objective: Extract information about traditional medicinal species from the text in json format. Return only JSON format so we can add it to dababase without any notes from you
    Text to analyze:
    {text}
    """

    data = {
        "model": "openchat/openchat-7b:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    # Print the prompt to see what is being sent to the API
    print("Sending the following text to the API:")
    print(prompt)

    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)
    
    # Printing the full response
    print("\nFull Response:")
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def main():
    # Hardcoded text for testing
    test_text = "The Ginkgo biloba tree has been used traditionally to enhance memory."
    try:
        result = extract_information(test_text)
        print("\nExtracted Data:\n", result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()