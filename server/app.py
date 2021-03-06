from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from serializers import tags_schema
from db import engine, Session, Tag, User, English, User_English_link

app = Flask(__name__)
bcrypt = Bcrypt()

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/api/<entry>')
def api_entry(entry):
  sess = Session()
  tags = sess.query(Tag).all()
  return tags_schema.dumps(tags)

@app.route('/api/sign-up', methods=['POST'])
def sign_up():
  sess = Session()
  data = request.get_json(silent=True)
  if data:
    print(data)
    password = data.get('password', '')
    name = data.get('name', '')
    if name and len(password) > 6:
      if not sess.query(User).filter(User.name == name).first():
        user = User(name=name, password=bcrypt.generate_password_hash(password))
        sess.add(user)
        sess.commit()
        return jsonify({'msg': 'signed up successfully'})
    if name:
      return jsonify({'msg': 'user already exits'})
    else:
      return jsonify({'msg': 'the length of password must be over 6'})
  return jsonify({ 'msg': 'request data is invalid' })

@app.cli.command('clear-migration-versions')
def clear_migration_versions():
  with engine.connect() as conn:
    is_exists = conn.execute(
      "select exists (select 1 from information_schema.tables where table_name = '?')",
      "alembic_version"
     ).fetchone()[0]
    if is_exists:
      conn.execute('delete from alembic_version')

@app.cli.command('seed')
def seed():
  sess = Session()
  for name in ["familiar", "unfamiliar", "not sure"]:
    res = sess.query(Tag).filter(Tag.name == name).first()
    if not res:
      sess.add(Tag(name=name))
  sess.commit()

if __name__ == '__main__':
  app.run(host='localhost', port=8888, debug=True)