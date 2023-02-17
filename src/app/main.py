from flask import Flask, request, render_template
import pickle


modelo = pickle.load(open('../../models/modelo.pkl','rb'))


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html',titulo="Satisfação de clientes")


@app.route('/soma/<int:valor>')
def soma(valor):
    return "Resultado: {}".format(valor+5)


@app.route('/predicao/<int:v1>/<int:v2>/<int:v3>/<int:v4>/<int:v5>/<int:v6>/<int:v7>/<int:v8>/<int:v9>/<int:v10>/<int:v11>/<int:v12>/<int:v13>/')
def predicao(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13):
    resultado = modelo.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]])
    return "Classe: {}".format(resultado)

@app.route('/predicaoform',methods=['POST'])
def form():
    gender = request.form['gender']    
    age = request.form['age']
    typeOfTravel = request.form['typeOfTravel']
    wifi_service = request.form['wifi-service']
    depature_arrival = request.form['depature-arrival']
    ease_online = request.form['ease-online']
    hotel_location = request.form['hotel-location']
    food_and_drink = request.form['food-and-drink']
    comfort = request.form['comfort']
    room_enter = request.form['room-enter']
    checkin_checkout = request.form['checkin-checkout']
    other = request.form['other']
    cleanliness = request.form['cleanliness']
    

    result = modelo.predict([[gender,age ,typeOfTravel, wifi_service, depature_arrival, ease_online, hotel_location, food_and_drink, comfort, room_enter, checkin_checkout, other, cleanliness ]])
    
    if result[0] == 1:
        resultado='Satisfeito'
    elif result[0] == 2:
        resultado='Insatisfeito'

    return render_template('resultado.html',titulo="Previsão", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)