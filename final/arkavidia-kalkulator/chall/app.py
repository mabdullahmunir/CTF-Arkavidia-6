from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)

BLACKLISTED_KEYWORD = []


@app.route('/')
def index():
    page = request.args.get('page')
    if page:

        if any(blist in page for blist in BLACKLISTED_KEYWORD):
            return render_template("index.html", hacker=True)

        if 'calc' in page:
            return render_template("calc.html")
        elif 'about' in page:
            return render_template("about.html")
        else:
            notfound = """
        {%% extends "base.html" %%}
        {%% block content_ %%}
          <div>
            <h1>404!</h1>
            <h3>Page %s not found</h3>
          </div>
        {%% endblock %%}
        """ % page
            return render_template_string(notfound)
    return render_template("index.html")


@app.route("/calc", methods=["POST"])
def lave():
    q = request.form.get('calc')

    if any(blist in q for blist in BLACKLISTED_KEYWORD) or 'open' in q:
        return render_template("index.html", hacker=True)

    if q:
        try:
            res = eval(q)
        except NameError:
            res = ''
        return render_template("index.html", result = res)


if __name__ == "__main__":
    with open("blacklist", "r") as fin:
        data = fin.readlines()
        for line in data:
            BLACKLISTED_KEYWORD.append(line.strip())
    app.run(host='0.0.0.0', port=1234, debug=False)
