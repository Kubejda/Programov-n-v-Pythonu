import requests

# ČÁST 1

ico = input("Zadejte IČO vyhledávaného subjektu:")
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
response = requests.get(url)
data = response.json()


print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])


# ČÁST 2

nazev = input("Zadejte název vyhledávaného subjektu:")
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = {"obchodniJmeno": nazev}
response = requests.post(url, headers=headers, json=data)
vysledek = response.json()

print(f"Nalezeno subjektů: {vysledek['pocetCelkem']}")

for subjekt in vysledek["ekonomickeSubjekty"]:
    print(subjekt["obchodniJmeno"] + ", " + subjekt["ico"])


   
