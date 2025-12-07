from flask import Flask, render_template, request
from wiki import get_wikipedia_page

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        return render_template("index.html", message="Please enter a search term")

    result = get_wikipedia_page(query)

    if result.get("error") == "disambiguation":
        return render_template("result.html", disambiguation=True, options=result["options"])
    elif result.get("error") == "not_found":
        return render_template("result.html", not_found=True, query=query)
    else:
        return render_template("result.html", page=result)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
