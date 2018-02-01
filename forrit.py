from bottle import *
import os

frettir = [
    {
        'Titill': 'Stormur á Íslandi',
        'Grein': 'Það mun ganga í suðaustan storm á Suður- og Vesturlandi í kvöld. Í fyrstu mun honum fylgja snjókoma sem síðar verður að stórhríð að sögn Veðurstofunnar. „Það dregur til tíðinda í kvöld,“ eins og veðurfræðingur kemst að orði. Frostið verður á bilinu 0 til 9 stig.',
        'Netfang': 'hehexd@gmail.com',
        'Mynd': 'frett1.jpg'
    },
    {
        'Titill':'Gunnar Nelsson nýr Forstjóri',
        'Grein':'Það hafa verið breytingar hjá Mjölni síðustu mánuði og sú nýjasta er sú að stærsta stjarna félagsins, Gunnar Nelson, er orðinn formaður félagsins.',
        'Netfang':'hehexd@gmail.com',
        'Mynd':'frett2.jpg'
    },
{
        'Titill':'Özil skrifar undir nýja samning',
        'Grein':'Þýski landsliðsmaðurinn Mesut Özil hefur skrifað undir samning við Arsenal til 2021 en BBC greinir frá þessu.',
        'Netfang':'hehexd@gmail.com',
        'Mynd':'frett3.jpg'
    },
{
        'Titill':'Slimani fer á lán',
        'Grein':'Newcastle hefur fengið framherjann Islam Slimani á láni frá Leicester út tímabilið. Þar með lýkur leit Newcastle að nýjum framherja.',
        'Netfang':'hehexd@gmail.com',
        'Mynd':'frett4.jpg'
    }


]
@route('/frett/<numer>')
def frett(numer):
    return template('frettir',frettir[int(numer)])

@route('/')
def index():
    return template('verk3')

@route('/a')
def lidura():
    return template('lidura')

@route('/b')
def lidurb():
    return template('lidurb')

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('kt', kennitala=kennitala)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./myfiles')

@error(404)
def error404(error):
    return '<h1>Þessi síða er ekki til </h1>'

run(host='0.0.0.0',port=os.environ.get('PORT'))
