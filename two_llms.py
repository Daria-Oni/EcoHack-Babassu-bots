import requests
import json

# OpenRouter API details
api_key = "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"
base_url = "https://openrouter.ai/api/v1"
model="openchat/openchat-7b:free"
headers = {
    "Authorization": f"Bearer {api_key}",
}
def extract_species(text):
    """
    This function takes a string of text as input and uses the OpenRouter model
    to extract information on plants mentioned in the text.
    """
    prompt1 = f"""


    ROLE: You are a Data Extraction Specialist for Medicinal Species. You have expertise in extracting detailed information about medicinal plants and animals from documents and organising it into JSON format. Your goal is to ensure accurate and comprehensive data for use in scientific research and database integration.

    Respond to the following:

    USER: Objective: Efficiently extract detailed information about ALL medicinal species from a document and organize it into a structured JSON format.

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



    {text}

    """

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt1}],
        "temperature": 0.5
    }

    # Print the prompt to see what is being sent to the API
    print("Sending the following text to the API:")
    print(prompt1)

    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)

    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
def check_species(text, species):
    """
    This function checks if the output information is correct using a second llm.
    """
    prompt2 = f"""
    You are an editor cross-checking new entries for a database on traditional medicinal plants from the amazon rainforest.
    Your colleague has read a text and has gathered information on all mentioned traditional medicinal species. Please check if the information is correct and she has not made up any species or data.
    If there are wrong entries, correct the error and output the corrected json file. Finally, state the changes you made.
    This is the original text:
    {text}
    and this is your colleague's list:
    {species}
    """

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt2}],
        "temperature": 0.5
    }

    # Print the prompt to see what is being sent to the API
    print("Sending the following text to the API:")
    print(prompt2)

    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)

    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def main():
    # Hardcoded text for testing
    with open('test_set/txts/bradao13.txt', 'r') as file:
        test_text = file.read()
    try:
        result1 = extract_species(test_text)
        print("\nExtracted Data:\n", result1)
    except Exception as e:
        print(e)
    try:
        result2 = check_species(test_text,result1)
        print("\nExtracted Data:\n", result2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    # You are a researcher looking to build a database on traditional medicinal plants from the amazon rainforest.

    # You are interested in the following information for each species:
    # Species Name: Record both the scientific and any common names.
    # Medicinal Uses: Include descriptions of use, which illnesses can be treated, and the specific parts utilized.
    # Habitat: Note the geographical location or habitat, such as ecosystems, of each species.
    # Citations: List any publications or studies that reference the species.
    # Additional Data: Capture extra details such as preparation methods and dosages.

    # The text you receive could contain information about traditional medicinal plants, but it is also possible that there is no such information in the text.
    # Output information on species with a medicinal purpose in a structured json format. If there are none, output "no species with a medicinal purpose found."
    # The json categories are Species Name, Medicinal uses, Habitat, Citations, and Additional Data. If there is no information available for one of the
    # categories for a described plant, put "no information" in that field.