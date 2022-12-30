-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 27, 2022 at 09:50 AM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `upscacademy`
--

-- --------------------------------------------------------

--
-- Table structure for table `aspirants_details`
--

DROP TABLE IF EXISTS `aspirants_details`;
CREATE TABLE IF NOT EXISTS `aspirants_details` (
  `aspirant_id` int(11) NOT NULL AUTO_INCREMENT,
  `full_Name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `phone_Number` bigint(20) NOT NULL,
  `profile` varchar(100) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `pin_number` varchar(255) NOT NULL,
  `register_date` date DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`aspirant_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aspirants_details`
--

INSERT INTO `aspirants_details` (`aspirant_id`, `full_Name`, `email`, `password`, `phone_Number`, `profile`, `state`, `country`, `education`, `address`, `pin_number`, `register_date`, `status`) VALUES
(29, 'Aslam', 'aslam@gmail.com', 'Aslam143@', 8765432109, 'images/6_0FrYzwc.png', 'Karnataka', 'India', 'B-form', 'Marathalli', '4567890', '2022-10-27', 'Pending'),
(28, 'Sundeep', 'sundeep12@gmail.com', 'Sandi@44', 9876543210, 'images/1_S7kWyWK.png', 'UP', 'India', 'M-form', 'Varanasi', '08876543', '2022-10-27', 'Pending'),
(26, 'Rohit', 'rohit@gmail.com', 'Rohit11$', 6783940284, 'images/7_mMLzNd4.png', 'TS', 'India', 'Bcom', 'Medak', '543678', '2022-10-27', 'Pending'),
(27, 'Abhilash', 'abhi@gmail.com', 'aBhi#1122', 8765432109, 'images/5_tSb2Gp3.png', 'Mp', 'India', 'Degree', 'Pune', '0876543', '2022-10-27', 'Pending'),
(13, 'Arjun', 'arjun@gmail.com', 'Arjun@1234', 12345674567, 'images/vijay_1_2.jpg', 'AP', 'India', 'BE', 'oppicherla', '234567', '2022-10-22', 'Accept'),
(11, 'Vijay kumar', 'vijayk@gmail.com', 'vijaY@1234', 7842505334, 'images/DSC06920.JPG', 'AP', 'India', 'java', 'Lb Nagar', '1234566', '2022-10-21', 'Accept'),
(12, 'Kiran', 'kiran@gmail.com', 'Kiran#1234', 1234567890, 'images/IMG_20171019_181033.jpg', 'Ap', 'India', 'Degree', 'kphb', '500072', '2022-10-22', 'Accept'),
(23, 'jeshwanth', 'jeswanth@gmail.com', 'Jes@1234', 7653537489, 'images/tyles.jpg', 'TS', 'India', 'B-tech', 'Lb Nagar', '233456', '2022-10-25', 'Accept'),
(30, 'Suraj', 'suraj@gmail.com', 'Auraj00&12', 6098543217, 'images/testimonial-1.jpg', 'Tamilnadu', 'India', 'MBA', 'Chennai', '485769', '2022-10-27', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `aspirant_feadback`
--

DROP TABLE IF EXISTS `aspirant_feadback`;
CREATE TABLE IF NOT EXISTS `aspirant_feadback` (
  `feadback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback_message` longtext NOT NULL,
  `feedback_sentiment` varchar(20) NOT NULL,
  `feedback_date` date NOT NULL,
  `aspirant_id` int(11) DEFAULT NULL,
  `rating1` int(11) DEFAULT NULL,
  `rating2` int(11) DEFAULT NULL,
  `rating3` int(11) DEFAULT NULL,
  PRIMARY KEY (`feadback_id`),
  KEY `aspirant_feadback_aspirant_id_0ce00ad4` (`aspirant_id`)
) ENGINE=MyISAM AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aspirant_feadback`
--

INSERT INTO `aspirant_feadback` (`feadback_id`, `feedback_message`, `feedback_sentiment`, `feedback_date`, `aspirant_id`, `rating1`, `rating2`, `rating3`) VALUES
(7, 'it is nice to visit this site and very good study material, but videos are not good and mock test too', 'Positive', '2022-10-20', 5, 4, 3, 2),
(8, 'it is nice to visit this site and very good study material, but videos are not good and mock test too', 'Positive', '2022-10-20', 5, 4, 3, 2),
(9, 'it is nice to visit this site and very good study material, but videos are not good and mock test too', 'Positive', '2022-10-20', 5, 4, 3, 2),
(10, 'not statisfied\r\n', 'Neutral', '2022-10-20', 5, 1, 1, 1),
(11, 'nice videos ', 'very Positive', '2022-10-20', 5, 4, 4, 4),
(48, 'Not good ', 'Negative', '2022-10-26', 12, 1, 3, 2),
(44, 'Nice environment and happy to be here', 'very Positive', '2022-10-22', 13, 4, 2, 4),
(46, 'This is the best academy I have ever seen before they are providing good study material and reference videos and mock papers also ......', 'very Positive', '2022-10-24', 11, 4, 2, 5),
(47, 'Very bad experience with faculty members but good environment ', 'Negative', '2022-10-24', 12, 3, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add upsc study material', 7, 'add_upscstudymaterial'),
(26, 'Can change upsc study material', 7, 'change_upscstudymaterial'),
(27, 'Can delete upsc study material', 7, 'delete_upscstudymaterial'),
(28, 'Can view upsc study material', 7, 'view_upscstudymaterial'),
(29, 'Can add upsc interview videos', 8, 'add_upscinterviewvideos'),
(30, 'Can change upsc interview videos', 8, 'change_upscinterviewvideos'),
(31, 'Can delete upsc interview videos', 8, 'delete_upscinterviewvideos'),
(32, 'Can view upsc interview videos', 8, 'view_upscinterviewvideos'),
(33, 'Can add upsc mock test', 9, 'add_upscmocktest'),
(34, 'Can change upsc mock test', 9, 'change_upscmocktest'),
(35, 'Can delete upsc mock test', 9, 'delete_upscmocktest'),
(36, 'Can view upsc mock test', 9, 'view_upscmocktest'),
(37, 'Can add aspirants model', 10, 'add_aspirantsmodel'),
(38, 'Can change aspirants model', 10, 'change_aspirantsmodel'),
(39, 'Can delete aspirants model', 10, 'delete_aspirantsmodel'),
(40, 'Can view aspirants model', 10, 'view_aspirantsmodel'),
(41, 'Can add aspirant feadback model', 11, 'add_aspirantfeadbackmodel'),
(42, 'Can change aspirant feadback model', 11, 'change_aspirantfeadbackmodel'),
(43, 'Can delete aspirant feadback model', 11, 'delete_aspirantfeadbackmodel'),
(44, 'Can view aspirant feadback model', 11, 'view_aspirantfeadbackmodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'adminapp', 'upscstudymaterial'),
(8, 'adminapp', 'upscinterviewvideos'),
(9, 'adminapp', 'upscmocktest'),
(10, 'aspirantapp', 'aspirantsmodel'),
(11, 'aspirantapp', 'aspirantfeadbackmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-10-18 10:12:08.004673'),
(2, 'auth', '0001_initial', '2022-10-18 10:12:08.262403'),
(3, 'admin', '0001_initial', '2022-10-18 10:12:08.338773'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-10-18 10:12:08.345753'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-18 10:12:08.353701'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-10-18 10:12:08.398122'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-10-18 10:12:08.419066'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-10-18 10:12:08.442003'),
(9, 'auth', '0004_alter_user_username_opts', '2022-10-18 10:12:08.449980'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-10-18 10:12:08.473864'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-10-18 10:12:08.475860'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-10-18 10:12:08.482840'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-10-18 10:12:08.506777'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-10-18 10:12:08.528716'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-10-18 10:12:08.550660'),
(16, 'auth', '0011_update_proxy_permissions', '2022-10-18 10:12:08.561661'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-10-18 10:12:08.583570'),
(18, 'sessions', '0001_initial', '2022-10-18 10:12:08.612492'),
(19, 'adminapp', '0001_initial', '2022-10-18 10:13:21.842531'),
(20, 'aspirantapp', '0001_initial', '2022-10-18 10:13:30.883189'),
(21, 'aspirantapp', '0002_remove_aspirantfeadbackmodel_rating_and_more', '2022-10-20 07:41:39.437462'),
(22, 'aspirantapp', '0003_aspirantfeadbackmodel_rating2_and_more', '2022-10-20 07:42:55.171546'),
(23, 'aspirantapp', '0004_alter_aspirantfeadbackmodel_rating1_and_more', '2022-10-20 07:44:13.058262'),
(24, 'aspirantapp', '0005_alter_aspirantfeadbackmodel_rating1', '2022-10-20 07:45:42.933225'),
(25, 'aspirantapp', '0006_alter_aspirantfeadbackmodel_rating1', '2022-10-20 08:24:04.756625'),
(26, 'aspirantapp', '0007_alter_aspirantfeadbackmodel_rating1', '2022-10-20 09:58:43.322457'),
(27, 'adminapp', '0002_upscinterviewvideos_videos_image', '2022-10-24 12:05:32.542112'),
(28, 'adminapp', '0003_upscmocktest_upload_image', '2022-10-27 06:12:14.912262');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('bytrsy9nq57o944ukhppnrxwv61iq8c7', 'eyJhc3BpcmFudF9pZCI6MTJ9:1onzDZ:WVUZkHZWePjhj-Pz_W0awsm5A0LXfdpWeRv0twm5ZhE', '2022-11-10 09:30:29.779135'),
('ykul756aqz7uutc3yvl9d5a3rdavspqm', 'eyJhc3BpcmFudF9pZCI6NX0:1ol6Mi:aldUJ5vwQiudOU40N_TmickoPid5kWcu9MZpYDfk19o', '2022-11-02 10:32:00.839685');

-- --------------------------------------------------------

--
-- Table structure for table `study_materials`
--

DROP TABLE IF EXISTS `study_materials`;
CREATE TABLE IF NOT EXISTS `study_materials` (
  `material_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `subject_name` varchar(255) NOT NULL,
  `uploded_file` varchar(100) DEFAULT NULL,
  `uplode_photo` varchar(100) DEFAULT NULL,
  `Published_date` date DEFAULT NULL,
  `updated_date` date DEFAULT NULL,
  PRIMARY KEY (`material_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `study_materials`
--

INSERT INTO `study_materials` (`material_id`, `title`, `subject_name`, `uploded_file`, `uplode_photo`, `Published_date`, `updated_date`) VALUES
(14, '  History of Rajasthan', 'Emperor', 'materials/Django-QA-1_9LSc5W1.pdf', 'images/django_2DZ1oOG.jpeg', '2022-10-26', '2022-10-27'),
(10, ' fluter', 'vijay', 'materials/Udemy_Practice_Notes_j892sky.pdf', 'images/cXsPo0XR_400x400_tJTlXhM.jpg', '2022-10-25', '2022-10-26'),
(12, ' python', 'djnaao', 'materials/Udemy_Practice_Notes_KFfHHvG.pdf', 'images/django_jXtdqLV.jpeg', '2022-10-26', '2022-10-26'),
(4, ' cloud', 'aws', 'materials/Udemy_Practice_Notes.pdf', 'images/images_1.jpg', '2022-10-22', '2022-10-25'),
(13, 'python', 'functions', 'materials/Python.NEXTGEN_r1HYaTe.pdf', 'images/Django-4_AHQHggd.jpg', '2022-10-26', '2022-10-26'),
(6, '               python', 'views', 'materials/fico_material_WdM248T.pdf', 'images/fico_QilTNWG.jpg', '2022-10-22', '2022-10-25'),
(7, '   asdfghj', 'functions', 'materials/fico_material_jbWZxvS.pdf', 'images/logo_pyton.gif', '2022-10-22', '2022-10-25'),
(9, ' MBA', 'Fico', 'materials/fico_material.pdf', 'images/python_WhFhbBZ.jpg', '2022-10-25', '2022-10-25');

-- --------------------------------------------------------

--
-- Table structure for table `upsc_mock_test_papers`
--

DROP TABLE IF EXISTS `upsc_mock_test_papers`;
CREATE TABLE IF NOT EXISTS `upsc_mock_test_papers` (
  `mock_test_id` int(11) NOT NULL AUTO_INCREMENT,
  `mock_test_title` varchar(255) NOT NULL,
  `mock_subject_name` varchar(255) NOT NULL,
  `uploded_file` varchar(100) DEFAULT NULL,
  `test_date` date NOT NULL,
  `test_updated` date NOT NULL,
  `upload_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mock_test_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `upsc_mock_test_papers`
--

INSERT INTO `upsc_mock_test_papers` (`mock_test_id`, `mock_test_title`, `mock_subject_name`, `uploded_file`, `test_date`, `test_updated`, `upload_image`) VALUES
(1, 'django', 'views', 'materials/Django-QA-1_gP8IBff.pdf', '2022-10-20', '2022-10-20', 'images/images_1_VZJtVI1.jpg'),
(2, 'python', 'oopss', 'materials/Udemy_Practice_Notes_6knd1wV.pdf', '2022-10-22', '2022-10-22', 'images/django_ooHgk5f.jpeg'),
(5, 'python', 'oops', 'materials/Python_Programming_Planner_Syllabus.pdf', '2022-10-27', '2022-10-27', 'images/Django-4_k9Wqgmm.jpg'),
(4, 'python', 'functions', 'materials/javascript-and-jquery-syllabus_yGYtiIX.pdf', '2022-10-26', '2022-10-26', 'images/images_1_UgUC6hl.jpg'),
(6, 'asdfghj', 'advanced', 'materials/javascript-and-jquery-syllabus_65ApDGj.pdf', '2022-10-27', '2022-10-27', 'images/cXsPo0XR_400x400_ngAabZW.jpg'),
(7, 'python', 'django', 'materials/fico_material_cBGw41o.pdf', '2022-10-27', '2022-10-27', 'images/images.jpg'),
(8, 'python', 'ddk', 'materials/Python_Ratan_CompleteMaterial_nLjTq5X.pdf', '2022-10-27', '2022-10-27', 'images/download_PRFBxY5.jpg'),
(9, 'python', 'django', 'materials/fico_material_UcFlD6a.pdf', '2022-10-27', '2022-10-27', 'images/fico_6fLdPfK.jpg'),
(10, 'python', 'django', 'materials/Python.NEXTGEN_Jxrl26R.pdf', '2022-10-27', '2022-10-27', 'images/images_1_RCj8Om5.jpg'),
(11, 'python', 'django', 'materials/cb88-java-logo-001_nv82Hd0.jpg', '2022-10-27', '2022-10-27', 'images/images_5NTKU89.jpg'),
(12, 'python', 'django', 'materials/fico.jpg', '2022-10-27', '2022-10-27', 'images/images_1_zCVRuda.jpg'),
(13, 'python', 'oops', 'materials/fico_zCVqRAc.jpg', '2022-10-27', '2022-10-27', 'images/images_DxWdoNb.jpg'),
(14, 'python', 'oops', 'materials/fico_material_gUbdtu0.pdf', '2022-10-27', '2022-10-27', 'images/fico_byjeTtk.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `upsc_videos`
--

DROP TABLE IF EXISTS `upsc_videos`;
CREATE TABLE IF NOT EXISTS `upsc_videos` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `video_title` varchar(255) NOT NULL,
  `subject_name` varchar(255) NOT NULL,
  `uplode_video` varchar(100) DEFAULT NULL,
  `video_link` varchar(255) DEFAULT NULL,
  `uplode_date` date DEFAULT NULL,
  `updated_date` date NOT NULL,
  `videos_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=MyISAM AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `upsc_videos`
--

INSERT INTO `upsc_videos` (`video_id`, `video_title`, `subject_name`, `uplode_video`, `video_link`, `uplode_date`, `updated_date`, `videos_image`) VALUES
(2, 'java', 'Etherium', 'videos/o7april1st_cls.mp4', ' https://bit.ly/3GRc7JX', '2022-10-20', '2022-10-21', NULL),
(47, 'History', 'Emporer', '', 'https://youtube.com/embed/hYFzyK9ExuM', '2022-10-26', '2022-10-27', 'images/logo_pyton_81OIQPF.gif'),
(18, 'python', 'functions', 'videos/video1689242505_g6rmgLD.mp4', '', '2022-10-25', '2022-10-26', 'images/cb88-java-logo-001_dD8gBAo.jpg'),
(24, 'MBA', 'fico', 'videos/o7thapril01st_cls_rzkgqua.mp4', 'https://youtube.com/embed/3Arj5zlUPG4', '2022-10-25', '2022-10-25', 'images/babu_0FULlSy.jpg'),
(42, 'python', 'part-78', 'videos/o8thapril01st_cls_LR70Hu8.mp4', 'https://youtube.com/embed/hBh_CC5y8-s', '2022-10-26', '2022-10-26', 'images/Django-4.jpg'),
(43, 'django', 'part-1', 'videos/o7thapril01st_cls_DKnO6St.mp4', NULL, '2022-10-26', '2022-10-26', 'images/django_OdtkSIj.jpeg'),
(44, 'python', 'python', 'videos/o7april1st_cls_5eIgs82.mp4', '', '2022-10-26', '2022-10-26', 'images/babu_PWIHY4n.jpg'),
(45, 'python', 'asp', 'videos/o7april1st_cls_H40bGVq.mp4', NULL, '2022-10-26', '2022-10-26', 'images/WhatsApp_gxJMhha.jpeg'),
(46, 'python', 'hacking', 'videos/o7april1st_cls_yuMR027.mp4', 'https://youtube.com/embed/hBh_CC5y8-s', '2022-10-26', '2022-10-26', 'images/cXsPo0XR_400x400_kb1yByW.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
