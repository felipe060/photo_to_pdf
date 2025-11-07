import os


def verify_extension(**kwargs):             #function that verifies if the extension of the file the user uploaded, is within the allowed extensions
    from index import app
    import os
    import uuid

    upload_folder = app.config["UPLOAD_FOLDER"]
    nome_arquivo = kwargs["file_name"].filename
    arquivo = kwargs["file_name"]

    print("side_tasks.py nome_arquivo --> ", nome_arquivo)
    print("side_tasks.py nome_arquivo type --> ", type(nome_arquivo))
    print("")

    print("side_tasks.py arquivo -->", arquivo)
    print("side_tasks.py arquivo type -->", type(arquivo))
    print("")

    extensao_arquivo = os.path.splitext(nome_arquivo)[1]
    print("side_tasks.py extensao_arquivo -->", extensao_arquivo)
    print("")

    if extensao_arquivo in app.config["ALLOWED_EXTENSIONS"]:
        new_file_base_name = str(uuid.uuid4())
        print("side_tasks.py new_file_base_name -->", new_file_base_name)
        print("")

        new_file_name = str(new_file_base_name + extensao_arquivo)
        print("side_tasks.py new_file_name -->", new_file_name)
        print("side_tasks.py new_file_name type --> ", type(new_file_name))
        print("")

        file_path = os.path.join(upload_folder, new_file_name)
        print("side_tasks.py file_path -->", file_path)
        print("")

        arquivo.save(file_path)

        print(f"side_tasks.py file extension is allowed --> {extensao_arquivo}")
        print("")

        convert_to_pdf(image_name=new_file_name)
        return f"file extension is allowed --> {extensao_arquivo}"

    else:
        print(f"side_tasks.py file extension // not // allowed --> {extensao_arquivo}")
        return f"side_tasks.py file extension not allowed --> {extensao_arquivo}"


def convert_to_pdf(**kwargs):
    from img2pdf import convert

    image_name = kwargs["image_name"]
    print("side_tasks.py convert_to_pdf() image_name kwargs['image_name'] --> ", image_name)
    image = f"static/files/{image_name}"

    print("side_tasks.py convert_to_pdf() kwargs --> ", kwargs)
    print("")

    #print("image_converter.py asking /file_path/ to index.py")
    #print("file path image_converter.py -->", file_path)

    foto_convertida = convert(image)
    with open("static/files/output.pdf", "wb") as file:
        file.write(foto_convertida)

    ola = os.remove(f"static/files/{image_name}")
    print("side_tasks.py convert_to_pdf() ola -->", ola)
    return "foto convertida"
