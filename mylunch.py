from flask import Flask, render_template
from random import sample
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/haedal")
def haedal():
    return "This is Haedal"

@app.route("/greeting/<string:name>")
def greeting(name):
  return f'반갑습니다. {name}!'

@app.route("/cube/<int:num>")
def cube(num):
  result = num ** 3
  return f'{num}의 세제곱은 {result}'

# 사람 수 만큼 점심 메뉴 추천
@app.route("/lunch/<int:people>")
def lunch(people):
  menu = ["짜장면", "짬뽕", "라면", "브리또", "사과", "찜닭"]
  return f'{sample(menu, people)}'

# 점심 메뉴 보여주자
@app.route("/show")
def show():
  menu = ['짜장면.jpg', '짬뽕.jpeg']
  pickme = ''.join(sample(menu,1))
  return render_template('index.html', food_img=pickme)

# Flask를 쉽게 켜자
if __name__ == '__main__':
  app.run(debug=True)