from flask import jsonify
from sqlite3 import Error
import sqlite3


class ConnectionDb:
    
    
    def get_connection(self):
        
        try:
            con = sqlite3.connect("databese.db", check_same_thread=False)
            return con
        except Error as e:
            return jsonify({"Error": str(e)})
    
    
    def execute_query(self, con, query, params=None, fetch_all = False):
        try:
            cur = con.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            con.commit()
            if fetch_all:
                return cur.fectchall()
            else:
                return cur.fetchone() if cur.rowcount > 0 else None
            
        except Error as e:
            return jsonify({"Error": str(e)})

    def fetch_all_rows(self,cur):
        
        try:
            return cur.fetchall()
        except Error as e:
            return jsonify({"Error": str(e)})
        
    def fetch_one(self,cur):
        try:
            return cur.fetchone()
        except Error as e:
            return jsonify({"Error": str(e)})

conection = ConnectionDb()