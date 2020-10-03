BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `blog_comment` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`created_at`	date NOT NULL,
	`update_at`	date NOT NULL,
	`author`	varchar ( 100 ) NOT NULL,
	`content`	text NOT NULL,
	`article_id`	integer NOT NULL,
	FOREIGN KEY(`article_id`) REFERENCES `blog_article`(`id`) DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO `blog_comment` VALUES (1,'2020-09-29','2020-09-29','herman',' I am not sure but spring is best',1);
CREATE TABLE IF NOT EXISTS `blog_category` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 250 ) NOT NULL,
	`description`	text NOT NULL
);
INSERT INTO `blog_category` VALUES (1,'beauté','les laits de beautés');
INSERT INTO `blog_category` VALUES (2,'','');
CREATE TABLE IF NOT EXISTS `blog_article` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`created_at`	date NOT NULL,
	`update_at`	date NOT NULL,
	`title`	varchar ( 250 ) NOT NULL,
	`content`	text NOT NULL,
	`category_id`	integer NOT NULL,
	`image`	varchar ( 250 ) NOT NULL,
	FOREIGN KEY(`category_id`) REFERENCES `blog_category`(`id`) DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO `blog_article` VALUES (1,'2020-09-29','2020-09-29','first art','djando is good',2,'balalalalal');
CREATE INDEX IF NOT EXISTS `blog_comment_article_id_3d58bca6` ON `blog_comment` (
	`article_id`
);
CREATE INDEX IF NOT EXISTS `blog_article_category_id_7e38f15e` ON `blog_article` (
	`category_id`
);
COMMIT;
