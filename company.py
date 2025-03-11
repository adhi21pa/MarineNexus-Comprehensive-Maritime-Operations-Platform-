from flask import *
from database import *
import pandas as pd
import pickle
from bestprediction import *


company=Blueprint('company',__name__)

@company.route('/company_home')
def company_home():
	return render_template('company_home.html') 
@company.route('/companymanageships',methods=['get','post'])  
def companymanageships():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		flightid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from ships where ship_id='%s'" %(flightid)  
		delete(q)
		return redirect(url_for('company.companymanageships'))  
	if action=="update":
		q="select * from ships where ship_id='%s'" %(flightid) 
		res=select(q)
		data['updateship']=res 
	if 'update' in request.form:
		flight=request.form['flight']	
		noofseats=request.form['noofseats']  
		latitude=request.form['lat']  
		longitude=request.form['lon']  
		q="update ships set ship_name='%s', noofseats='%s',latitude='%s',longitude='%s' where ship_id='%s'" %(flight,noofseats,latitude,longitude,flightid)  
		update(q)
		return redirect(url_for('company.companymanageships')) 
	if 'add' in request.form:
		flight=request.form['flight']
		noofseats=request.form['noofseats'] 
		shiptype=request.form['shiptype'] 
		latitude=request.form['lat']  
		longitude=request.form['lon'] 
		q="insert into ships values(null,'%s','%s','%s','%s','%s',curdate(),'pending','%s')" %(session['company_id'] ,flight,noofseats,latitude,longitude,shiptype)     
		insert(q) 
		return redirect(url_for('company.companymanageships')) 
	q="select * from ships where company_id='%s'"%(session['company_id'])
	res=select(q) 
	data['flights']=res
	if res:
		session['ship_id'] = res[0]['ship_id']
	else:
		pass
	return render_template('companymanageships.html',data=data)  	

@company.route('/companymanageseats',methods=['get','post'])  	
def companymanageseats():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		seatid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from seats where seat_id='%s'" %(seatid)  
		delete(q)
		return redirect(url_for('company.companymanageseats'))  
	if action=="update":
		q="select * from seats where seat_id='%s'" %(seatid)  
		res=select(q)
		data['updateseats']=res 
		q1 = """
    SELECT 
        ship_status, 
        company_id, 
        ship_id, 
        ship_name, 
        noofseats,
        (ship_id='%s') AS sel 
    FROM 
        ships 
    WHERE 
        ship_status='verify' 
        AND company_id='%s' 
    ORDER BY 
        sel DESC, ship_id ASC
""" % (res[0]['ship_id'],session['company_id'])
		print(q1,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
		res1 = select(q1)

		data['updateship']=res1 
		q2="SELECT type_id,type,(type_id='%s') AS sel FROM type ORDER BY sel DESC,type_id ASC" %(res[0]['type_id'])  
		res2=select(q2) 
		data['updatetype']=res2
	if 'update' in request.form:
		typeid=request.form['type_id']	
		flightid=request.form['flight_id'] 
		seatno=request.form['seatno']  
		q="update seats set type_id='%s',ship_id='%s',seatno='%s' where seat_id='%s'" %(typeid,flightid,seatno,seatid)  
		update(q)
		return redirect(url_for('company.companymanageseats')) 
	if 'add' in request.form:
		typeid=request.form['type_id']
		flightid=request.form['flight_id']
		seatno=request.form['seatno'] 
		q="insert into seats values(null,'%s','%s','%s')" %(typeid,flightid,seatno)     
		insert(q) 
		return redirect(url_for('company.companymanageseats')) 
	q="select * from seats INNER JOIN ships using(ship_id) inner join type using(type_id) WHERE   ships.`company_id`='%s'"%(session['company_id'])  	 
	res=select(q) 
	data['seats']=res 	
	q="SELECT * FROM ships WHERE  `ship_status`='verify' AND `company_id`='%s'"%(session['company_id'])   
	res=select(q)
	data['flight_id']=res  
	q="select * from type"
	res=select(q)
	data['type_id']=res 
	return render_template('companymanageseats.html',data=data)  	

@company.route('/companymanagescheduleship',methods=['get','post'])  	
def companymanagescheduleship():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		scheduleid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from ship_schedule where schedule_id='%s'" %(scheduleid)  
		delete(q)
		return redirect(url_for('company.companymanagescheduleship'))  
	
	if 'add' in request.form:
		schedule=request.form['schedule']
		flightid=request.form['flight_id']
		fromairportid=request.form['from_airport_id']
		print(fromairportid,"uuuuuuuuuuuuuuuuu")
		toairportid=request.form['to_airport_id'] 
		print(toairportid,"tttttttttttttttttttt")
		startdatetime=request.form['start_date_time'] 
		enddatetime=request.form['end_date_time']
		if  fromairportid==toairportid:
			flash("From Ship Port and To Ship Port Are Same")
		else:
			
			q="insert into ship_schedule values(null,'%s','%s','%s','%s','%s','0','%s')" %(flightid,fromairportid,toairportid,startdatetime,enddatetime,schedule) 
			insert(q) 
			return redirect(url_for('company.companymanagescheduleship')) 
	# q="SELECT *,a1.`name` AS fname,a2.`name` AS tname FROM `ship_schedule` f,`shipports` a1,`shipports` a2,`ships` ff WHERE f.`ship_id`= ff.ship_id AND f.`from_shipport_id`=a1.`shipport_id` AND f.`to__shipport_id`=a2.`shipport_id` and ff.company_id = '%s'"% (session['company_id']) 
	query = """
    SELECT *,
           a1.name AS fname,
           a2.name AS tname
    FROM ship_schedule f
    JOIN shipports a1 ON f.from_shipport_id = a1.shipport_id
    JOIN shipports a2 ON f.to__shipport_id = a2.shipport_id
    JOIN ships ff ON f.ship_id = ff.ship_id
    WHERE ff.company_id =' %s'
"""%(session['company_id'])
	res=select(query) 
	data['ship_schedule']=res 	
	q="SELECT * FROM ships WHERE  `ship_status`='verify' AND `company_id`='%s'"%(session['company_id'])   
	res=select(q)
	data['flight_id']=res 
	q="select * from shipports" 
	res=select(q)
	data['to_airport_id']=res
	q="select * from shipports" 
	res=select(q)

	data['from_airport_id']=res 


	
	return render_template('companymanagescheduleship.html',data=data)  



@company.route('/company_manage_packages',methods=['get','post'])  	
def company_manage_packages():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		package_id=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from package where package_id='%s'" %(package_id)  
		delete(q)
		return redirect(url_for('company.company_manage_packages'))  
	
	if 'add' in request.form:
		schedule_id=request.form['schedule_id']
		bedroom_id=request.form['bedroom_details'].replace("'", "\\'")
		food_id=request.form['food_details'].replace("'", "\\'")
		pack_name=request.form['pack_name'].replace("'", "\\'")
		pack_details=request.form['pack_details'].replace("'", "\\'") 
		pack_amount=request.form['pack_amount']
		# if  fromairportid==toairportid:
		# 	flash("From Ship Port and To Ship Port Are Same")
		# else:
			
		q="insert into package values(null,'%s','%s','%s','%s','%s','%s')" %(schedule_id,bedroom_id,food_id,pack_name,pack_details,pack_amount) 
		insert(q) 
		return redirect(url_for('company.company_manage_packages')) 
	q="SELECT * FROM `ships` INNER JOIN `ship_schedule` USING(`ship_id`) WHERE  `company_id`='%s' "%( session['company_id'])
	res=select(q)
	data['schedule_id']=res
	# q="select * from bedrooms" 
	# res=select(q)

	# data['bedroom_id']=res 
	# q="select * from foods" 
	# res=select(q)

	# data['food_id']=res
	# q="SELECT * FROM `ships` INNER JOIN `ship_schedule` USING(`ship_id`) INNER JOIN `package` USING(`schedule_id`) INNER JOIN `bedrooms` USING(`bedroom_id`) INNER JOIN `foods` USING(`food_id`) where `company_id`='%s'"%(session['company_id'])   
	q="SELECT * FROM `ships` INNER JOIN `ship_schedule` USING(`ship_id`) INNER JOIN `package` USING(`schedule_id`) where `company_id`='%s'"%(session['company_id']) 
	print(q,"iii")
	res=select(q)
	data['pack_details']=res
	


	
	return render_template('company_manage_packages.html',data=data)  



import bcrypt

@company.route('/adminmanagestaff', methods=['GET', 'POST']) 
def adminmanagestaff(): 
    data = {}

    if 'action' in request.args:
        action = request.args['action'] 
        staffid = request.args['id'] 
        login_id = request.args['login_id'] 
    else:
        action = None

    if action == "delete":
        # Delete staff record
        q = "DELETE FROM staff WHERE staff_id='%s'" % (staffid)
        delete(q)
        # Delete corresponding login record
        q = "DELETE FROM login WHERE login_id='%s'" % (login_id)
        delete(q)
        return redirect(url_for('company.adminmanagestaff'))  

    if action == 'update':
        # Fetch staff details for updating
        qa = "SELECT * FROM staff WHERE staff_id='%s'" % (staffid)
        r2 = select(qa)
        data['upd'] = r2

    if 'update' in request.form:
        # Updating staff details
        fname = request.form['fname'] 
        lname = request.form['lname'] 
        gender = request.form['gender'] 
        age = request.form['age']
        phone = request.form['phone'] 
        email = request.form['email'] 
        designation = request.form['designation'] 
        qd = "UPDATE staff SET firstname='%s', lastname='%s', gender='%s', age='%s', phone='%s', email='%s', designation='%s' WHERE staff_id='%s'" % (
            fname, lname, gender, age, phone, email, designation, staffid)
        update(qd)
        return redirect(url_for('company.adminmanagestaff'))

    if 'submit' in request.form: 
        # Fetch form data for new staff member
        fname = request.form['fname'] 
        lname = request.form['lname'] 
        gender = request.form['gender'] 
        age = request.form['age']
        phone = request.form['phone'] 
        email = request.form['email'] 
        designation = request.form['designation'] 
        usern = request.form['username'] 
        passw = request.form['password']  

        # Check if username already exists
        qin = "SELECT * FROM login WHERE username='%s'" % usern
        ress = select(qin)
        if ress:
            flash("Sorry, the username already exists. Please choose another one.")
        else:
            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
            
            # Insert into login table with hashed password
            q = "INSERT INTO login (username, password, usertype) VALUES ('%s', '%s', 'captain')" % (
                usern, hashed_password.decode('utf-8'))     
            id = insert(q) 

            # Insert into staff table
            q = "INSERT INTO staff  VALUES (null,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                id, fname, lname, gender, age, phone, email, designation, session['company_id']) 
            insert(q)

            flash("Staff member added successfully.")
            return redirect(url_for('company.adminmanagestaff')) 

    # Fetch all staff members for the company
    q = "SELECT * FROM staff WHERE company_id='%s'" % (session['company_id'])
    print(q,"ppp")
    res = select(q)
    data['staff'] = res

    return render_template('adminmanagestaff.html', data=data)
 		
		
@company.route('/adminstaffallocate',methods=['get','post']) 
def adminstaffallocate():
	data={}  
	if 'action' in request.args:
		action=request.args['action'] 
		allocateid=request.args['id'] 
	else:
		action=None
	if action=="delete": 
		q="delete from staffallocate where allocate_id='%s'" %(allocateid) 
		delete(q) 
		return redirect(url_for('company.adminstaffallocate'))	

	if 'submit' in request.form: 
		staffid=request.form['staff_id'] 
		airportid=request.form['airport_id']
		shipport_id=request.form['shipport_id']
		qr="SELECT * FROM `staffallocate` WHERE `staff_id`='%s' AND `ship_id`='%s'"%(staffid,airportid)
		res=select(qr)
		if res:
			flash("already allocated")
		else:
			q="insert into staffallocate values(null,'%s','%s','accept','%s')" %(staffid,airportid,shipport_id)  
			print(q,"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
			insert(q) 
			return redirect(url_for('company.adminstaffallocate')) 

	

	q="select *,CONCAT(`firstname`,' ',`lastname`)as names from staffallocate INNER JOIN staff using(staff_id) INNER JOIN ships using(ship_id) where ships.company_id='%s'"%(session['company_id'] )   
	res=select(q) 
	print(res)
	data['allocate']=res   
	q="select *,CONCAT(`firstname`,' ',`lastname`)as names from staff where company_id='%s'" %(session['company_id']) 
	res=select(q) 
	data['staff_id']=res 
	q="select * from ships  WHERE  `ship_status`='verify' AND `company_id`='%s'"%(session['company_id'])   
	res=select(q)
	data['airport_id']=res  
	q="select * from shipports"
	res=select(q)
	data['shipport_id']=res 
	return render_template('adminstaffallocate.html',data=data)   



import bcrypt

@company.route('/company_manage_crew', methods=['POST', 'GET'])
def company_manage_crew():
    data = {}
    
    if 'submit' in request.form:
        crew_name = request.form['crew_name']
        crew_place = request.form['crew_place']
        crew_phone = request.form['crew_phone']
        crew_email = request.form['crew_email']
        username = request.form['username']
        password = request.form['password']
        shp_id = request.form['shp_id']

        # Check if the username or password already exists in the login table
        qc = "SELECT * FROM login WHERE username='%s'" % username
        ress = select(qc)
        if ress:
            flash("Username already exists")
        else:
            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # Insert into the login table with the hashed password
            qr = "INSERT INTO login (username, password, usertype) VALUES ('%s', '%s', 'crew')" % (username, hashed_password.decode('utf-8'))
            res = insert(qr)

            # Insert the new crew member into the crew table
            q = "INSERT INTO crew VALUES (null,'%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                res, crew_name, crew_place, crew_phone, crew_email, shp_id, session['company_id'])
            insert(q)
            return redirect(url_for('company.company_manage_crew'))
    
    # Fetch ships for selecting ship_id
    qn = "SELECT * FROM `ships` WHERE `ship_status`='verify'"
    data['ship_id'] = select(qn)
    
    # Fetch crew data with ship details
    qn = "SELECT * FROM `ships` INNER JOIN `crew` USING(`ship_id`) INNER JOIN login USING(login_id) WHERE crew.company_id='%s'" % (session['company_id'])
    data['view'] = select(qn)
    
    # Fetch ships for updating crew assignment
    qn = "SELECT * FROM `ships` WHERE `ship_status`='verify'"
    data['updateplace'] = select(qn)
    
    if 'action' in request.args:
        action = request.args['action']
        login_id = request.args['id']
    else:
        action = None

    # Action to block crew member
    if action == "block":
        q = "UPDATE `login` SET `usertype`='block' WHERE `login_id`='%s'" % (login_id)
        update(q)
        return redirect(url_for('company.company_manage_crew'))

    # Action to unblock crew member
    if action == "unblock":
        q = "UPDATE `login` SET `usertype`='crew' WHERE `login_id`='%s'" % (login_id)
        update(q)
        return redirect(url_for('company.company_manage_crew'))

    # Action to update crew member's ship assignment
    if action == "update":
        q = "SELECT * FROM `ships` INNER JOIN `crew` USING(`ship_id`) WHERE `login_id`='%s'" % (login_id)
        data['up'] = select(q)
    
    # Update crew member's ship assignment
    if 'update' in request.form:
        ship_id = request.form['ship_id']
        q = "UPDATE `crew` SET `ship_id`='%s' WHERE `login_id`='%s'" % (ship_id, login_id)
        update(q)
        return redirect(url_for('company.company_manage_crew'))

    return render_template('company_manage_crew.html', data=data)







@company.route('/company_booked_package', methods=['get', 'post']) 
def company_booked_package():
    data = {}
    bid = request.args['bid'] 
    package_id = request.args['package_id']  # Corrected indentation here
    q = "SELECT * FROM  `ticketsbooked`  inner join  `package` USING(`package_id`)  WHERE `booked_id`='%s'" % (bid)
    print("seat", q)
    res = select(q)
    print(res)
    data['packages'] = res   
    return render_template('company_booked_package.html', data=data)




@company.route('/company_viewticketsbooked',methods=['get','post'])
def company_viewticketsbooked():
	data={}
	if 'bid' in request.args:

		bid=request.args['bid']
		fid=request.args['fid']
		q="update ticketsbooked set booked_status='Approve' where booked_id='%s'" %(bid)
		update(q)
		return redirect(url_for('staff.staffviewticketsbooked'))
	q = "SELECT `ticketsbooked`.*, `ship_schedule`.*,ships.*, `from_airport`.`name` AS `from_airport_name`, `to_airport`.`name` AS `to_airport_name` FROM ticketsbooked INNER JOIN ship_schedule USING(schedule_id)INNER JOIN `shipports` AS `from_airport` ON `ship_schedule`.`from_shipport_id` = `from_airport`.`shipport_id` INNER JOIN `shipports` AS `to_airport` ON `ship_schedule`.`to__shipport_id` = `to_airport`.`shipport_id`  INNER JOIN ships USING(ship_id)  WHERE `company_id`='%s'"%(session['company_id'])
	res=select(q)
	data['ticketsbooked']=res 	
	return render_template('company_viewticketsbooked.html',data=data)










@company.route('/compnay_complaints',methods=['get','post'])
def compnay_complaints():
    data={}
    q="SELECT * FROM `complaint` INNER JOIN `crew` USING(`login_id`) WHERE `complaint`.`company_id`='%s' AND `send_type`='crew'"%(session['company_id'])
    res=select(q)
    data['view']=res
    j=0
    for i in range(1,len(res)+1):
        if 'submit' +str(i) in request.form:
            reply=request.form['reply'+str(i)]
            q="UPDATE `complaint` SET `reply`='%s' WHERE `complaint_id`='%s' "%(reply,res[j]['complaint_id'])
            update(q)
            flash('success')
            return redirect(url_for('company.compnay_complaints'))
        j=j+1
    return render_template('compnay_complaints.html',data=data)
@company.route('/ship_performace_prediction', methods=['get', 'post'])
def ship_performace_prediction():
    data = {}
    id=request.args['id']
    engine_efficiency = None
    efficiency_details = None

    if request.method == 'POST' and 'add' in request.form:
        # Collect data from the form
        shipno = request.form['ship_id']
        ship_type = request.form['ship_type']
        route_id = request.form['route_id']
        month = request.form['month']
        distance = float(request.form['distance'])
        fuel_type = request.form['fuel_type']
        fuel_consumption = float(request.form['fuel_consumption'])
        CO2_emissions = float(request.form['CO2_emissions'])
        weather_conditions = request.form['weather_conditions']

        # Create DataFrame for input data
        input_data = {
            "ship_id": shipno,
            "ship_type": ship_type,
            "route_id": route_id,
            "month": month,
            "distance": distance,
            "fuel_type": fuel_type,
            "fuel_consumption": fuel_consumption,
            "CO2_emissions": CO2_emissions,
            "weather_conditions": weather_conditions
        }

        df_input = pd.DataFrame([input_data])

        # Load original dataset structure to perform the one-hot encoding
        data = pd.read_csv("ship_fuel_efficiency.csv")
        data = pd.get_dummies(data, columns=['ship_id', 'ship_type', 'route_id', 'month',
                                             'distance', 'fuel_type', 'fuel_consumption',
                                             'CO2_emissions', 'weather_conditions'])

        df_input = pd.get_dummies(df_input, columns=['ship_id', 'ship_type', 'route_id', 'month',
                                                     'distance', 'fuel_type', 'fuel_consumption',
                                                     'CO2_emissions', 'weather_conditions'])

        # Align input data with the trained model's features
        df_input = df_input.reindex(columns=data.columns.drop('engine_efficiency'), fill_value=0)

        # Predict engine efficiency
        engine_efficiency = model.predict(df_input)[0]

        # Determine efficiency details based on the predicted engine efficiency
        if engine_efficiency >= 85:
            efficiency_details = "Efficient"
        elif engine_efficiency >= 80:
            efficiency_details = "Semi-efficient"
        else:
            efficiency_details = "Not efficient"

        # Prepare the SQL query
        query = """
        INSERT INTO prediction (`prediction_id`, `shipno`, `ship_type`, `route_id`, `month`,
        `distance`, `fuel_type`, `fuel_consumption`, `CO2_emissions`, `weather_conditions`,
        `engine_efficiency`, `efficiency_details`,`ship_id`)
        VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')
        """ % (shipno, ship_type, route_id, month, distance, fuel_type,
               fuel_consumption, CO2_emissions, weather_conditions, engine_efficiency, efficiency_details,id)
        insert(query)

    return render_template('ship_performace_prediction.html', engine_efficiency=engine_efficiency, efficiency_details=efficiency_details)



@company.route('/company_view_mechanics',methods=['get','post']) 
def company_view_mechanics():
	data={}
	ship_id=request.args['ship_id'] 
	qr="select * from ships where ship_id='%s'"%(ship_id)
	print(qr)
	res=select(qr)
	val=res[0]['ship_id']
	data['shp']=val
	
	if 'action' in request.args:
		action=request.args['action'] 
		typeid=request.args['id']

	else:
		action=None
	if action=="assign":
		q="INSERT INTO `work_assign` VALUES(NULL,'%s','%s','pending')" %(val,typeid)
		print(q,"9999999999999999999999999999999999")

		insert(q)
		return redirect(url_for('company.company_home',ship_id=ship_id)) 
	
	q="SELECT * FROM mechanics where company_id='%s'"%(session['company_id'])
	res=select(q) 
	print(q,"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
	data['type']=res 
	print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
	return render_template('company_view_mechanics.html',data=data,ship_id=ship_id) 





import bcrypt

@company.route('/admin_manage_mechanic', methods=['get', 'post'])
def admin_manage_mechanic():
    data = {}

    if 'action' in request.args:
        action = request.args['action']
        typeid = request.args['id']
    else:
        action = None

    # Action to delete the mechanic user
    if action == "delete":
        q = "UPDATE `login` SET `usertype`='pending' WHERE `login_id`='%s'" % (typeid)
        delete(q)
        return redirect(url_for('admin.admin_manage_mechanic'))

    # Action to allow the mechanic user
    if action == "allow":
        q = "UPDATE `login` SET `usertype`='mechanic' WHERE `login_id`='%s'" % (typeid)
        delete(q)
        return redirect(url_for('admin.admin_manage_mechanic'))

    # Action to update mechanic details
    if action == "update":
        q = "SELECT * FROM mechanics WHERE login_id='%s'" % (typeid)
        res = select(q)
        data['updatecompany'] = res

    # If the update form is submitted
    if 'update' in request.form:
        mech_name = request.form['company_name']
        mech_place = request.form['company_place']
        mech_phone = request.form['company_phone']
        mech_email = request.form['company_email']
        mech_address = request.form['company_address']
        q = "UPDATE mechanics SET mech_name='%s', mech_place='%s', mech_phone='%s', mech_email='%s', mech_address='%s' WHERE login_id='%s'" % (
            mech_name, mech_place, mech_phone, mech_email, mech_address, typeid)
        update(q)
        return redirect(url_for('company.admin_manage_mechanic'))

    # If the add form is submitted
    if 'add' in request.form:
        mech_name = request.form['company_name']
        mech_place = request.form['company_place']
        mech_phone = request.form['company_phone']
        mech_email = request.form['company_email']
        mech_address = request.form['company_address'].replace("'", "\\'")
        username = request.form['username']
        password = request.form['password']

        # Check if the username or password already exists in the login table
        qc = "SELECT * FROM login WHERE username='%s'" % username
        ress = select(qc)
        if ress:
            flash("Username already exists. Please try again with a different one.")
        else:
            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Insert into the login table with the hashed password
            qr = "INSERT INTO login (username, password, usertype) VALUES ('%s', '%s', 'mechanic')" % (
                username, hashed_password.decode('utf-8'))
            res = insert(qr)

            # Insert the new mechanic details into the mechanics table
            q = "INSERT INTO mechanics  VALUES (null,'%s', '%s', '%s', '%s', '%s', '%s',curdate(), '%s')" % ( res, mech_name, mech_place, mech_phone, mech_email, mech_address, session['company_id'])
            insert(q)

            return redirect(url_for('company.admin_manage_mechanic'))

    # Fetch all mechanics for the current company
    q = "SELECT * FROM mechanics INNER JOIN login USING(login_id) WHERE company_id='%s'" % (session['company_id'])
    res = select(q)
    data['type'] = res

    return render_template('admin_manage_mechanic.html', data=data)



@company.route('/compny_view_assigned_work',methods=['get','post']) 
def compny_view_assigned_work():
	data={}
	
	q="SELECT * FROM `mechanics` INNER JOIN  `work_assign` USING(`mechanic_id`) INNER JOIN `ships` USING(`ship_id`) INNER JOIN `prediction` ON `prediction`.`ship_id`=`ships`.`ship_id` WHERE `ships`.`company_id`='%s' ORDER BY `work_assign`.`work_assign_id` DESC"%(session['company_id']) 	
	res=select(q) 
	print(q,"xxxxx")
	data['type']=res 
	print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
	return render_template('compny_view_assigned_work.html',data=data) 



@company.route('/compnay_view_paymet_work',methods=['get','post']) 
def compnay_view_paymet_work():
	data={}
	work_id=request.args['work_id']
	q="SELECT * FROM `work_payment`  INNER JOIN `work_assign` USING(`work_assign_id`) WHERE `work_assign_id`='%s'"%(work_id) 	
	res=select(q) 
	print(q,"xxxxx")
	data['type']=res 
	print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
	return render_template('compnay_view_paymet_work.html',data=data) 




@company.route('/companymakepayment',methods=['get','post']) 
def companymakepayment():		
	data={}
	amt=request.args['amount']
	data['amt']=amt


	bid=request.args['bid']  
	data['bid']=bid
	ship_id=request.args['ship_id']  
	data['bid']=bid
	amount=request.args['amount']
	data['amount']=amount

	action=request.args['action']

	if 'submit' in request.form:
		q="insert into payments values(null,'%s','%s',curdate())" %(bid,amount)
		insert(q)

		q="update ships set ship_status='verify' where ship_id='%s'" %(ship_id)
		update(q)
		q="update work_assign set work_status='Paid' where work_assign_id='%s'" %(ship_id)
		update(q)


		return '''<script>alert('Payment Successful');window.location='/company/company_home'</script>'''
	
	return render_template('make_payment.html',data=data)   
@company.route('/compnay_view_the_cargo',methods=['get','post']) 
def compnay_view_the_cargo():
	data={}
	q = "SELECT `users`.*, `cargo_details`.*, `ship_schedule`.*,ships.*, `from_airport`.`name` AS `from_airport_name`, `to_airport`.`name` AS `to_airport_name` FROM  `users` INNER JOIN `cargo_details` USING(`user_id`) INNER JOIN ship_schedule USING(schedule_id)INNER JOIN `shipports` AS `from_airport` ON `ship_schedule`.`from_shipport_id` = `from_airport`.`shipport_id` INNER JOIN `shipports` AS `to_airport` ON `ship_schedule`.`to__shipport_id` = `to_airport`.`shipport_id`  INNER JOIN ships USING(ship_id) WHERE `company_id`='%s' order by `cargo_id` DESC"%(session['company_id'])
	print(q,"yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
	res=select(q)
	data['ticketsbooked']=res 
	if 'action' in request.args:
		action=request.args['action']
		bid=request.args['bid']
	else:
		action=None
	if action=='accept':
		q="update cargo_details set cargo_status='accept' where cargo_id='%s'" %(bid)
		update(q)
		return '''<script>alert('Cargo Accept Successful');window.location='/company/compnay_view_the_cargo'</script>'''
	
	if action=='delivered':
		q="update cargo_details set cargo_status='delivered' where cargo_id='%s'" %(bid)
		update(q)
		return '''<script>alert('CCargo Delivered Successful');window.location='/company/compnay_view_the_cargo'</script>'''
	

 
	return render_template('compnay_view_the_cargo.html',data=data) 