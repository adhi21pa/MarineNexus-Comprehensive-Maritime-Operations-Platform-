/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - python_ship_reservation_system
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`python_ship_reservation_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `python_ship_reservation_system`;

/*Table structure for table `assignseat` */

DROP TABLE IF EXISTS `assignseat`;

CREATE TABLE `assignseat` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `passengers_id` int(11) DEFAULT NULL,
  `seat_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `assignseat` */

insert  into `assignseat`(`assign_id`,`passengers_id`,`seat_id`,`status`) values 
(7,2,10,'accept'),
(3,3,9,'accept'),
(4,4,11,'accept'),
(5,1,9,'pending'),
(6,1,11,'pending'),
(8,3,13,'pending'),
(9,4,2,'pending'),
(10,4,2,'pending'),
(11,4,1,'pending'),
(12,4,3,'pending');

/*Table structure for table `bedrooms` */

DROP TABLE IF EXISTS `bedrooms`;

CREATE TABLE `bedrooms` (
  `bedroom_id` int(11) NOT NULL AUTO_INCREMENT,
  `bedroom_name` varchar(100) DEFAULT NULL,
  `bed_type` varchar(100) DEFAULT NULL,
  `details` text,
  PRIMARY KEY (`bedroom_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `bedrooms` */

insert  into `bedrooms`(`bedroom_id`,`bedroom_name`,`bed_type`,`details`) values 
(2,'new Bed room','single bedroom','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '),
(3,'Bedroom 2','double Bed room','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '),
(4,'bedroom 3','family bed room ','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '),
(5,'bedroom 4','famiy with extra bed','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been ');

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `company_place` varchar(100) DEFAULT NULL,
  `company_phone` varchar(100) DEFAULT NULL,
  `company_email` varchar(100) DEFAULT NULL,
  `company_address` varchar(1000) DEFAULT NULL,
  `company_join_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `company` */

insert  into `company`(`company_id`,`login_id`,`company_name`,`company_place`,`company_phone`,`company_email`,`company_address`,`company_join_date`) values 
(1,10,'canvas','kollam','7894561231','ss@gmail.com','amhbcads\r\nasdjhasvdhmayyyyy','2025-02-05'),
(2,11,'new comapny','kochi','789456123055','RR2@gmail.com','dcbdcfbfcr\r\nscbdchjdfc','2025-02-05'),
(3,12,'liya company','trissure','5285858585','rr@gmail0.com','dcbsdhdjew\r\nmcbhdshmcjdsk\r\nsjchds','2025-02-05');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `complaint` text,
  `reply` text,
  `datetime` varchar(10) DEFAULT NULL,
  `send_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`login_id`,`complaint`,`reply`,`datetime`,`send_type`) values 
(2,18,'sdjwed,hwee','pending','2025-02-10','crew'),
(3,18,'smqwdkwq','pending','2025-02-10','crew');

/*Table structure for table `countries` */

DROP TABLE IF EXISTS `countries`;

CREATE TABLE `countries` (
  `country_id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `countries` */

insert  into `countries`(`country_id`,`country`) values 
(1,'Qatar'),
(2,'India'),
(3,'china'),
(6,'Dubai');

/*Table structure for table `crew` */

DROP TABLE IF EXISTS `crew`;

CREATE TABLE `crew` (
  `crew_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `crew_name` varchar(100) DEFAULT NULL,
  `crew_place` varchar(100) DEFAULT NULL,
  `crew_phone` varchar(100) DEFAULT NULL,
  `crew_email` varchar(100) DEFAULT NULL,
  `ship_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`crew_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `crew` */

insert  into `crew`(`crew_id`,`login_id`,`crew_name`,`crew_place`,`crew_phone`,`crew_email`,`ship_id`,`company_id`) values 
(1,18,'fewfe','fsdfefe','8784558484','uu@gmail.com',2,4);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values 
(1,1,'good','2021-01-31 00:18:11'),
(2,1,'good customer service','2021-02-11 15:00:36'),
(3,4,'zxc,nscvsdj','2025-02-06 23:51:23');

/*Table structure for table `flight_schedule` */

DROP TABLE IF EXISTS `flight_schedule`;

CREATE TABLE `flight_schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `from_shipport_id` int(11) DEFAULT NULL,
  `to__shipport_id` int(11) DEFAULT NULL,
  `start_date_time` varchar(100) DEFAULT NULL,
  `end_date_time` varchar(100) DEFAULT NULL,
  `t_amount` varchar(20) DEFAULT NULL,
  `shedule_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `flight_schedule` */

insert  into `flight_schedule`(`schedule_id`,`ship_id`,`from_shipport_id`,`to__shipport_id`,`start_date_time`,`end_date_time`,`t_amount`,`shedule_name`) values 
(2,2,11,8,'2025-02-14T00:09','2025-02-23T00:09','0','new travel ship');

/*Table structure for table `flighttiming` */

DROP TABLE IF EXISTS `flighttiming`;

CREATE TABLE `flighttiming` (
  `flighttime_id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `airport_id` int(11) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`flighttime_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `flighttiming` */

insert  into `flighttiming`(`flighttime_id`,`schedule_id`,`airport_id`,`time`,`type`) values 
(1,3,3,'16:15:38','departure'),
(2,3,3,'16:16:13','arrival'),
(3,2,11,'14:09:38','departure'),
(4,2,11,'14:09:42','arrival');

/*Table structure for table `foods` */

DROP TABLE IF EXISTS `foods`;

CREATE TABLE `foods` (
  `food_id` int(11) NOT NULL AUTO_INCREMENT,
  `food_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`food_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `foods` */

insert  into `foods`(`food_id`,`food_name`) values 
(2,'biriyanis'),
(3,'chiken'),
(4,'mutton');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'manju','manju','staff'),
(3,'radhu','radhu','pending'),
(4,'radhu','radhu','pending'),
(5,'athira','athirakm45','staff'),
(6,'karthika','karthika','staff'),
(7,'vacoviwyc','1234','users'),
(9,'liyaann','Liyaantony@23','users'),
(10,'asdhgd','sdjfghfm@#mjndfj','company'),
(11,'hscdsfbc','sdjfhds88#hnbdn','company'),
(12,'li','li','company'),
(16,'cap','cap','staff'),
(14,'chbdchdbmcjds','kxjsakx7@hnbxcd','mechanic'),
(15,'tsagxasxvas','uu@gmailsdhb$','mechanic'),
(18,'crew','crew','crew');

/*Table structure for table `luggage_info` */

DROP TABLE IF EXISTS `luggage_info`;

CREATE TABLE `luggage_info` (
  `luggage_id` int(11) NOT NULL AUTO_INCREMENT,
  `booked_id` int(11) DEFAULT NULL,
  `total_weight` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`luggage_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `luggage_info` */

insert  into `luggage_info`(`luggage_id`,`booked_id`,`total_weight`,`details`,`status`) values 
(1,2,'32 kg','bags','approve');

/*Table structure for table `mechanics` */

DROP TABLE IF EXISTS `mechanics`;

CREATE TABLE `mechanics` (
  `mechanic_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `mech_name` varchar(100) DEFAULT NULL,
  `mech_place` varchar(100) DEFAULT NULL,
  `mech_phone` varchar(100) DEFAULT NULL,
  `mech_email` varchar(100) DEFAULT NULL,
  `mech_address` text,
  `mech_join_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mechanic_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `mechanics` */

insert  into `mechanics`(`mechanic_id`,`login_id`,`mech_name`,`mech_place`,`mech_phone`,`mech_email`,`mech_address`,`mech_join_date`) values 
(1,14,'santhosh mechs','kollam','7894561230','ss@gmail.com','chbdddnmc\r\nsdshbhde\r\ncjd','2025-02-05'),
(2,15,'mech shaji','kochi','7894561230','yy@gmail.com','ttttttttt\r\nrfjrfr\r\nferf','2025-02-05');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`message_id`,`sender_id`,`receiver_id`,`message`,`reply`) values 
(1,3,2,'hiii\r\n','hi'),
(2,3,2,'zsxcszCszczs czxd cxc ','fsdfsdfvdsfv');

/*Table structure for table `package` */

DROP TABLE IF EXISTS `package`;

CREATE TABLE `package` (
  `package_id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `bedroom_id` int(11) DEFAULT NULL,
  `food_id` int(11) DEFAULT NULL,
  `pack_name` varchar(100) DEFAULT NULL,
  `pack_details` text,
  `pack_amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`package_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `package` */

insert  into `package`(`package_id`,`schedule_id`,`bedroom_id`,`food_id`,`pack_name`,`pack_details`,`pack_amount`) values 
(1,2,2,2,'this is a new cruis pacakge','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the ','2500'),
(2,2,3,3,'cruis package ','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the ','6000'),
(3,2,4,4,'fivre starpacjagr','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the ','7000'),
(4,2,5,2,'ttttttttttttttttt','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the ','3500');

/*Table structure for table `passengers` */

DROP TABLE IF EXISTS `passengers`;

CREATE TABLE `passengers` (
  `passengers_id` int(11) NOT NULL AUTO_INCREMENT,
  `booked_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `passport_no` varchar(100) DEFAULT NULL,
  `validity_date` varchar(100) DEFAULT NULL,
  `image1` varchar(250) DEFAULT NULL,
  `image2` varchar(250) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`passengers_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `passengers` */

insert  into `passengers`(`passengers_id`,`booked_id`,`first_name`,`last_name`,`phone`,`email`,`dob`,`gender`,`house_name`,`place`,`country`,`passport_no`,`validity_date`,`image1`,`image2`,`status`,`user_id`) values 
(1,1,'Radhu','K','9444467784','radhu6777@gmail.com','2014-12-05','Female','kfhfhh','Ernakulam','India','5788889786 ','2021-02-02','static/uploadimages/d1ff3db8-afbc-4e9a-9ace-7b615894f2f9de module 2.JPG','static/uploadimages/ebfc1cdc-d316-4862-9def-f88dbbbb7875r1.JPG','pending',4),
(2,2,'Radhu','K','9444467784','radhu6777@gmail.com','1984-02-02','Female','Madathil house','Trivandrum','India','A2096457','2022-01-31','static/uploadimages/8335b832-69bf-4a14-82d2-a6db1dee4b73re.JPG','static/uploadimages/afaf5d11-c09b-481d-b6be-31b5082bbc1fr2.JPG','approve',NULL),
(3,4,'Malavika','S','8452311905','malavikass2375@gmail.com','1980-04-09','Female','Madathil house','Trivandrum','India','A5095672','2021-12-31','static/uploadimages/7f3d5302-134c-4928-9f37-7b3dab94ae82dedekind,orde.JPG','static/uploadimages/e69a3d44-7de8-4467-96c3-71f1506e0c1fdedekinds prop.JPG','approve',NULL),
(4,3,'Anamika','K','6483400268','anamika6348@gmail.com','1997-09-09','Female','Thekedath House','Trivandrum','India','B2378214','2022-02-28','static/uploadimages/8cc3f613-9562-4e21-899f-bb55884d72ffded1.JPG','static/uploadimages/c1a72832-1215-462f-8c7d-31e1b2b63112r2.JPG','approve',NULL);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booked_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booked_id`,`amount`,`date`,`type`) values 
(1,2,'7000','2025-02-06','ticket'),
(2,3,'5000','2025-02-09','ticket');

/*Table structure for table `place` */

DROP TABLE IF EXISTS `place`;

CREATE TABLE `place` (
  `place_id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) DEFAULT NULL,
  `state_place` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`place_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `place` */

insert  into `place`(`place_id`,`country_id`,`state_place`) values 
(8,2,'Nedumbaserry '),
(11,2,'Chacka'),
(10,2,'Karipur'),
(13,2,'kerala-kollam'),
(14,2,'kerala-thrissur'),
(15,6,'dubai internation airport s');

/*Table structure for table `seats` */

DROP TABLE IF EXISTS `seats`;

CREATE TABLE `seats` (
  `seat_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT NULL,
  `ship_id` int(11) DEFAULT NULL,
  `seatno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`seat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `seats` */

insert  into `seats`(`seat_id`,`type_id`,`ship_id`,`seatno`) values 
(1,3,2,'13'),
(2,4,2,'12'),
(3,2,2,'10'),
(4,2,2,'1'),
(5,3,2,'3'),
(6,4,2,'2');

/*Table structure for table `shipports` */

DROP TABLE IF EXISTS `shipports`;

CREATE TABLE `shipports` (
  `shipport_id` int(11) NOT NULL AUTO_INCREMENT,
  `place_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`shipport_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `shipports` */

insert  into `shipports`(`shipport_id`,`place_id`,`name`,`district`,`state`) values 
(3,5,'Trivandrum International Airport','Thiruvanthpuram','kerala'),
(9,10,'Calicut International Airport','Kozhikode','Kerala '),
(7,8,'Cochin International Airport','Ernakulam ','Kerala'),
(8,9,'Kannur International Airport','Kannur ','kerala'),
(11,15,'ship port dubai','di=uabi','duabi');

/*Table structure for table `ships` */

DROP TABLE IF EXISTS `ships`;

CREATE TABLE `ships` (
  `ship_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `ship_name` varchar(100) DEFAULT NULL,
  `noofseats` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `registartion_date` varchar(100) DEFAULT NULL,
  `ship_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ship_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `ships` */

insert  into `ships`(`ship_id`,`company_id`,`ship_name`,`noofseats`,`latitude`,`longitude`,`registartion_date`,`ship_status`) values 
(2,3,'shinto ship','850','9.988715685028335','76.2879467010498','2025-02-05','verify'),
(3,3,'marina one','120','9.9787996440854','76.2991011733563','2025-02-05','reject');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`firstname`,`lastname`,`gender`,`age`,`phone`,`email`,`designation`,`company_id`) values 
(1,2,'sdzfsdgvsdffv','S','Male','38','9956678787','manju7774@gmail.com','worker',NULL),
(2,5,'Manju dddddddddd','S','Male','38','9956678787','manju7774@gmail.com','worker',NULL),
(3,6,'Manju dddddddddd','S','Male','38','9956678787','manju7774@gmail.com','worker',NULL),
(4,16,'ann atos','captain cool','Male','25','7894561230','uu@gmail.com','hbcdhfcb',3);

/*Table structure for table `staffallocate` */

DROP TABLE IF EXISTS `staffallocate`;

CREATE TABLE `staffallocate` (
  `allocate_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `ship_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `shipport_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocate_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staffallocate` */

insert  into `staffallocate`(`allocate_id`,`staff_id`,`ship_id`,`status`,`shipport_id`) values 
(1,4,2,'accept',11);

/*Table structure for table `ticketsbooked` */

DROP TABLE IF EXISTS `ticketsbooked`;

CREATE TABLE `ticketsbooked` (
  `booked_id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `noofpassengers` varchar(100) DEFAULT NULL,
  `booked_status` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `package_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`booked_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `ticketsbooked` */

insert  into `ticketsbooked`(`booked_id`,`schedule_id`,`amount`,`noofpassengers`,`booked_status`,`user_id`,`package_id`) values 
(2,2,'7000','2','Approve',4,4),
(3,2,'5000','2','Paid',4,1);

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `type` */

insert  into `type`(`type_id`,`type`) values 
(2,'aside '),
(3,'window '),
(4,'middle');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `path` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`path`) values 
(1,3,'Radhu','K','Ernakulam','9444467784','syamraj310@gmail.com','static/uploadimages/62e56ea2-0ebd-486b-be84-ead3f1422566dedekinds prop.JPG'),
(3,7,'Noelle Huber','Zachary Sosa','Eum dolore mollitia ','9999999999','sepez@mailinator.com','static/uploadimages/d979e1d5-17d3-4102-b6da-691c6ff3f7fc2.png'),
(4,9,'liya','antony','kollam','9454845154','gg@gmail.com','static/uploadimages/4cfde315-f929-4af8-8868-b8038640abcbWhatsApp Image 2025-01-24 at 10.27.26 PM.jpeg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
