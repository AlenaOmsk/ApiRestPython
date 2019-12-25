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

#Insert
@app.route("/user", methods=['POST'])
def AddUser():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    new_user = Result(name, email, password)
    db.session.add(new_user)
    db.session.commit()

    return result_schema.jsonify(new_user)
#Get all
@app.route("/users", methods=['GET'])
def GetUsers():
    all_results = Result.query.all()
    results = results_schema.dump(all_results)
    return jsonify(results)
#Get by id
@app.route("/user/<id>", methods=['GET'])
def GetUserByID(id):
    result = Result.query.get(id)
    return result_schema.jsonify(result)

#Update user by ID
@app.route("/user/<id>", methods=['PUT'])
def UpdateUser(id):
    result = Result.query.get(id)

    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    result.name = name
    result.email = email
    result.password = password

    db.session.commit()
    return result_schema.jsonify(result)        
#Delete user by ID
@app.route("/user/<id>", methods=['DELETE'])
def DeleteUser(id):
    result = Result.query.get(id)

    db.session.delete(result)
    db.session.commit()

    return result_schema.jsonify(result)

if __name__ == '__main__':
    app.run()
