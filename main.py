from flask import Flask, request
import services

app = Flask(__name__)

@app.route('/')
def index():
  return """
  <h1>Caesar Cipher App</h1>
  <hr />
  <form method="POST" action='/cipher'>
  Mode: 
  <input type="radio" name="mode" value="encrypt" checked="checked" /> Encrypt
  <input type="radio" name="mode" value="decrypt" /> Decrypt
  <br />
  <label>Secret Message:</label>
  <input type="text" name="secret" />
  <br />
  <label>Key:</label>
  <input type='number' name='key' />
  
  <input type="submit" value="Submit" />
  </form>
  """

@app.route('/cipher', methods=['GET', 'POST'])
def cipher():
  mode = request.form.get('mode', 'encrypt')
  message = request.form.get('secret', None)
  key = request.form.get('key', None)
  if not message or not key:
    return 'You must provide a valid message and a valid key!'
  else:
    cipher_message = services.cipher(message, key=int(key), mode=mode)
    
  return f"""
      Your message: {cipher_message}
      <br />
      <a href='/'>Return</a>
      """
  


app.run(debug=True, host='0.0.0.0', port='3003')