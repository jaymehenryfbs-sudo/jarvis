import requests



TOKEN = "8733557221:AAHbEemfuiiot93Dmc0bry8VIiKvL_olTYE"

CHAT_ID = "6601796698"



def test_liaison():

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {

        "chat_id": CHAT_ID,

        "text": "🤖 [SYSTÈME] Monsieur, la liaison satellite est établie. J.A.R.V.I.S. est prêt à sécuriser le périmètre."

    }

    try:

        response = requests.post(url, json=payload)

        if response.status_code == 200:

            print("✅ Succès ! Vérifiez votre téléphone.")

        else:

            print(f"❌ Échec. Code erreur : {response.status_code}")

    except Exception as e:

        print(f"❌ Erreur de connexion : {e}")



if __name__ == "__main__":

    test_liaison()
