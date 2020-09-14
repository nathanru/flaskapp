from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
  return '''<h1>Adopt a Pet!</h1>
  <P>Browse through the links below to find your new furry friend:</p>
  <ul>
      <li><a href ='/animals/dogs'>Dogs</a></li>
      <li><a href ='/animals/cats'>Cats</a></li>
      <li><a href ='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''
@app.route("/animals/<pet_type>")

def animals(pet_type):
    html = f'<h1>List of {pet_type} </h>'
    return html
