from flask import Flask, request, render_template_string

app = Flask(__name__)

comments = {}
user_comment_count = {}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comment Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        .comment {
            border-bottom: 1px solid #ccc;
            padding: 10px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Comment Server</h1>
        <form method="post">
            <input type="text" name="user_id" placeholder="Enter your Facebook ID">
            <textarea name="comment" placeholder="Enter your comment" style="width: 100%; height: 100px; padding: 10px; border: 1px solid #ccc;"></textarea>
            <button type="submit" style="background-color: #4CAF50; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Post Comment</button>
        </form>
        <h2>Comments:</h2>
        {% for user_id, user_comments in comments.items() %}
            <h3>User ID: {{ user_id }}</h3>
            {% for comment in user_comments %}
                <div class="comment">{{ comment }}</div>
            {% endfor %}
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        comment = request.form.get("comment")
        if user_id not in user_comment_count:
            user_comment_count[user_id] = 0
            comments[user_id] = []
        if user_comment_count[user_id] < 1000:
            comments[user_id].append(comment)
            user_comment_count[user_id] += 1
        else:
            return "Aapke comments ki limit poori ho gayi hai!"
    return render_template_string(html_template, comments=comments)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
