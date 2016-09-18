from flask import Flask, request, render_template, redirect, url_for
from models import *

app = Flask(__name__)


@app.route('/form', methods=["GET"])
def story():
    data = []
    return render_template('form.html', data = data, function = "Add New")


@app.route('/story/', methods=['POST'])
def handle_data():
    user_story = UserStory.create(story_title=request.form['story_title'],
                            user_story=request.form['user_story'],
                            acceptance_criteria=request.form['acceptance_criteria'],
                            business_value = request.form['business_value'],
                            estimation=request.form['estimation'],
                            status=request.form['status'])
    query = UserStory.select()
    return render_template('list.html', user_stories=query)


@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def list_data():
    query = UserStory.select()
    return render_template('list.html', user_stories=query)


@app.route('/delete/<story_id>', methods=['POST'])
def delete_data(story_id):
    story = UserStory.select().where(UserStory.id == story_id).get()
    story.delete_instance()
    story.save()
    return redirect(url_for('list_data'))

@app.route("/story/<story_id>", methods=["GET"])
def render_edit(story_id):
    data = UserStory.get(UserStory.id == story_id)
    return render_template("form.html", data = data, function = "Edit")


@app.route('/story/<story_id>', methods=['POST'])
def update_data(story_id):
    update = UserStory.update(story_title=request.form["story_title"],
                                user_story=request.form["user_story"],
                                acceptance_criteria=request.form["acceptance_criteria"],
                                business_value=request.form["business_value"],
                                estimation=request.form["estimation"],
                                status=request.form["status"]).where(UserStory.id == story_id)
    update.execute()
    return redirect("http://localhost:5000/")


if __name__ == '__main__':
    app.run(debug=True)

