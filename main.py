from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

### コードいろいろ... ###
# 課題１

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>ホームページ</title>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>これは、24FI019のホームページです。</p>

            <h2>趣味</h2>
            <ul>
            <li>卓球</li>
            <li>ゲーム(FPS)</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

#課題２
@app.post("/present")
async def give_present(present: str):

    gifts = [
        "キャンディー",
        "ケーキ",
        "ぬいぐるみ",
        "ゲームソフト",
        "チョコレート",
        "図書カード"
    ]

    return_gift = random.choice(gifts)
    return {
        "response": f"{present}をありがとう！お返しに{return_gift}をプレゼントします！"
    }