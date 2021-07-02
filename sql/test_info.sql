
USE `test`;

/*Table structure for table `src_h5_model` */
DROP TABLE IF EXISTS `src_h5_model`;

CREATE TABLE `src_h5_model` (
  `primaryKey` bigint(20) NOT NULL AUTO_INCREMENT,
  `top` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '2',
  `type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `classify` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `content` mediumtext COLLATE utf8mb4_unicode_ci,
  `record_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `record_id` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `record_date` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_id` varchar(18) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `order_number` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_have_preview` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '2',
  `preview` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `browse_number` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '0',
  `publisher` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`primaryKey`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=220 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

