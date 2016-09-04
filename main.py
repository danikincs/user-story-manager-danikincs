from flask import Flask, request, render_template, redirect, url_for

from models import *
db.connect()

db.create_tables([UserStory], safe=True)

app = Flask(__name__)
app.debug = True


@app.route('/form')
def story():
    return render_template('form.html')


@app.route('/story', methods=['POST'])
def handle_data():
    user_story = UserStory.create(story_title = request.form['story_title'],
                            user_story=request.form['user_story'],
                            acceptance_criteria=request.form['acceptance_criteria'],
                            business_value = request.form['business_value'],
                            estimation = request.form['estimation'],
                            status=request.form['status'])
    query = UserStory.select()
    return render_template('list.html', user_stories=query)


@app.route('/')
@app.route('/list')
def list_data():
    query = UserStory.select()
    return render_template('list.html', user_stories=query)


@app.route('/delete/<story_id>', methods=['POST'])
def delete_data(story_id):
    story = UserStory.select().where(UserStory.story_id == story_id).get()
    story.delete_instance()
    story.save()
    return redirect(url_for('list_data'))

if __name__ == '__main__':
    app.run()

