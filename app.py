import flask
import db
app = flask.Flask(__name__)

db.database_creation.create()


@app.route('/')
def index():
    return flask.render_template('index.html')
# {{url_for('.static', filename='IndexFrame.css')}}


@app.route('/loader', methods=['POST'])
def loader():
    if flask.request.form['id'] == '': return flask.render_template('ID_Dialog.html')
    return flask.redirect(flask.url_for('load', id_text=flask.request.form['id']))
@app.route('/id_sel')
def id_sel():
    return flask.render_template('ID_Dialog.html')

@app.route('/load/<id_text>')
def load(id_text):
    return flask.render_template('LoadTextFromDB.html', ID_text=id_text, Text1=db.search_module.db_search(id_text))


@app.route('/upload')
def upload():
    return flask.render_template('UploadTextToDB.html')


@app.route('/db_add', methods=['POST'])
def db_add():
    if flask.request.form['text'] == '' or flask.request.form['text'] == '  ': return flask.render_template('UploadTextToDB.html')
    id_text = db.insert_module.db_insert(flask.request.form['text'])
    return flask.redirect(flask.url_for('load', id_text=id_text))


@app.route('/api/get/<id_get>', methods=['GET'])
def api_get(id_get):
    return flask.jsonify({'text': db.search_module.db_search(id_get)})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)