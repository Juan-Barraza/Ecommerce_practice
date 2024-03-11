from flask import jsonify
from sqlite3 import Error
import sqlite3
import json


class ConnectionDb:
    
    
    def get_connection(self):
        
        try:
            con = sqlite3.connect("databese.db", check_same_thread=False)
            return con
        except Error as e:
            return jsonify({"Error": str(e)})
    
    
    def execute_query(self, con, query, params=None, fetch_all=False):
        try:
            cur = con.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            con.commit()
            if fetch_all is True:
                return cur.fetchall()
            else:
                return cur.fetchone()
        except Error as e:
             error_message = {"Error": str(e)}
             return json.dumps(error_message), 500 

conection = ConnectionDb()