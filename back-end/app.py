from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def index():
    return jsonify({
        "image" : "https://th.bing.com/th/id/OIP.lSrLCYcXWcNXH1PDFweHYQHaHa?rs=1&pid=ImgDetMain",
        "title" : "The fall of roman empire",
        "content" : "The fall of the Western Roman Empire, also called the fall of the Roman Empire or the fall of Rome, was the loss of central political control in the Western Roman Empire, a process in which the Empire failed to enforce its rule, and its vast territory was divided among several successor polities. ",
        "category": "history",
        "punctuation" : "3"
    })


if __name__ == "__main__":
    app.run()