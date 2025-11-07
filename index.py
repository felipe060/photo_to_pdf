from flask import Flask, render_template, url_for, request, send_from_directory
import os

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(413)                              #verifica o tamanho do arquivo
def request_too_large(error):                       #se ele for maior doq o MAX_CONTENT_LENGTH, o resto do codigo nem vai ser executado
    return ("file size exceeds maximum of 50Mb "
            "<br>"
            "arquivo maior doq o limite de 50Mb permitido")


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():

    print("index.py request.files -->", request.files)                   #imprime o dicionario do request
    print("")

    if "name_image" not in request.files:                       #se o arquivo nomeado "name_image" no html n tiver no request.files
        print("no files were sent in the request\n"             #imprime no terminal esse texto dizendo q o arquivo n ta la
              "nenhum arquivo foi enviado na requisicao\n")
        return ("none file was sent in request <br> "           #e retorna pro usuario dizendo q n tem nenhuma arquivo na requisicao
                "nenhum arquivo foi enviado na requisicao")

    file = request.files["name_image"]                          #armazena numa variavel o arquivo que o usuario fez o upload
    print("index.py file-->", file)                             #imprime no terminal essa variavel
    print("")

    if file.filename == "":                                                 #se o arquivo que armazenamos na variavel ali em cima, for uma string vazia
        print("empty filename // filename is a empty string\n"              #dai imprime no terminal q o nome do arquivo ta como string vazia
              "filename vazio // filename esta como uma string vazia")
        return "empty filename <br> filename vazio"                         #e retorna pro usuario dizendo que o nome do arquivo ta vazio

    if file:                                                                #se a variavel "file" retorna True, ou seja, ela existe e n ta como string vazio
        file.seek(0, 2)
        tamanho = file.tell()
        file.seek(0)
        print("index.py tamanho -->", tamanho, "bytes")
        print("")

        from side_tasks import verify_extension
        verify_extension(file_name=file)

        return send_from_directory("temp", "output.pdf", as_attachment=True)
        #return render_template("send_back.html")


if __name__ == "__main__":
    app.run()
