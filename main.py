import fitz
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def pdf_oku(dosya_yolu):
    doc = fitz.open(dosya_yolu)
    metin = ""
    for sayfa in doc:
        metin += sayfa.get_text()
    return metin

def ozet_al(metin):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Sen bir metin özetleyicisin. Verilen metni kısa ve anlaşılır şekilde özetle."},
            {"role": "user", "content": f"Bu metni özetle:\n\n{metin[:3000]}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    dosya = input("PDF dosya yolunu gir: ")
    print("\nPDF okunuyor...")
    metin = pdf_oku(dosya)
    print("Özet hazırlanıyor...\n")
    ozet = ozet_al(metin)
    print("ÖZET:")
    print(ozet)