import requests
import json

# OpenRouter API details
api_key = "key"
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
    ROLE: You are a Data Extraction Specialist for Medicinal Species of South America. You have expertise in extracting detailed information about medicinal plants and animals from documents and organising it into JSON format. Your goal is to ensure accurate and comprehensive data for use in scientific research and database integration.

    Respond to the following:

    USER: Objective: Extract information about ALL medicinal species from a document and organize it into a structured JSON format. All text should be returned in English.

    Data to Extract (ALWAYS maintain consistent variable names in the JSON output):

    species_name: Record both the scientific and any common names.
    medicinal_uses: Include descriptions of uses and the specific parts utilized.
    location: Note the geographical location or habitat of each species.
    citations: List any publications or studies that reference the species.
    habitat_details: Provide information about the type of ecosystem where the species is found.
    additional_data: Capture extra details such as preparation methods and dosages.

    Instructions:
    Keep entries consistent and comprehensive for database integration.
    Ensure each species entry in the document is converted into the JSON format.
    Focus on accurately transferring data without interpretation. Where specific details are unavailable, note "None" for that field.
    If no species data is present in the text, return an empty JSON array to indicate that no relevant information could be extracted.

    Text: \"\"\"
    {text}
    \"\"\"
    """

    data = {
        "model": "openchat/openchat-7b:free",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4
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
    # Filename is set here
    filename = "text.txt"
    try:
        with open(filename, 'r') as file:
            file_text = file.read()

        result = extract_information(file_text)
        print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
