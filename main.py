from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
GRAPH_API_URL = "https://graph.facebook.com/v18.0"

HTML_TEMPLATE = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>𝐏𝐀𝐆𝐄 𝐓𝐎𝐊𝐄𝐍 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100vh;
            width: 100vw;
            overflow-x: hidden;
            background:      
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            color:      
            touch-action: manipulation;
        }
        .box {
            background:         
            border: 2px solid         
            border-radius: 10px;
            padding: 30px;
            width: 90%;
            max-width: 400px;
            box-shadow: 0 0 20px         
            animation: fadeIn 1s ease-in;
            text-align: center;
            margin-top: 20px;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        input[type="#111;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            color: #fff;
            touch-action: manipulation;
        }
        .box {
            background: #ff69b4;
            border: 2px solid #00ffcc;
            border-radius: 10px;
            padding: 30px;
            width: 90%;
            max-width: 400px;
            box-shadow: 0 0 20px #00ffcc;
            animation: fadeIn 1s ease-in;
            text-align: center;
            margin-top: 20px;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            border: 2px solid         
            border-radius: 5px;
            background:      
            color:      
        }
        input[type="#4CAF50;
            border-radius: 5px;
            background: #333;
            color: #fff;
        }
        input[type="submit"] {
            background:         
            color:      
            padding: 12px;
            width: 100%;
            border: none;
            margin-top: 20px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        input[type="#8BC34A;
            color: #000;
            padding: 12px;
            width: 100%;
            border: none;
            margin-top: 20px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        input[type="submit"]:hover {
            background:         
        }
        .link-button {
            display: block;
            text-decoration: none;
            margin-top: 10px;
            padding: 6px 10px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 14px;
            width: 70%;
            margin-left: auto;
            margin-right: auto;
            transition: background 0.3s;
        }
        .whatsapp-button {
            background:         
            color:      
        }
        .whatsapp-button:hover {
            background:         
        }
        .facebook-button {
            background:         
            color:      
        }
        .facebook-button:hover {
            background:         
        }
        .signature-box {
            margin-top: 25px;
            padding: 15px;
            border: 1px dashed         
            border-radius: 10px;
            font-size: 14px;
            color:         
            background-color:      
        }
    </style>
</head>
<body>
    <form action="#3e8e41;
        }
        .link-button {
            display: block;
            text-decoration: none;
            margin-top: 10px;
            padding: 6px 10px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 14px;
            width: 70%;
            margin-left: auto;
            margin-right: auto;
            transition: background 0.3s;
        }
        .whatsapp-button {
            background: #25D366;
            color: #000;
        }
        .whatsapp-button:hover {
            background: #1ebe5d;
        }
        .facebook-button {
            background: #3b5998;
            color: #fff;
        }
        .facebook-button:hover {
            background: #334d84;
        }
        .signature-box {
            margin-top: 25px;
            padding: 15px;
            border: 1px dashed #ff9800;
            border-radius: 10px;
            font-size: 14px;
            color: #ff9800;
            background-color: #333;
        }
    </style>
</head>
<body>
    <form action="/" method="POST" class="box">
        <h2>❣️𝐓𝐎𝐊𝐄𝐍 𝐃𝐀𝐀𝐋 𝐊𝐄 𝐏𝐀𝐆𝐄 𝐈𝐃 𝐓𝐎𝐊𝐄𝐍 𝐍𝐈𝐊𝐀𝐋𝐎❣️</h2>
        <label>❣️𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐓𝐎𝐊𝐄𝐍❣️:</label>
        <input type="text" name="token" required>
        <input type="submit" value="❣️𝐒𝐔𝐁𝐌𝐈𝐓 ❣️">
        <a href="https://alvo.chat/5Yi2" class="link-button whatsapp-button" target="_blank">Go to WhatsApp</a>
        <a href="https://www.facebook.com/profile.php?id=100064267823693" class="link-button facebook-button" target="_blank
