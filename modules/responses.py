import requests
import random

books = {
    "1": ["abu-daud", 4419],
    "2": ["ahmad", 4305],
    "3": ["bukhari", 6638],
    "4": ["darimi", 2949],
    "5": ["ibnu-majah", 4285],
    "6": ["malik", 1587],
    "7": ["muslim", 4930],
    "8": ["nasai", 5364],
    "9": ["tirmidzi", 3625]
}


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

            response_tafseer = requests.get(
                f"http://api.quran-tafseer.com/tafseer/3/{surah_number}/{aya_number}")
            # Ensure the response is interpreted as UTF-8
            response_tafseer.encoding = 'utf-8'
            tafseer_data = response_tafseer.json()

            if response_tafseer.status_code == 200 and 'text' in tafseer_data:
                tafseer_text = tafseer_data['text']
            else:
                tafseer_text = "Tafseer not available."

            final_text = (
                f"Aya from Surah {surah_name}, Aya {aya_number}: {aya_text}\n\n"
                f"Tafseer Elsaadi: \n {tafseer_text}"
            )

            return final_text
        else:
            return "Could not fetch a random Aya at the moment."
    except requests.RequestException as e:
        return f"Network error occurred: {str(e)}"
    except Exception as e:
        return f"Error occurred: {str(e)}"


def get_random_hadith() -> str:
    try:
        # Select a random book and hadith number
        book_num = random.randint(1, 9)
        book_id = books[str(book_num)][0]
        book_hadith_nums = books[str(book_num)][1]
        hadith_num = random.randint(1, book_hadith_nums)

        # Fetch a random hadith from the API
        response = requests.get(
            f"https://api.hadith.gading.dev/books/{book_id}/{hadith_num}"
        )
        response.encoding = 'utf-8'  # Ensure the response is interpreted as UTF-8
        data = response.json()

        if response.status_code == 200:
            # Extract Hadith text and reference
            hadith_text = data['data']['contents']['arab']
            hadith_number = data['data']['contents']['number']
            hadith_reference = data['data']['name']

            final_text = (
                f"Hadith from {hadith_reference}, No. {hadith_number}:\n"
                f"{hadith_text}\n\n"
            )

            return final_text
        else:
            return "Could not fetch a random Hadith at the moment."
    except requests.RequestException as e:
        return f"Network error occurred: {str(e)}"
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
    elif 'hd' in lowered:
        return get_random_hadith()
    else:
        return get_random_aya()
