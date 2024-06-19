import requests
import random


def get_random_aya() -> str:
    try:
        verse_num = random.randint(1, 6346)
        # Fetch a random Aya from the API
        response = requests.get(
            f"https://api.alquran.cloud/v1/ayah/{verse_num}/ar.asad")
        response.encoding = 'utf-8'  # Ensure the response is interpreted as UTF-8
        data = response.json()

        if response.status_code == 200 and data['status'] == "OK":
            # Extract Aya text and reference
            aya_text = data['data']['text']
            surah_name = data['data']['surah']['englishName']
            surah_number = data['data']['surah']['number']
            aya_number = data['data']['numberInSurah']

            print(f"Aya from Surah {surah_name}, Aya {aya_number}: {aya_text}")
            return f"Aya from Surah {surah_name}, Aya {aya_number}: {aya_text}"
        else:
            return "Could not fetch a random Aya at the moment."
    except Exception as e:
        return f"Error occurred: {str(e)}"


def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return "Wanna talk?"
    elif 'hello' in lowered:
        return "Hello"
    elif 'hi' in lowered:
        return "Hi"
    elif 'bye' in lowered:
        return "Bye"
    elif 'mnl' in lowered:
        return get_manzil_data()
    else:
        return get_random_aya()
