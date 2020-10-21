--
-- Table structure for table `author`
--
 
 
CREATE TABLE `author` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `profile` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
 
--
-- Dumping data for table `author`
--
 
INSERT INTO `author` VALUES (1,'leechaemin','developer');
INSERT INTO `author` VALUES (2,'pepsi','data scientist');
INSERT INTO `author` VALUES (3,'cokacola','data engineer');
 
--
-- Table structure for table `topic`
--
 
CREATE TABLE `topic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `description` text,
  `created` datetime NOT NULL,
  `author_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
);
 
--
-- Dumping data for table `topic`
--
 
INSERT INTO `topic` VALUES (1,'MySQL','MySQL is...','2020-10-18 12:17:37',1);
INSERT INTO `topic` VALUES (2,'Oracle','Oracle is ...','2020-10-18 12:22:29',1);
INSERT INTO `topic` VALUES (3,'MongoDB','MongoDB is ...','2020-10-18 12:24:29',2);
INSERT INTO `topic` VALUES (4,'NOSQL','NOSQL is ...','2020-10-18 12:25:50',1);
INSERT INTO `topic` VALUES (5,'SQL Server','SQL Server is ...','2020-10-18 13:19:13',3);

