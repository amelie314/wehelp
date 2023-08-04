-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',10,'2023-08-01 12:34:56'),(2,'Jane Smith','user2','password2',5,'2023-07-31 08:45:30'),(3,'Tom Johnson','user3','password3',15,'2023-07-30 17:23:45'),(4,'Alice Williams','user4','password4',8,'2023-07-29 09:12:34'),(5,'Amelie Chen','user5','password5',20,'2023-07-28 20:15:10');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'留言內容186',59,'2023-02-27 08:04:37'),(2,2,'留言內容666',66,'2023-04-05 01:19:37'),(3,3,'留言內容569',91,'2022-09-24 03:23:37'),(4,4,'留言內容487',72,'2023-05-28 23:29:37'),(5,5,'留言內容485',0,'2023-01-05 20:04:37'),(6,1,'留言內容226',45,'2023-01-04 03:35:37'),(7,2,'留言內容507',42,'2022-12-18 20:19:37'),(8,3,'留言內容43',28,'2023-04-19 02:27:37'),(9,4,'留言內容70',80,'2022-10-04 23:29:37'),(10,5,'留言內容545',29,'2022-10-09 10:56:37'),(11,1,'留言內容799',89,'2023-06-30 22:01:37'),(12,2,'留言內容739',84,'2023-07-27 02:49:37'),(13,3,'留言內容335',23,'2023-06-03 13:22:37'),(14,4,'留言內容834',39,'2023-02-20 14:30:37'),(15,5,'留言內容340',32,'2023-01-03 17:39:37'),(16,1,'留言內容42',28,'2023-04-10 23:00:37'),(17,2,'留言內容951',90,'2022-12-07 01:39:37'),(18,3,'留言內容100',57,'2022-12-31 11:16:37'),(19,4,'留言內容82',35,'2023-01-24 03:22:37'),(20,5,'留言內容623',31,'2022-11-12 00:26:37'),(21,1,'留言內容968',24,'2023-04-11 20:23:37'),(22,2,'留言內容730',90,'2023-04-05 17:56:37'),(23,3,'留言內容668',25,'2023-04-26 02:24:37'),(24,4,'留言內容258',64,'2023-03-02 10:51:37'),(25,5,'留言內容258',95,'2023-08-03 12:53:37'),(26,1,'留言內容267',10,'2022-11-13 09:15:37'),(27,2,'留言內容929',53,'2022-09-21 23:32:37'),(28,3,'留言內容252',98,'2023-06-06 19:52:37'),(29,4,'留言內容283',11,'2022-11-06 08:04:37'),(30,5,'留言內容728',96,'2022-12-19 11:16:37'),(31,1,'留言內容27',7,'2023-04-19 10:16:37'),(32,2,'留言內容78',29,'2023-05-10 08:51:37'),(33,3,'留言內容999',66,'2023-04-11 01:38:37'),(34,4,'留言內容203',3,'2023-01-06 22:33:37'),(35,5,'留言內容77',17,'2022-12-14 00:08:37'),(36,1,'留言內容380',44,'2023-06-28 12:05:37'),(37,2,'留言內容179',28,'2022-09-19 04:37:37'),(38,3,'留言內容497',43,'2022-11-22 11:49:37'),(39,4,'留言內容466',92,'2023-05-07 06:11:37'),(40,5,'留言內容911',22,'2023-03-11 09:11:37'),(41,1,'留言內容226',80,'2023-04-07 11:26:37'),(42,2,'留言內容266',74,'2022-08-27 06:13:37'),(43,3,'留言內容719',36,'2022-12-04 11:26:37'),(44,4,'留言內容234',60,'2023-04-12 22:51:37'),(45,5,'留言內容671',2,'2023-07-04 08:01:37'),(46,1,'留言內容897',67,'2022-11-21 05:20:37'),(47,2,'留言內容1',14,'2022-11-15 13:00:37'),(48,3,'留言內容680',50,'2023-01-31 16:05:37'),(49,4,'留言內容658',67,'2023-03-10 16:56:37'),(50,5,'留言內容496',42,'2022-12-12 17:54:37');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-04 18:04:13
