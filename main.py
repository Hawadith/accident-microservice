import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash
		
@app.route('/add', methods=['POST'])
def add_report():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json 
        _ReportType = _json['type']
        _Location = _json['location']
        _Dateandtime = _json['dateTime']
        _Fee = _json['fee']
        _userID = _json['userID']
        # validate the received values
        if _ReportType and _Location and _Dateandtime and _Fee and _userID and  request.method == 'POST':
			# save edits
			sql = "INSERT INTO Accident(ReportType, Location, Dateandtime, FineFee, userID) VALUES(%s, %s, %s, %s, %s)"
			data = (_ReportType, _Location, _Dateandtime, _Fee, _userID,)
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Accident Report added successfully!')
			resp.status_code = 200
			return resp
        else:
			return not_found()
    except Exception as e:
		print(e)
    finally:
		cursor.close()
		conn.close()

@app.route('/accidents', methods=['GET'])
def accidents():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Accident")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/accidents/<int:id>', methods=['GET'])
def accident(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Accident WHERE AccidentID=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['POST'])
def update_accident():
    conn = mysql.connect()
    cursor = conn.cursor() 
    try:
        _json = request.json
        _id = _json['id']
        _ReportType = _json['type']
        _Location = _json['location']
        _Dateandtime = _json['dateTime']
        _Fee = _json['fee']
        _userID = _json['userID']
        # validate the received values
        if _ReportType and _Location and _Dateandtime and _Fee and _userID and _id and request.method == 'POST':
            # save edits
            sql = "UPDATE Accident SET ReportType=%s, Location=%s, Dateandtime=%s, FineFee=%s, userID=%s WHERE AccidentID=%s"
            data = (_ReportType, _Location, _Dateandtime, _Fee, _userID, _id,)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Accident Report updated successfully!')
            resp.status_code = 200
            return resp 
        else: 
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_report(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM Accident WHERE AccidentID=%s", (id,))
		conn.commit()
		resp = jsonify('Accident Report deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()

