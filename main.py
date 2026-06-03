from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Containerized Python API</title>
        <style>
            body{
                background:#1e1e1e;
                color:white;
                font-family:Arial, sans-serif;
                text-align:center;
                padding-top:50px;
            }
            .container{
                width:80%;
                margin:auto;
                border:1px solid #555;
                border-radius:10px;
                padding:30px;
                background:#252526;
            }
            h1{
                font-size:40px;
            }
            h2{
                margin-top:30px;
            }
            button{
                background:#2196F3;
                color:white;
                border:none;
                padding:10px 20px;
                margin:10px;
                border-radius:5px;
                cursor:pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the webpage, Hari Loganathan!</h1>
            <p>"The only way to do great work is to love what you do." - Steve Jobs</p>

            <h1>🚀</h1>

            <h2>Containerized Python API</h2>

            <p>
            This is a containerized application that exposes a JSON API using FastAPI.
            </p>

            <button onclick="window.location.href='/docs'">
                Try it out
            </button>

            <button onclick="window.location.href='https://github.com'">
                Project Source
            </button>
        </div>
    </body>
    </html>
    """
