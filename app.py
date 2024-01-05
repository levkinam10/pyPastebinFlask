import flask
import db
app = flask.Flask(__name__)

db.database_creation.create()


@app.route('/')
def index():
    return flask.render_template('index.html')
#{{url_for('.static', filename='IndexFrame.css')}}


@app.route('/load')
def load():
    return flask.render_template('LoadTextFromDB.html', ID_text='ID', Text1='Text')


@app.route('/upload')
def upload():
    return flask.render_template('UploadTextToDB.html')


@app.route('/db_add', methods=['POST'])
def db_add():
    if flask.request.form['text'] == '' or flask.request.form['text'] == '  ': return flask.render_template('UploadTextToDB.html')
    print(db.insert_module.db_insert(flask.request.form['text']))
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)