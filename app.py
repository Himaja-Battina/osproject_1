from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "hello, welcome to ibm isdl labs !!"
# if __name__=="__main__":
#     app.run(debug=True)
#added new comment

"""from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello!</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)"""
print("hello")
