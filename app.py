from flask import Flask, render_template, request, redirect


app = Flask(__name__)
class cadInfluencers:
    def __init__(self,nome,plataforma,seguidores,areas):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.areas = areas

lista=[]

@app.route('/Influenciadores')
def pokemon():
    return render_template(' Influenciadores.html',Titulo = "Cadastro de Influenciadores Digitais:",ListaInfluenciadores = lista)

@app.route('/Cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de  Influenciadores")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    areas = request.form['areas']
    obj =cadInfluencers(nome,plataforma,seguidores,areas)
    lista.append(obj)
    return redirect('/Influenciadores')

@app.route('/excluir/<nomeinflu>', methods=['GET','DELETE'])
def excluir(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            lista.pop(i)
            break
    return redirect('/Influenciadores')

@app.route('/editar/<nomeinflu>', methods=['GET'])
def editar(nomeinflu):
    for i, Influ in enumerate(lista):
        if Influ.nome == nomeinflu:
            return render_template('Editar.html', Influencer = Influ, titulo="Alterar influencer")

@app.route('/alterar', methods=['POST', "PUT"])
def alterar():
    nome = request.form['nome']
    for i, influ in enumerate(lista): # o request acessa as informações do formulário
        if influ.nome == nome:
            influ.nome = request.form['nome']
            influ.plataforma = request.form['plataforma']
            influ.seguidores = request.form['seguidores']
            influ.areas = request.form['areas']
    return  redirect('/Influenciadores')


if __name__ == '__main__':
    app.run()
