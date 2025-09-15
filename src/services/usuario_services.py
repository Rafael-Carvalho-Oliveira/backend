from src import db
from ..models import usuario_model
from ..schemas import usuario_schema


def cadastrar_usuario(usuario):
    usuario_db = usuario_model.Usuario(nome = usuario.nome, email = usuario.email, telefone=usuario.telefone, senha = usuario.senha)
    # criptografa a senha
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

def listar_usuario():
    usuarios = usuario_model.Usuario.query.all()
    schema = usuario_schema.UsuarioSchema(many = True)
    return usuario_model.Usuario.query.all()

def listar_usuario_id(id):
    try:
        # buscar usuario
        usuario_encontrado = usuario_model.Usuario.query.get(id)
        return usuario_encontrado
    except Exception as e:
        print(f"Erros ao listar usuario por id {e}")
        return None

def excluir_usuario(id):
    usuario = usuario_model.Usuario.query.get(id)

    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    
    return False

def editar_usuario(id, novo_usuario):
    usuario = usuario_model.Usuario.query.get(id)
    if usuario:
        usuario.nome = novo_usuario.nome        
        usuario.email = novo_usuario.email        
        usuario.telefone = novo_usuario.telefone

        if novo_usuario.senha:
            usuario.gen_senha(novo_usuario.senha)

        db.session.commit()
        return usuario
    return None        

def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email = email).first()