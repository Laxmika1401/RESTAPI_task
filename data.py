import pymysql,os,json
file = os.path.abspath("data.json")
json_data = open(file).read()
json_obj = json.loads(json_data)
def validate_string(val):
    if val != None:
        return str(val).encode('utf-8')
    else:
        return val

conn = pymysql.connect(host = "localhost", user = "root" , passwd = "laxmika" , db = "tva_data")
mycur = conn.cursor()
for i,item in enumerate(json_obj):
    id = validate_string(item.get('id',None))
    first_name = validate_string(item.get('first_name',None))
    last_name = validate_string(item.get('last_name',None))
    company = validate_string(item.get('company_name',None))
    city = validate_string(item.get('city',None))
    state = validate_string(item.get('state',None))
    zip = validate_string(item.get('zip',None))
    email = validate_string(item.get('email',None))
    web = validate_string(item.get('web',None))
    age = validate_string(item.get('age',None))
    
    mycur.execute("INSERT INTO tva_app_tva_table(id,first_name,last_name,company,city,state,zip,email,web,age) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,first_name,last_name,company,city,state,zip,email,web,age))
conn.commit()
conn.close()