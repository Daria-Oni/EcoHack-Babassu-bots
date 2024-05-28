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
    to extract information on plants mentioned in the text.
    """
    prompt1 = f"""
    Objective: Efficiently extract detailed information about ALL plant or animal species that can be used for medicinal purposes described in a document.

    Data to Extract: If there is a species with medicinal purpose described in the text, summarize any available information on the species such as:

    Species Name: Record both the scientific and any common names.
    Medicinal Uses: Include descriptions of use, which illnesses can be treated, and the specific parts utilized.
    Habitat: Note the geographical location or habitat, such as ecosystems, of each species.
    Citations: List any publications or studies that reference the species.
    Additional Data: Capture extra details such as preparation methods and dosages.

    Instructions:

    Focus on accurately transferring data without interpretation. Where specific details are unavailable, only include a summary of the available information.
    If no species with medicinal use is present in the text, return "no information about species with medicinal use" and no other output.

    These are examples of input and desired output:
    Input 1: "The plant with the scientific name Opus popus, commonly known as wallflower, grows in the Brasilian rainforest. It is most commonly found in secondary forests.
    It is reportedly used by the indigenous population to treat various illnesses such as indigestion or headaches (Albus et al., 2011). It can be consumed as a tea, but the dosage needs to be
    carefully chosen because an overdose can cause hallucinations. This is not the only plant that can be used to make tea. Other popular plants that can be used to make tea
    include strawberry leaves, peppermint, and cherries.

    Output 1: "Wall flowers (scientific name: Opus popus) are plants that are used by indigenous people to treat illnesses such as indigestion or headaches. The plant is
    found in secondary forests of the brasilian rainforest. It is consumed as a tea. The correct dosage is important to prevent side effects like hallucinations. Citation: Albus et al., 2011

    Input 2: " Lay down these words

    Before your mind like rocks.
    placed solid, by hands
    In choice of place, set
    Before the body of the mind
    in space and time:
    Solidity of baby, lint, or wall
    riprap of things:
    Cobble of milky way,
    straying planets,
    These poems, people,
    lost ponies with
    Dragging saddles —"

    Output 2: "no information about species with medicinal use"

    Input 3: "In the lush Amazon rainforest, the towering Brazil nut trees stand as guardians of the diverse ecosystem. Scarlet macaws, with their vibrant plumage, soar through the canopy, while howler monkeys leap from branch to branch, filling the air with their distinctive calls. On the forest floor, jaguars prowl stealthily, their rosetted coats blending into the dappled shadows. Nearby, colorful poison dart frogs hop among the leaf litter, their bright hues a warning to predators. The rainforest is also home to the elusive harpy eagle, whose powerful talons grasp the branches as it scans for prey. Beneath the water's surface, pink river dolphins navigate the winding tributaries, sharing the waters with schools of piranhas. This rich tapestry of plant and animal life highlights the incredible biodiversity of the Amazon, where every species plays a crucial role in maintaining the delicate balance of this unique environment."
    Output 3: "no information about species with medicinal use"

    Your input to analyze:
    {text}

    """

    data = {
        "model": "meta-llama/llama-3-8b-instruct:free",
        "messages": [{"role": "user", "content": prompt1}]
    }

    # Print the prompt to see what is being sent to the API
    print("Sending the following text to the API:")
    print(prompt1)

    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)

    # Printing the full response
    print("\nFull Response Part 1:")
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
def extract_json(text):
    """
    This function takes a string of text as input and uses the OpenRouter model
    to extract information, organizing it into a structured JSON format.
    """
    prompt2 = f"""
    Objective: Efficiently extract detailed information about ALL traditional medicinal species from a document and organize it into a structured JSON format.

    Data to Extract:

    Species Name: Record both the scientific and any common names.
    Medicinal Uses: Include descriptions of uses and the specific parts utilized.
    Location: Note the geographical location or habitat of each species.
    Citations: List any publications or studies that reference the species.
    Habitat Details: Provide information about the type of ecosystem where the species is found.
    Additional Data: Capture extra details such as preparation methods and dosages.

    Instructions:

    Ensure each species entry in the document is converted into the JSON format.
    Focus on accurately transferring data without interpretation. Where specific details are unavailable, note "None" for that field.
    If no species data is present in the text, return an empty JSON array to indicate that no relevant information could be extracted.
    Keep entries consistent and comprehensive for database integration.

    Text to analyze:
    {text}
    """

    data = {
        "model": "meta-llama/llama-3-70b",
        "messages": [{"role": "user", "content": prompt2}]
    }

    # Print the prompt to see what is being sent to the API
    print("Sending the following text to the API:")
    print(prompt2)

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
    test_text1 = "Table 1 Medicinal species from the Brazilian Amazon recorded by von Martius in the 19th century. Family and botanical name Vernacular names Part Occurrence Traditional usea,b,c Correlated studies Apocynaceae Couma utilis (Mart.) Mull.Arg. ( ¨ Collophora utilis Mart.)a Sorveira Latex Rio Negro, near Barra Antihelminthic with ricinus oil a,c None Himatanthus phagedaenicus (Mart.) Woodson (Plumeria phagedaenica Mart.)a Sebuu-¨ uva, Sucu-u ¨ ˆba Latex Rio Negro Externally: infected ulcers; internally: against wormsa,c , psoriasis and warts None Odontadenia macrantha (Roem. & Schult.) Markgr. (Echites grandiflorus G. Mey.)a Sipo´ cururu Wood Amazonas, Guyana Infusion in water to treat dyspepsia and other digestive disordersa , diaphoretic, purgativec None Odontadenia puncticulosa (Rich.) Pulle (Echites cururu Mart.)a,b,c Cipo´ -cururu Wood after flowering Near Panure´; near Rio Urupes Infusion is used as drastic, to treat dyspepsia and digestive disordersa ; to treat gastric feverb Diaphoretic and purgativec None Araceae Caladium bicolour (Aiton) Vent.a Pe´ de bezerro, Papagaio, Tagura´, Tinhorao, Tanhor ~ ao~ Juice Para´, Amazonas Cathartic, antihelminthic, against ascaridsa None Dracontium polyphyllum L.a Jiraraca, Herva de Santa Maria Tubers ‘‘Brasilia amazonica‘‘ Externally: woundsa ; Internally: asthma, chlorosis, amenorrhoea, viper bitesa None Montrichardia arborescens (L.) Schott (Philodendron arborescens (L.) Kunth, Arum arborescens L.)a Aninga, Aninga-uva Leaves,thallus, ¨ roots Amazonas near Japura´, Para´ Healing wounds and ulcers, with fresh juice. Decoction of fresh leaves or dried roots as bath to treat rheumatic pain, testicular and articulation tumours; hydrothoraxa None Pistia stratiotes L. (Pistia occidentalis Blume) a,b Flor d’a´gua Lentilha d‘a´gua n.d. Amazonas, Ega, Rio Solimoes, ~ Para´ Mucilaginous herb, used to clean wounds,infusion internally to treat blood in urine, diabetes, tumours from erysipelas, herpes and hemoptysisa ; old wounds can be healed by application of fresh flowersb Antidiabetic, antidermatophytic, antifungal, antimicrobial, diuretic (Tripathi et al., 2010) Asteraceae Ayapana triplinervis (Vahl) R.M. King & H. Rob. (Eupatorium ayapana Vent.)a,c Ayapana Herb Amazonas, near Sao Jo ~ ao do ~ Principe (Rio Negro) Squeezed herb juice or infusion (internally) and pressed herb (externally) against snake bites and as alexipharmacona Antimicrobial (Gupta et al., 2002) Acanthospermum australe (Loefl.) Kuntze (Acanthospermum xanthioides DC.)a Poejo-da-praia Herb Amazonas near Manaus, Para´ Diuretic, diaphoretic; infusion against diarrhoea (originating from colds)a Antiviral (Rocha Martins et al., 2011); antifungal (Portillo et al., 2001) Bidens pilosa L. (Bidens leucantha (L.) Willd.)a n.d. Herb, branches Near Para´ Mucilaginous herb used together with indigo, Senna uniflora (Mill.) H.S. Irwin & Barneby (Cassia sericea Sw.), to treat skin ulcers and lymphoedema. Roots are more mucilaginous than the stems Antiviral (Nakama et al., 2012); antitumour (Nakama et al., 2011); antibacterial (Tobinaga et al., 2009) Eclipta paludicola Steud. (Eclipta prostrata (L.) L., Eclipta erecta L.)a Tangaraca Herb Amazonas, Para´ Decoction is used to treat diarrhoea None Elephantopus mollis Kunth (Elephantopus. martii Graham)a Suc-uaya Roots Amazonas Decoction is used in asthenic feversa None Bignoniaceae Cybistax antisyphilitica (Mart.) Mart.a Caroba de flor verde Young branches; roots, leaves Amazonas, near Manaus Antisyphilitic, decoction and infusion to treat dysuria, hydrops, water retention; poultice and lotions against syphilitic ulcers a None Jacaranda copaia (Aubl.) D.Don (Jacaranda procera (Willd.) Spreng.)a Caroba Leaves Rio Japura´ Used against venereal diseases, mainly inflammations of inguinal lymph, in baths of infusion or decoction for impingement. High doses of decoction cause vomiting and diarrhoea None Boraginaeae Heliotropium indicum L. (Tiaridium indicum (L.) Lehm.)a Aguara ciunha-ac-u Jacuaacanga n.d. Near O´ bitos, Para´ Desobstruents, to clean wounds and ulcers, against cutaneous affection; used on anal inflammations Wound healing (Dash and Murthy, 2011); antibacterial (Nethaji and Manokaran, 2009) "
    with open('text.txt', 'r') as file:
        test_text = file.read()
    try:
        result1 = extract_information(test_text1)
        print("\nExtracted Data:\n", result1)
    except Exception as e:
        print(e)
    # try:
    #     result2 = extract_json(result1)
    #     print("\nExtracted Data:\n", result2)
    # except Exception as e:
    #     print(e)

if __name__ == "__main__":
    main()