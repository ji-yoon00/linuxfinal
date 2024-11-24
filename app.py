from flask import Flask, render_template_string
import subprocess, logging
app = Flask(__name__)

# 로그 파일 설정
logging.basicConfig(filename='button_clicks.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# 기본 페이지, 버튼을 클릭하면 '/button' 페이지로 이동
@app.route('/')
def home():
    return render_template_string('''
        <html>
            <body>
                <h1>Welcome to the Flask App</h1>
                <button onclick="window.location.href='/button'">Click Me</button>
            </body>
        </html>
    ''')


def commit_button_click():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Button clicked"])
    subprocess.run(["git", "push", "origin", "main"])


# 버튼 클릭 후 이동할 페이지
@app.route('/button')
def button_page():
    # 버튼 클릭을 로그에 기록
    logging.info("Button was clicked!")
    commit_button_click()
    return "<h1>Button Clicked! You are now on a new page.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

