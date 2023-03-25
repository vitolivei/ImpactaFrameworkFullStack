from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)
        media = (primeira + segunda) / 2

        return str(media)
    else:
        return 'Insira as notas na URL.'

if __name__ == '__main__':
    app.run(debug=True)
