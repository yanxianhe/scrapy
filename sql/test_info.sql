
USE `test`;

/*Table structure for table `test_info` */

DROP TABLE IF EXISTS `test_info`;

CREATE TABLE `test_info` (
  `id` varchar(254) NOT NULL COMMENT '表id',
  `storagetime` datetime DEFAULT NULL COMMENT '入库日期',
  `numb` int(12) NOT NULL COMMENT '排名',
  `start` int(32) NOT NULL COMMENT '综合得分',
  `info` varchar(512) DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
