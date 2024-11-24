from flask import Flask, render_template_string, redirect, url_for
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

# 버튼 클릭 후 이동할 페이지
@app.route('/button')
def button_page():
    # 버튼 클릭 로그 기록
    logging.info("Button was clicked!")
    
    # Git 작업을 실행하는 함수 호출
    commit_button_click()

    # 버튼 클릭 후 "Button Clicked!" 메시지를 보여주는 페이지로 이동
    return '''
        <html>
            <body>
                <h1>Button Clicked! You are now on a new page.</h1>
            </body>
        </html>
    '''

# Git 작업을 처리하는 함수
def commit_button_click():
    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Button clicked"])
        subprocess.run(["git", "push", "origin", "branch1"])
    except Exception as e:
        logging.error(f"Error during Git operation: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

