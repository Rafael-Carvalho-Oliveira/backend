from src import db

class Agendamento(db.Model):
    __tablename__ = "tb_usuario"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dt_agendamento = db.Column(db.Datetime)
    dt_atendimento = db.Column(db.Datetime, nullable = False)
    User_idUser = db.Column(db.Integer, nullable = False)
    Servicos_idServicos = db.Column(db.Integer, nullable = False)
    Profissional_idProfissional = db.Column(db.Integer, nullable = False)
    
    def __init__(self, dt_agendamento, dt_atendimento, User_idUser, Servicos_idServicos, Profissional_idProfissional):
        self.dt_agendamento = dt_agendamento
        self.dt_atendimento = dt_atendimento
        self.User_idUser = User_idUser
        self.Servicos_idServicos = Servicos_idServicos
        self.Profissional_idProfissional = Profissional_idProfissional