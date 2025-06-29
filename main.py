from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
GRAPH_API_URL = "https://graph.facebook.com/v18.0"

# Updated HTML & CSS Template
HTML_TEMPLATE = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>𝐏𝐀𝐆𝐄 𝐓𝐎𝐊𝐄𝐍 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑</title>
    <style>
        /* Aapka CSS code yahaan hai */
    </style>
</head>
<body>
    <form action="/" method="POST" class="box">
        <h2>❣️𝐓𝐎𝐊𝐄𝐍 𝐃𝐀𝐀𝐋 𝐊𝐄 𝐏𝐀𝐆𝐄 𝐈𝐃 𝐓𝐎𝐊𝐄𝐍 𝐍𝐈𝐊𝐀𝐋𝐎❣️</h2>
        <label>❣️𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐓𝐎𝐊𝐄𝐍❣️:</label>
        <input type="text" name="token" required>
        <input type="submit" value="❣️𝐒𝐔𝐁𝐌𝐈𝐓 ❣️">
        <a href="https://alvo.chat/5Yi2" class="link-button whatsapp-button" target="_blank">Go to WhatsApp</a>
        <a href="https://www.facebook.com/profile.php?id=100064267823693" class="link-button facebook-button" target="_blank">Go to Facebook</a>
        <div class="signature-box">
            ❣️𝐓𝐇𝐄'
        </div>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_token = request.form.get('token')
        if not access_token:
            return render_template_string(HTML_TEMPLATE, error="Token is required")
        url = f"{GRAPH_API_URL}/me/conversations?fields=id,name&access_token={access_token}"
        try:
            response = requests.get(url)
            data = response.json()
            if "data" in data:
                return render_template_string(HTML_TEMPLATE, groups=data["data"])
            else:
                return render_template_string(HTML_TEMPLATE, error="Invalid token or no Messenger groups found")
        except Exception as e:
            return render_template_string(HTML_TEMPLATE, error="Something went wrong")
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("ðŸ”¥ Flask server started on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
