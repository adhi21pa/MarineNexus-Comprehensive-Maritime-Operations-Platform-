from flask import *
from database import *


crew=Blueprint('crew',__name__)

@crew.route('/crew_home')
def crew_home():
	return render_template('crew_home.html')



@crew.route('/crew_view_assign_ship', methods=['get', 'post'])
def crew_view_assign_ship():
    data = {}
   
    # Main query to retrieve flight details and packages
    q = """SELECT 
    fs.*, 
    aa.name AS fname, 
    ab.name AS tname, 
    s.ship_name, 
    s.latitude, 
    s.longitude, 
    c.company_name,  
    tb.package_id
FROM 
    ship_schedule fs
JOIN 
    ships s ON fs.ship_id = s.ship_id
JOIN 
    shipports aa ON fs.from_shipport_id = aa.shipport_id
JOIN 
    shipports ab ON fs.to__shipport_id = ab.shipport_id
LEFT JOIN 
    crew sa ON fs.ship_id = sa.ship_id
LEFT JOIN 
    company c ON s.company_id = c.company_id
INNER JOIN 
    ticketsbooked tb ON fs.schedule_id = tb.schedule_id  where
    sa.crew_id = '%s' GROUP BY s.ship_id
    
"""%(session['crew_id'])

    print("Final Query:", q)
    res = select(q)
    data['flighttime_id'] = res

    return render_template('crew_view_assign_ship.html', data=data)





@crew.route('/crewviewbpassager_details', methods=['get', 'post'])
def crewviewbpassager_details():
    data = {}
    package_id=request.args['sid']
    # Main query to retrieve flight details and packages
#     q = """SELECT * FROM `users` inner join `ticketsbooked` USING(`user_id`) WHERE `package_id`='%s'
# """%(package_id)
    q = """SELECT * FROM `users` INNER JOIN `ticketsbooked` USING(`user_id`)  INNER JOIN `ship_schedule` USING(`schedule_id`) INNER JOIN `ships` USING(`ship_id`) INNER JOIN `seats` USING(`ship_id`) WHERE `package_id`='%s' group by user_id
"""%(package_id)

    print("Final Query:", q)
    res = select(q)
    data['passengers'] = res

    return render_template('crewviewbpassager_details.html', data=data)



@crew.route('/crew_send_complaints',methods=['get','post'])
def crew_send_complaints():
	data={}
	q="SELECT * FROM `complaint` where login_id ='%s'"%(session['lid'])
	res=select(q)
	data['view']=res
    
	if 'submit' in request.form:
		com=request.form['com']
		q="INSERT INTO `complaint` VALUES(NULL,'%s','%s','pending',curdate(),'crew','%s')"%(session['lid'],com,session['com_id'] )
		insert(q)
		return redirect(url_for('crew.crew_send_complaints'))
	return render_template('crew_send_complaints.html',data=data)



@crew.route('/staffallocateseat',methods=['get','post']) 
def staffallocateseat():
	data={} 
	fid=request.args['fid']
	data['fid']=fid
	bid=request.args['bid']
	data['bid']=bid
	pid=request.args['pid']
	data['pid'] =pid
	pname=request.args['pname']
	data['names']=pname

	if 'actions' in request.args:
		action=request.args['actions'] 
		assignid=request.args['id'] 
	else:
		action=None 
	if action=="delete":
		q="delete from assignseat where assign_id='%s'" %(assignid)  
		delete(q)
		return redirect(url_for("crew.staffallocateseat",bid=bid,pid=pid,pname=pname,fid=fid))  
	
	if 'add' in request.form:
		# passengerid=request.form['passenger_id'] 
		seatid=request.form['seat_id'] 
		
		
	 
		q="insert into assignseat values(null,'%s','%s','accept')" %(pid,seatid)   
		insert(q) 
		return redirect(url_for('crew.crew_home',bid=bid,fid=fid)) 	
	q="SELECT *,CONCAT(`fname`,' ',`lname`)AS NAMES FROM assignseat INNER JOIN users USING(user_id) INNER JOIN seats USING(seat_id) WHERE `user_id`='%s'"%(pid)
	print(q)
	res=select(q)
	data['viewseats']=res  


	 	
	# q="select *,concat(fname,' ',lname) as names from users where booked_id='%s'" %(bid)	
	q="select *,concat(fname,' ',lname) as names from users"	
	res=select(q)
	data['assignseat']=res  

	q="SELECT * FROM `seats` INNER JOIN `type` USING(`type_id`) INNER JOIN `ships` USING(`ship_id`) WHERE `ship_id`='%s' and seat_id Not in(select assignseat.seat_id from assignseat inner join seats where ship_id='%s')"%(fid,fid)
	print("seat",q)
	res=select(q)
	print(res)
	data['viewseat']=res   
	return render_template('staffallocateseat.html',data=data) 

