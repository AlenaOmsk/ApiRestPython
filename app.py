app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
ma = Marshmallow(app)

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)   

    class ResultSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email')

result_schema = ResultSchema()
results_schema = ResultSchema(many=True)
