from models import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
    CONNECTION = "sqlite:///teste_login.db"
    engine = create_engine(CONNECTION, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class Controller_cadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len (nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 100:
            return 3 
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_verficados = cls.verifica_dados(nome, email, senha)

        if dados_verficados != 1:
            return dados_verficados

        
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email, senha=senha)
            session.add(p1)
            session.commit()
            return 1

        except:
            return 3


class Controller_login():
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()
        if len(logado) == 1:
            return 'Usuário logado'
        else:
            return 'Senha ou email inválidos'




