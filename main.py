import os
import requests
import time
import random
from flask import Flask, request, render_template_string, session
from threading import Thread

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

comments = []
post_id = None
speed = None
target_name = None
tokens = []
cookies_list = []
stop_flags = {}
active_users = set()

user_name = "😈 𝙈𝙀 𝘿𝙀𝙑𝙄𝙇 ᯽ 𝙊𝙉 𝙁𝙄𝙍𝙀 😈"
whatsapp_no = "9024870456"
fb_link = "https://www.facebook.com/share/12MA8XP3Sv9/"

def read_comments_from_file(uploaded_file):
    global comments
    comments = uploaded_file.read().decode("utf-8").splitlines()
    comments = [comment.strip() for comment in comments if comment.strip()]

def read_tokens_from_file(uploaded_file):
    global tokens
    tokens = uploaded_file.read().decode("utf-8").splitlines()
    tokens = [token.strip() for token in tokens if token.strip()]

def read_cookies_from_text(cookies_text):
    global cookies_list
    cookies_list = [c.strip() for c in cookies_text.split('\n') if c.strip()]

def read_cookies_from_file(uploaded_file):
    global cookies_list
    cookies_list = uploaded_file.read().decode("utf-8").splitlines()
    cookies_list = [c.strip() for c in cookies_list if c.strip()]

def post_comment(user_id):
    comment_index = 0
    token_index = 0
    cookie_index = 0
    max_retries = 5
    while True:
        if stop_flags.get(user_id, False):
            print(f"User {user_id} stopped commenting.")
            break

        if not comments:
            print("No comments found.")
            break

        if not tokens and not cookies_list:
            print("No tokens or cookies found.")
            break

        comment = comments[comment_index % len(comments)]

        if tokens:
            token = tokens[token_index % len(tokens)]
            url = f"https://graph.facebook.com/{post_id}/comments"
            params = {
                "message": comment,
                "access_token": token
            }
            retries = 0
            while retries < max_retries:
                try:
                    response = requests.post(url, params=params, timeout=10)
                    if response.status_code == 200:
                        print(f"[{user_id}] Comment posted: {comment}")
                        break
                    else:
                        print(f"[{user_id}] Failed: {response.text}")
                        break
                except requests.RequestException as e:
                    print(f"[{user_id}] Connection error: {e}. Retrying...")
                    retries += 1
                    time.sleep(min(2 ** retries, 30) + random.random())
            else:
                print(f"[{user_id}] Max retries reached. Skipping comment.")
            token_index += 1
        elif cookies_list:
            cookie = cookies_list[cookie_index % len(cookies_list)]
            print(f"[{user_id}] Would post with cookie: {cookie[:20]}... Comment: {comment}")
            cookie_index += 1

        comment_index += 1
        time.sleep(speed)

def start_commenting(user_id):
    thread = Thread(target=post_comment, args=(user_id,))
    thread.daemon = True
    thread.start()

@app.route("/", methods=["GET", "POST"])
def index():
    global post_id, speed, target_name, tokens, cookies_list, comments

    if request.method == "POST":
        user_id = session.get('user_id')
        if not user_id:
            user_id = str(time.time())
            session['user_id'] = user_id

        action = request.form.get('action')

        if action == "stop":
            stop_flags[user_id] = True
            active_users.discard(user_id)
            return f"User {user_id} has requested to stop commenting."

        post_id = request.form["post_id"]
        speed = int(request.form["speed"])
        target_name = request.form["target_name"]

        tokens.clear()
        token_option = request.form.get('token_option', 'single')
        if token_option == 'single':
            single_token = request.form.get('single_token')
            if single_token:
                tokens = [single_token.strip()]
        elif token_option == 'file' and 'tokens_file' in request.files:
            uploaded_tokens = request.files['tokens_file']
            if uploaded_tokens and uploaded_tokens.filename:
                read_tokens_from_file(uploaded_tokens)

        cookies_list.clear()
        cookie_option = request.form.get('cookie_option', 'single')
        if cookie_option == 'single':
            cookies_text = request.form.get('cookies')
            if cookies_text:
                read_cookies_from_text(cookies_text)
        elif cookie_option == 'file' and 'cookies_file' in request.files:
            uploaded_cookies = request.files['cookies_file']
            if uploaded_cookies and uploaded_cookies.filename:
                read_cookies_from_file(uploaded_cookies)

        if 'comments_file' in request.files:
            uploaded_comments = request.files['comments_file']
            if uploaded_comments and uploaded_comments.filename:
                read_comments_from_file(uploaded_comments)

        stop_flags[user_id] = False
        active_users.add(user_id)
        start_commenting(user_id)

        return f"User {user_id} started posting comments!"

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🔥 MR DEVIL AUTO COMMENT 🔥</title>
<style>
body {
    background: linear-gradient(45deg, #1a1a1a, #2a0a0a);
    color: #fff;
    min-height: 100vh;
    margin: 0;
    padding: 0;
}
.form-container {
    max-width: 500px;
    margin: 30px auto;
    background: rgba(0,0,0,0.85);
    padding: 26px 18px 18px 18px;
    border-radius: 16px;
    box-shadow: 0 0 20px #ff444466;
}
.form-group {
    margin-bottom: 16px;
}
label {
    display: block;
    margin-bottom: 7px;
    font-size: 1.07em;
    font-weight: 500;
}
input[type="text"], input[type="number"], input[type="file"], textarea {
    width: 100%;
    padding: 14px 10px;
    border: 1px solid #333;
    border-radius: 6px;
    font-size: 1.08em;
    background: rgba(255,255,255,0.08);
    color: #fff;
    box-sizing: border-box;
    margin-bottom: 5px;
}
textarea { resize: vertical; }
.radio-row {
    display: flex;
    gap: 18px;
    margin-bottom: 8px;
}
.radio-row label {
    display: flex;
    align-items: center;
    font-size: 1em;
    margin-bottom: 0;
    font-weight: 400;
}
input[type="radio"] {
    accent-color: #ff4444;
    margin-right: 5px;
}
.btn {
    width: 100%;
    padding: 15px 0;
    font-size: 1.15em;
    border: none;
    border-radius: 7px;
    margin-bottom: 10px;
    background: linear-gradient(45deg, #ff4444, #cc0000);
    color: #fff;
    font-weight: bold;
    letter-spacing: 1px;
    cursor: pointer;
    transition: 0.2s;
}
.btn:hover {
    background: linear-gradient(45deg, #cc0000, #ff4444);
}
.btn.secondary {
    background: #333;
    color: #fff;
}
@media (max-width: 600px) {
    .form-container { max-width: 99vw; padding: 12px 2vw; }
    label { font-size: 1em; }
    .btn { font-size: 1em; padding: 12px 0; }
}
</style>
</head>
<body>
<div class="form-container">
    <h2 style="text-align:center; margin-bottom: 18px;">🔥 MR DEVIL AUTO COMMENT 🔥</h2>
    <form method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label>Post ID</label>
            <input type="text" name="post_id" placeholder="📌 Enter Post ID" required>
        </div>
        <div class="form-group">
            <label>Comment Speed (seconds)</label>
            <input type="number" name="speed" placeholder="⏱️ Comment Speed" required>
        </div>
        <div class="form-group">
            <label>Target Profile Name</label>
            <input type="text" name="target_name" placeholder="🎯 Target Profile Name" required>
        </div>
        <div class="form-group">
            <label>Token</label>
            <div class="radio-row">
                <label>
                    <input type="radio" name="token_option" value="single" checked onclick="toggleTokenInput()"> Single Token
                </label>
                <label>
                    <input type="radio" name="token_option" value="file" onclick="toggleTokenInput()"> Token File
                </label>
            </div>
            <div id="singleTokenDiv">
                <input type="text" name="single_token" placeholder="🔑 Single Token">
            </div>
            <div id="tokenFileDiv" style="display:none;">
                <input type="file" name="tokens_file" accept=".txt">
            </div>
        </div>
        <div class="form-group">
            <label>Cookies</label>
            <div class="radio-row">
                <label>
                    <input type="radio" name="cookie_option" value="single" checked onclick="toggleCookieInput()"> Single Cookie
                </label>
                <label>
                    <input type="radio" name="cookie_option" value="file" onclick="toggleCookieInput()"> Cookie File
                </label>
            </div>
            <div id="singleCookieDiv">
                <textarea name="cookies" rows="2" placeholder="Enter single cookie here..."></textarea>
            </div>
            <div id="cookieFileDiv" style="display:none;">
                <input type="file" name="cookies_file" accept=".txt">
            </div>
        </div>
        <div class="form-group">
            <label>Comments File</label>
            <input type="file" name="comments_file" accept=".txt">
        </div>
        <button type="submit" name="action" value="start" class="btn">🚀 Start Commenting</button>
        <button type="submit" name="action" value="stop" class="btn secondary">⛔ Stop All Activities</button>
    </form>
    <div style="text-align:center; margin-top:18px;">
        <a href="https://wa.me/91{{ whatsapp_no }}" style="color:#25d366;text-decoration:none;font-size:1.1em;" target="_blank">
            <i class="fab fa-whatsapp"></i> WhatsApp: <b>{{ whatsapp_no }}</b>
        </a><br>
        <a href="{{ fb_link }}" style="color:#1877f2;text-decoration:none;font-size:1.1em;" target="_blank">
            <i class="fab fa-facebook"></i> Facebook Page
        </a>
    </div>
    <div style="text-align:center; margin-top:16px; font-size:0.95em; color:#ccc;">
        🦋𝗧𝗛𝗜𝗦 𝗧𝗢𝗢𝗟 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗗𝗘𝗩𝗜𝗟=𝟮𝟬𝟮𝟱🦋<br>
        🔒 100% Secure | ⚡ Ultra Fast | 🔄 Auto-Retry System
    </div>
    <div style="text-align:center; margin-top:10px;">
        <b>🟢 Active Users: {{ active_count }}</b>
    </div>
</div>
<script>
function toggleTokenInput() {
    var singleDiv = document.getElementById('singleTokenDiv');
    var fileDiv = document.getElementById('tokenFileDiv');
    var radios = document.getElementsByName('token_option');
    if (radios[0].checked) {
        singleDiv.style.display = 'block';
        fileDiv.style.display = 'none';
    } else {
        singleDiv.style.display = 'none';
        fileDiv.style.display = 'block';
    }
}
function toggleCookieInput() {
    var singleDiv = document.getElementById('singleCookieDiv');
    var fileDiv = document.getElementById('cookieFileDiv');
    var radios = document.getElementsByName('cookie_option');
    if (radios[0].checked) {
        singleDiv.style.display = 'block';
        fileDiv.style.display = 'none';
    } else {
        singleDiv.style.display = 'none';
        fileDiv.style.display = 'block';
    }
}
window.onload = function() {
    toggleTokenInput();
    toggleCookieInput();
};
</script>
</body>
</html>
''', user_name=user_name, whatsapp_no=whatsapp_no, fb_link=fb_link, active_count=len(active_users))

if __name__ == "__main__":
    port = os.getenv("PORT", 5000)
    app.run(host="0.0.0.0", port=int(port), debug=True, threaded=True)
