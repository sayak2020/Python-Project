-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 22, 2020 at 03:39 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ardent`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `id` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`id`, `password`) VALUES
('sayak@gmail.com', 'sayak1234');

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `sl` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `bloodgroup` varchar(5) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `pin` varchar(10) NOT NULL,
  `status` varchar(5) NOT NULL DEFAULT 'p'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`sl`, `name`, `phone`, `email`, `age`, `gender`, `bloodgroup`, `dob`, `pin`, `status`) VALUES
(66, 'Sayak Chatterjee ', '7686831513', 'sayak@gmail.com', '1', 'male', 'A-', '2020-06-18', '700123', 'd'),
(67, 'Sayak Chatterjee ', '7686831513', 'sayak@gmail.com', '19', 'male', 'AB-', '2020-06-25', '700123', 'd'),
(69, 'd', '7686831513', 'sayak@gmail.com', '12', 'other', 'B+', '2020-06-01', '700123', 'd'),
(70, 'd', '7686831513', 'sayak@gmail.com', '12', 'other', 'B+', '2020-06-01', '700123', 'd'),
(71, 'd', '7686831513', 'sayak@gmail.com', '12', 'other', 'B+', '2020-06-01', '700123', 'd'),
(72, 'Sayak Chatterjee ', '7686831513', 'sayak@gmail.com', '1', 'male', 'A-', '2020-06-03', '700123', 'd'),
(73, 'Sayak das', '9876543210', 'sayak@gmail.com', '20', 'female', 'AB+', '2020-06-24', '700123', 'p'),
(74, 'Sayak Chatterjee ', '7686831513', 'sayak@gmail.com', '18', 'male', 'O+', '2000-08-20', '700123', 'p'),
(75, 'sourin paul', '9001234567', 'abc@gmail.com', '18', 'male', 'AB+', '2020-06-01', '700123', 'd'),
(76, 'Sayak Chatterjee ', '7686831513', 'abc@gmail.com', '18', 'male', 'B-', '2020-06-10', '700123', 'd'),
(77, 'Sayak Chatterjee ', '7686831513', 'abc@gmail.com', '1', 'male', 'B+', '2020-06-16', '700123', 'd'),
(78, 'Sayak Chatterjee ', '7686831513', 'abc@gmail.com', '12', 'female', 'A-', '2020-06-24', '700123', 'p'),
(79, 'Biswarup', '9876543221', 'b', '19', 'other', 'O-', '2020-06-01', '700123', 'p'),
(80, 'Manjit Mondal', '9876543210', 'manjit@gmail.com', '20', 'male', 'O+', '2020-06-17', '700123', 'd'),
(81, 'Sayak das', '7686831513', 'sayak@gmail.com', '18', 'male', 'O+', '2020-06-01', '700123', 'p'),
(82, 'jonty', '9876543210', 'jonty@gmail.com', '21', 'male', 'A+', '2020-06-19', '700100', 'p');

-- --------------------------------------------------------

--
-- Table structure for table `msg`
--

CREATE TABLE `msg` (
  `sl` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `msg` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `msg`
--

INSERT INTO `msg` (`sl`, `name`, `email`, `subject`, `msg`) VALUES
(1, 'Sayak Chatterjee ', 'abc@gmail.com', 'trial', 'trial one'),
(2, 'sayan mandal', 'sayak@gmail.co', 'blood Donation', 'want to donate blood can you reach me?'),
(3, 'sourin', 'so@gmail.com', 'trial', 'traial 2'),
(4, 'Sayak Chatterjee ', 'abc@gmail.com', 'trial', 'scscsc');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `sl` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`sl`, `email`, `password`, `name`, `phone`) VALUES
(1, 'abc@gmail.com', '1234', 'Sayak Chatterjee ', '7686831513'),
(6, 'b', 'b', 'biswarup ', '9876543210'),
(9, 'jonty@gmail.com', 'jonty1234', 'jonty', '9876543210'),
(7, 'manjit@gmail.com', '1234', 'Manjit Mondal', '9876543210'),
(4, 'sayak@gmail.com', '12345678', 'Sayak Chatterjee ', '7686831513'),
(3, 'sourin@gmail.com', 'sourin', 'sourin paul', '123890'),
(5, 'tanmay@gmail.com', '1234', 'tanmay sarkar', '1000000'),
(8, 'tom@gmail.com', '12345678', 'tom', '7686831513');

-- --------------------------------------------------------

--
-- Table structure for table `riskanalysis`
--

CREATE TABLE `riskanalysis` (
  `sl` int(11) NOT NULL,
  `risk` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `riskanalysis`
--

INSERT INTO `riskanalysis` (`sl`, `risk`) VALUES
(1, 'lr'),
(8, 'lr'),
(9, 'mr'),
(10, 'mr'),
(11, 'mr'),
(12, 'hr'),
(13, 'hr'),
(14, 'lr'),
(15, 'mr'),
(16, 'hr'),
(17, 'mr'),
(18, 'hr'),
(19, 'hr'),
(20, 'mr'),
(21, 'mr'),
(22, 'mr'),
(23, 'mr'),
(24, 'mr'),
(25, 'mr'),
(26, 'mr'),
(27, 'mr'),
(28, 'mr'),
(29, 'mr'),
(30, 'mr'),
(31, 'mr'),
(32, 'mr'),
(33, 'mr'),
(34, 'mr'),
(35, 'mr'),
(36, 'hr'),
(37, 'hr'),
(38, 'hr'),
(39, 'hr'),
(40, 'hr'),
(41, 'lr'),
(42, 'lr'),
(43, 'lr'),
(44, 'lr'),
(45, 'mr'),
(46, 'mr'),
(47, 'lr'),
(48, 'lr'),
(49, 'hr'),
(50, 'hr'),
(51, 'lr'),
(52, 'lr'),
(53, 'lr'),
(54, 'lr'),
(55, 'lr'),
(56, 'mr'),
(57, 'mr'),
(58, 'mr'),
(59, 'mr'),
(60, 'mr'),
(61, 'mr'),
(62, 'mr'),
(63, 'mr'),
(64, 'mr'),
(65, 'mr'),
(66, 'hr'),
(67, 'hr'),
(68, 'hr'),
(69, 'hr'),
(70, 'mr'),
(71, 'mr'),
(72, 'mr'),
(73, 'mr'),
(74, 'mr'),
(75, 'mr'),
(76, 'hr'),
(77, 'hr'),
(78, 'hr');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `sl` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `test` varchar(50) NOT NULL,
  `status` varchar(5) NOT NULL,
  `r1` varchar(50) DEFAULT NULL,
  `r2` varchar(50) DEFAULT NULL,
  `r3` varchar(50) DEFAULT NULL,
  `r4` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`sl`, `email`, `test`, `status`, `r1`, `r2`, `r3`, `r4`) VALUES
(1, 'sayak@gmail.com', 'COVID-19', 'd', 'day one -ve', 'day 2 -ve', 'rtpcr -ve', 'Negative'),
(3, 'sayak@gmail.com', 'HEAMOGLOBIN', 'd', 'a', 'b', 'c', 'adsd'),
(4, 'sayak@gmail.com', 'BLOOD SUGAR', 'd', 'high:120', 'low:80', 'your Result: 110', 'good'),
(6, 'sayak@gmail.com', 'THYROID', 'd', 'high:120', 'low:80', 'your Result: 110', 'NORMAL LEVEL.'),
(9, 'sayak@gmail.com', 'LIVER FUNCTION', 'd', 'Q', 'Q', 'Q', 'QQQQQQ'),
(10, 'abc@gmail.com', 'LIPID PROFILE', 'd', 'HDL: 120/20', 'LDL: 130/40', 'VLDL: 120/80', 'good'),
(11, 'abc@gmail.com', 'BLOOD SUGAR', 'd', 'empty stomach : 100', 'PE: 120', 'SE: 100', 'High'),
(12, 'tanmay@gmail.com', 'COVID-19', 'd', 'high:120', 'low:80', 'your Result: 110', 'good'),
(13, 'tanmay@gmail.com', 'THYROID', 'd', 'HDL: 120/20', 'low:80', 'rtpcr -ve', 'trial'),
(14, 'tanmay@gmail.com', 'LIPID PROFILE', 'd', 'LDL: 100', 'HDL: 120', 'VLDL: 120/80', 'GOOD REPORT'),
(15, 'abc@gmail.com', 'THYROID', 'd', 'high:120', 'low:80', 'your Result: 110', 'good'),
(16, 'abc@gmail.com', 'THYROID', 'd', 'high:120', 'low:80', 'your Result: 110', 'good'),
(17, 'abc@gmail.com', 'BLOOD SUGAR', 'd', 'empty stomach : 100', 'PE: 120', 'SE: 100', 'High'),
(18, 'b', 'COVID-19', 'p', NULL, NULL, NULL, NULL),
(19, 'b', 'HEAMOGLOBIN', 'p', NULL, NULL, NULL, NULL),
(20, 'manjit@gmail.com', 'COVID-19', 'd', 'a', 'b', 'c', 'trial'),
(21, 'manjit@gmail.com', 'BLOOD SUGAR', 'd', 'TSH 100', 'day 2 -ve', 'T3 90', 'MODERATE LEVEL'),
(22, 'manjit@gmail.com', 'LIVER FUNCTION', 'd', 'high:120', 'HDL: 120', 'VLDL: 80', 'GOOD REPORT'),
(23, 'manjit@gmail.com', 'THYROID', 'd', 'high:120', 'low:80', 'your Result: 110', 'Negative'),
(24, 'sayak@gmail.com', 'LIPID PROFILE', 'd', 'HDL: 120/20', 'LDL: 130/40', 'VLDL: 120/80', 'MODERATE LEVEL'),
(25, 'jonty@gmail.com', 'LIPID PROFILE', 'd', 'LDL: 100', 'HDL: 120', 'VLDL: 80', 'GOOD REPORT'),
(26, 'jonty@gmail.com', 'THYROID', 'd', 'TSH 100', 'T4 120', 'T3 90', 'NORMAL LEVEL.'),
(27, 'sayak@gmail.com', 'HEAMOGLOBIN', 'd', 'a', 'b', 'c', 'adsd'),
(28, 'sayak@gmail.com', 'LIVER FUNCTION', 'd', 'Q', 'Q', 'Q', 'QQQQQQ'),
(29, 'sayak@gmail.com', 'BLOOD SUGAR', 'p', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`sl`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `msg`
--
ALTER TABLE `msg`
  ADD PRIMARY KEY (`sl`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `sl` (`sl`);

--
-- Indexes for table `riskanalysis`
--
ALTER TABLE `riskanalysis`
  ADD PRIMARY KEY (`sl`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`sl`),
  ADD KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `sl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `msg`
--
ALTER TABLE `msg`
  MODIFY `sl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `sl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `riskanalysis`
--
ALTER TABLE `riskanalysis`
  MODIFY `sl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `sl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`email`) REFERENCES `register` (`email`);

--
-- Constraints for table `test`
--
ALTER TABLE `test`
  ADD CONSTRAINT `test_ibfk_1` FOREIGN KEY (`email`) REFERENCES `register` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
