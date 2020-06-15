from flask_restful import Resource, reqparse
from db import query

class Emp(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('empno', type = int, required = True, help = 'empno cannot be left blank')
        data = parser.parse_args()
        print(data)
        try:
            return query(f"""SELECT * FROM testapi.emp WHERE empno = {data['empno']};""")
        except:
            return {"message" : "there was an error connecting to emp table"},500

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('empno', type = int, required = True, help = 'empno cannot be left blank')
        parser.add_argument('ename', type = str, required = True, help = 'ename cannot be left blank')
        parser.add_argument('job', type = str, required = True, help = 'job cannot be left blank')
        parser.add_argument('mgr', type = int, required = True, help = 'mgr cannot be left blank')
        parser.add_argument('hiredate', type = str, required = True, help = 'hiredate cannot be left blank')
        parser.add_argument('sal', type = str, required = True, help = 'sal cannot be left blank')
        parser.add_argument('comm', type = str)
        parser.add_argument('deptno', type = int, required = True, help = 'deptno cannot be left blank')
        parser.add_argument('pass', type = str, required = True, help = 'pass cannot be left blank')

        data = parser.parse_args()

        try:
            x = query(f"""SELECT * FROM testapi.emp WHERE empno = {data['empno']}""", return_json = False)
            if len(x) > 0:
                return {"message":"empno already exists"},400
        except:
            return {"message":"error inserting into emp"}
            
        try:
            query(f"""INSERT INTO testapi.emp VALUES (
                                                            {data['empno']},
                                                            '{data['ename']}',
                                                            '{data['job']}',
                                                            {data['mgr']},
                                                            '{data['hiredate']}',
                                                            '{data['sal']}',
                                                            '{data['comm']}',
                                                            {data['deptno']},
                                                            '{data['pass']}'
                                                            )"""
                                                            )
        except:
            return {"message":"there was an error inserting into the table"},500
        
        return {"message":"successfully inserted."},201