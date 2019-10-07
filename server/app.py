from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from serializers import tags_schema
from db import Session, Tag, User, English, User_English_link

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

if __name__ == '__main__':
  app.run(host='localhost', port=8888, debug=True)