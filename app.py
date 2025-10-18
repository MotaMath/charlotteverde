from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('Message')
    
    with open('messages.json', 'a') as file:
     file.write(f"Nome: {name}\nEmail: {email}\Message: {message}\n\n")
     file.close

    return jsonify({"status": "success", "message": "Mensagem recebida com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)