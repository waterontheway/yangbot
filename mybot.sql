-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 17, 2023 at 08:42 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mybot`
--

-- --------------------------------------------------------

--
-- Table structure for table `linebot_image`
--

CREATE TABLE `linebot_image` (
  `No` int(11) NOT NULL,
  `DateTime` varchar(100) NOT NULL,
  `UserID` varchar(100) DEFAULT NULL,
  `DisplayName` varchar(30) DEFAULT NULL,
  `FileName` varchar(300) NOT NULL,
  `GoogleDrive` varchar(300) NOT NULL,
  `Address` varchar(500) DEFAULT NULL,
  `Latitude` varchar(100) DEFAULT NULL,
  `Longitude` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `linebot_log`
--

CREATE TABLE `linebot_log` (
  `No` int(11) NOT NULL,
  `DateTime` varchar(100) NOT NULL,
  `UserID` varchar(100) DEFAULT NULL,
  `DisplayName` varchar(30) DEFAULT NULL,
  `Message` varchar(200) NOT NULL,
  `MessageType` varchar(200) NOT NULL,
  `ReplyMessage` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `linebot_user`
--

CREATE TABLE `linebot_user` (
  `No` int(11) NOT NULL,
  `DateTime` varchar(100) NOT NULL,
  `UserID` varchar(100) DEFAULT NULL,
  `DisplayName` varchar(30) DEFAULT NULL,
  `Status` int(11) DEFAULT NULL,
  `FullName` varchar(100) DEFAULT NULL,
  `Address` varchar(500) DEFAULT NULL,
  `Latitude` varchar(100) DEFAULT NULL,
  `Longitude` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `linebot_image`
--
ALTER TABLE `linebot_image`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `linebot_log`
--
ALTER TABLE `linebot_log`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `linebot_user`
--
ALTER TABLE `linebot_user`
  ADD PRIMARY KEY (`No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `linebot_image`
--
ALTER TABLE `linebot_image`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `linebot_log`
--
ALTER TABLE `linebot_log`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `linebot_user`
--
ALTER TABLE `linebot_user`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
