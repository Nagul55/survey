from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'survey_secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        regno = request.form['regno']
        college = request.form['college']
        # Save or store in session if needed
        return redirect('/question/1')
    return render_template('index.html')


# Survey Questions
questions = [
    {
        "text": "Which programming language do you like most?",
        "options": ["Python", "Java", "C++", "JavaScript"]
    },
    {
        "text": "Which field are you interested in?",
        "options": ["AI/ML", "Web Development", "Cybersecurity", "Data Science"]
    },
    {
        "text": "How many hours do you spend coding daily?",
        "options": ["<1 hour", "1–2 hours", "2–4 hours", "5+ hours"]
    }
]

@app.route("/question/<int:qid>", methods=["GET", "POST"])
def question(qid):
    if qid > len(questions) or qid < 1:
        return redirect(url_for('question', qid=1))

    if request.method == 'POST':
        selected = request.form.get('option')
        session[str(qid)] = selected
        return redirect(url_for('question', qid=qid+1 if qid < len(questions) else qid))

    q = questions[qid - 1]
    return render_template("question.html", qid=qid, question=q["text"], options=q["options"], total_questions=len(questions))



if __name__ == '__main__':
    app.run(debug=True)
