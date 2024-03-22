-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 08, 2023 at 06:37 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hnc`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `user_id` int(10) NOT NULL,
  `username` varchar(55) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`user_id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phonenumber` bigint(10) NOT NULL,
  `message` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `phonenumber`, `message`) VALUES
(2, 'thanveer', 'thannu914491@gmail.com', 9346736020, 'good website for franchise');

-- --------------------------------------------------------

--
-- Table structure for table `forget`
--

CREATE TABLE `forget` (
  `email` varchar(66) NOT NULL,
  `otp` varchar(99) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `forget`
--

INSERT INTO `forget` (`email`, `otp`) VALUES
('ksriya3105@gmail.com', '6086');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `item_id` int(4) NOT NULL,
  `item_image` varchar(100) NOT NULL,
  `item_name` varchar(15) NOT NULL,
  `item_desc` varchar(500) NOT NULL,
  `item_cost` int(5) NOT NULL,
  `quantity` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`item_id`, `item_image`, `item_name`, `item_desc`, `item_cost`, `quantity`) VALUES
(1, 'menu1.jpg', 'pizza', 'Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients (such as various types of sausage, anchovies, mushrooms, onions, olives, vegetables, meat, ham, etc.), which is then baked at a high temperature, traditionally in a wood-fired oven.A small pizza is sometimes called a pizzetta.', 100, 0),
(2, 'menu-2.jpeg', 'burger', 'The patties that are the essence of a veggie burger have existed in various Eurasian cuisines for mi', 150, 0),
(3, 'menu-3.jpg', 'Sandwich', 'A sandwich is a food typically consisting of vegetables, sliced cheese or meat, placed on or between slices of bread, or more generally any dish wherein bread serves as a container or wrapper for another food type.The sandwich began as a portable, convenient finger food in the Western world, though over time it has become prevalent worldwide.', 100, 0),
(4, 'menu-4.jpg', 'Wraps', 'A wrap is a dish made with a soft flatbread rolled around a filling.The usual flatbreads are wheat tortillas, lavash, or pita; the filling may include cold sliced meat, poultry, or fish, shredded lettuce, diced tomato or pico de gallo, guacamole, sauteed mushrooms, bacon, grilled onions, cheese, and a sauce, such as ranch or honey mustard.', 80, 0),
(5, 'menu-5.jpg', 'Bread pizza', 'Bread pizza is a yummy snack made using bread as the pizza base. This easy recipe will help you make bread pizza on stove top or oven. This can be enjoyed as a evening snack or a party starter.', 150, 0),
(6, 'menu-6.jpg', 'Fries ', 'French fries are prepared by cutting potatoes into even strips, drying them, and frying them, usually in a deep fryer. Pre-cut, blanched, and frozen russet potatoes are widely used, and sometimes baked in a regular or convection oven; air fryers are small convection ovens marketed for frying potatoes. ', 60, 0),
(7, 'menu-7.jpg', 'Momos', 'Momo is a type of East and South Asian steamed filled dumpling. Momos are native to Tibet, Nepal, Bhutan, as well as North Indian region of Ladakh, Northeast Indian regions of Sikkim, Assam, and Arunachal Pradesh, and East Indian region of Darjeeling. It is popular across a wider region of the Indian subcontinent.', 100, 0),
(8, 'menu-8.jpg', 'Shakes', 'A shake is a sweet drink made by blending milk, ice cream, and flavorings or sweeteners such as butterscotch, caramel sauce, chocolate syrup, fruit syrup, or whole fruit into a thick, sweet, cold mixture. It may also be made using other types of milk such as almond milk, coconut milk, or soy milk.', 50, 0),
(9, 'menu-9_b7mMRGz.jpg', 'Ice cream', 'Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together.', 50, 0),
(10, 'menu-10_23dLA6Q.jpg', 'Mock tail', 'A mocktail is a non-alcoholic mixed drink. Mocktails are designed to look and taste like a fancy cocktail but without all the alcohol.When a drink is categorized as a mocktail, it is usually a replica of a real cocktail but the alcoholic ingredients have been replaced with juice, seltzers, water or simply eliminated.', 200, 0),
(11, 'menu-11_56qe9Rz.jpg', 'Combos', 'Combos, officially called Combos Stuffed Snacks, are cylindrical tubes of cracker, pretzel, or tortilla, available with various fillings.Combos are produced by forming a soft bread-like dough, which is hollowed out into a tube-shaped form. A cutter slices the dough into bite-sized lengths. The snacks are then baked, cooled, and filled with the appropriate filling.', 1000, 0),
(12, 'cfries.JPG', 'cheese fries', 'Cheese fries or cheesy chips (latter British English) is a dish consisting of French fries covered in cheese, with the possible addition of various other toppings. Cheese fries are generally served as a lunch or dinner dish. They can be found in fast-food locations, diners, and grills around the globe.', 70, 0);

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(66) NOT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`id`, `username`, `email`, `message`) VALUES
(1, 'maneesh', 'maneesh@gmail.com', 'hi');

-- --------------------------------------------------------

--
-- Table structure for table `orderdetails`
--

CREATE TABLE `orderdetails` (
  `orderitemid` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `itemid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderdetails`
--

INSERT INTO `orderdetails` (`orderitemid`, `order_id`, `itemid`, `quantity`) VALUES
(1, 1, 1, 2),
(2, 1, 4, 2),
(3, 1, 9, 4),
(4, 2, 6, 2),
(5, 3, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `ordereddate` date NOT NULL DEFAULT current_timestamp(),
  `deliverystatus` varchar(10) NOT NULL,
  `totalamount` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `username`, `ordereddate`, `deliverystatus`, `totalamount`) VALUES
(1, 'sriya', '2023-04-08', '0', 560),
(2, 'rohith', '2023-04-08', '0', 120),
(3, 'rohith', '2023-04-08', '0', 0);

-- --------------------------------------------------------

--
-- Table structure for table `paydetails`
--

CREATE TABLE `paydetails` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phonenumber` bigint(11) NOT NULL,
  `baddress` varchar(99) NOT NULL,
  `saddress` varchar(100) NOT NULL,
  `cardnumber` bigint(11) NOT NULL,
  `cvv` bigint(3) NOT NULL,
  `deliverystatus` varchar(15) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `paydetails`
--

INSERT INTO `paydetails` (`id`, `name`, `email`, `phonenumber`, `baddress`, `saddress`, `cardnumber`, `cvv`, `deliverystatus`, `username`, `order_id`) VALUES
(3, 'thanveer', 'thannu914491@gmail.com', 9346736020, 'hzb', 'hzb', 987656789332, 456, '0', 'rohith', 8),
(4, 'kunkumalla sriya', 'sriyakunkumalla@gmail.com', 9390316760, 'H-NO:1-44/A,near hanuman temple,kasulapalli,peddapalli', 'hzb', 9876543234567, 678, '0', 'rohith', 9),
(5, 'maneesh', 'maneesh@gmail.com', 9346736020, 'karimnagar', 'karimnagar', 987345362812, 845, '0', 'sriya', 1),
(6, 'rohith', 'gaderohith2002@gmail.com', 6305559479, 'warangal', 'karimnagar', 345678923123, 193, '0', 'rohith', 2);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(4) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(66) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phoneNumber` varchar(10) NOT NULL,
  `u_password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `name`, `email`, `address`, `phoneNumber`, `u_password`) VALUES
(1, 'rohith', 'gaderohith2002@gmail.com', 'warangal', '6305559479', '12'),
(2, 'sriya', 'ksriya3105@gmail.com', 'karimnagar', '9390316760', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`item_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD PRIMARY KEY (`orderitemid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `paydetails`
--
ALTER TABLE `paydetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `item_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `orderdetails`
--
ALTER TABLE `orderdetails`
  MODIFY `orderitemid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `paydetails`
--
ALTER TABLE `paydetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
