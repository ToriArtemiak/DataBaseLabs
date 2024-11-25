CREATE SCHEMA IF NOT EXISTS `CarSalesDBLAB3` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `CarSalesDBLAB3` ;

CREATE TABLE IF NOT EXISTS `CarTypes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dealerships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idx_dealership_location` (`location`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `sellers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `dealership_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idx_seller_name` (`name`),
  INDEX `dealership_id` (`dealership_id`),
  CONSTRAINT `sellers_ibfk_1`
    FOREIGN KEY (`dealership_id`)
    REFERENCES `dealerships` (`id`)
    ON DELETE SET NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `cars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(255) NOT NULL,
  `brand` VARCHAR(255) NULL DEFAULT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `country` VARCHAR(255) NULL DEFAULT NULL,
  `mileage` INT NULL DEFAULT NULL,
  `year` YEAR NOT NULL,
  `car_type_id` INT NULL DEFAULT NULL,
  `seller_id` INT NULL DEFAULT NULL,
  `dealership_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `cars_ibfk_1`
    FOREIGN KEY (`car_type_id`)
    REFERENCES `CarTypes` (`id`),
  CONSTRAINT `cars_ibfk_2`
    FOREIGN KEY (`seller_id`)
    REFERENCES `sellers` (`id`),
  CONSTRAINT `cars_ibfk_3`
    FOREIGN KEY (`dealership_id`)
    REFERENCES `dealerships` (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idx_user_email` (`email`)
) ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `CarFeatures` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `feature_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FeatureOptions` (
  `id` INT NOT NULL AUTO_INCREMENT,
   `feature_id` INT NULL DEFAULT NULL,
  `option_value` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `featureoptions_ibfk_1`
     FOREIGN KEY (`feature_id`)
     REFERENCES `CarFeatures` (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `CarFeatureValues` (
   `car_id` INT NOT NULL,
   `feature_id` INT NOT NULL,
   `option_id` INT NULL DEFAULT NULL,
   PRIMARY KEY (`car_id`, `feature_id`),
    INDEX `feature_id` (`feature_id` ASC) VISIBLE,
  INDEX `option_id` (`option_id` ASC) VISIBLE,
   CONSTRAINT `carfeaturevalues_ibfk_1`
    FOREIGN KEY (`car_id`)
    REFERENCES `Cars` (`id`),
  CONSTRAINT `carfeaturevalues_ibfk_2`
    FOREIGN KEY (`feature_id`)
    REFERENCES `CarFeatures` (`id`),
  CONSTRAINT `carfeaturevalues_ibfk_3`
    FOREIGN KEY (`option_id`)
    REFERENCES `FeatureOptions` (`id`)

) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `CarPhotos` (
   `id` INT NOT NULL AUTO_INCREMENT,
  `car_id` INT NULL DEFAULT NULL,
  `photo_url` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `car_id` (`car_id` ASC) VISIBLE,
  CONSTRAINT `carphotos_ibfk_1`
    FOREIGN KEY (`car_id`)
    REFERENCES `Cars` (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Comments` (
   `id` INT NOT NULL AUTO_INCREMENT,
  `car_id` INT NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `comment_text` TEXT NULL DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `car_id` (`car_id` ASC) VISIBLE,
  INDEX `user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `comments_ibfk_1`
    FOREIGN KEY (`car_id`)
    REFERENCES `Cars` (`id`),
  CONSTRAINT `comments_ibfk_2`
    FOREIGN KEY (`user_id`)
    REFERENCES `Users` (`id`)
) ENGINE = InnoDB;


INSERT INTO Users (username, email, password, phone_number)
VALUES
('john_doe', 'john.doe@example.com', 'password123', '1234567890'),
('jane_smith', 'jane.smith@example.com', 'securepass', '0987654321'),
('alex_brown', 'alex.brown@example.com', 'alex1234', '1112223333'),
('maria_white', 'maria.white@example.com', 'maria5678', '4445556666'),
('chris_black', 'chris.black@example.com', 'chrispass', '7778889999'),
('linda_gray', 'linda.gray@example.com', 'linda3456', '9998887777'),
('peter_blue', 'peter.blue@example.com', 'blue12345', '5554443333'),
('susan_green', 'susan.green@example.com', 'greenpass', '6667778888'),
('tom_yellow', 'tom.yellow@example.com', 'yellow7890', '2223334444'),
('emma_pink', 'emma.pink@example.com', 'pinkpass123', '1114447777');

INSERT INTO DealerShips (name, location)
VALUES
('City Motors', 'New York, NY'),
('Auto World', 'San Francisco, CA'),
('Highway Auto', 'Los Angeles, CA'),
('Urban Cars', 'Chicago, IL'),
('Luxury Rides', 'Miami, FL'),
('Speed Wheels', 'Houston, TX'),
('Family Cars', 'Phoenix, AZ'),
('Off-Road Adventures', 'Denver, CO'),
('Green Mobility', 'Seattle, WA'),
('Budget Auto', 'Las Vegas, NV');

INSERT INTO Sellers (name, dealership_id)
VALUES
('Mike Johnson', 1),
('Alice Cooper', 2),
('Steve Rogers', 3),
('Nataly Jennings', 4),
('Bruce Wayne', 5),
('Clark Kent', 6),
('Diana Prince', 7),
('Barry Allen', 8),
('Arthur Curry', 9),
('Victor Stone', 10);

INSERT INTO CarTypes (type_name)
VALUES
('Sedan'),
('SUV'),
('Truck'),
('Convertible'),
('Coupe'),
('Hatchback'),
('Minivan'),
('Wagon'),
('Electric'),
('Diesel');

INSERT INTO Cars (model, brand, price, country, mileage, year, car_type_id, seller_id, dealership_id)
VALUES
('Model S', 'Tesla', 79999.99, 'USA', 10000, 2023, 1, 1, 1),
('Civic', 'Honda', 24999.99, 'Japan', 5000, 2022, 2, 2, 2),
('F-150', 'Ford', 39999.99, 'USA', 20000, 2021, 3, 3, 3),
('Camry', 'Toyota', 27999.99, 'Japan', 12000, 2022, 1, 4, 4),
('Mustang', 'Ford', 55999.99, 'USA', 8000, 2023, 5, 5, 5),
('Corolla', 'Toyota', 21999.99, 'Japan', 15000, 2021, 1, 6, 6),
('Wrangler', 'Jeep', 40999.99, 'USA', 9000, 2022, 2, 7, 7),
('Model 3', 'Tesla', 59999.99, 'USA', 7000, 2023, 9, 8, 8),
('Ranger', 'Ford', 32999.99, 'USA', 18000, 2021, 3, 9, 9),
('Odyssey', 'Honda', 35999.99, 'Japan', 22000, 2022, 7, 10, 10);

INSERT INTO CarFeatures (feature_name)
VALUES
('Color'),
('Transmission'),
('Fuel Type'),
('Sunroof'),
('GPS'),
('Leather Seats'),
('Heated Seats'),
('Bluetooth'),
('Backup Camera'),
('Alloy Wheels');

INSERT INTO FeatureOptions (feature_id, option_value)
VALUES
(1, 'Red'),
(1, 'Blue'),
(1, 'Black'),
(1, 'White'),
(2, 'Automatic'),
(2, 'Manual'),
(3, 'Electric'),
(3, 'Gasoline'),
(3, 'Diesel'),
(3, 'Hybrid');

INSERT INTO CarFeatureValues (car_id, feature_id, option_id)
VALUES
(1, 1, 1),
(1, 2, 5),
(1, 3, 7),
(2, 1, 2),
(2, 2, 6),
(2, 3, 8),
(3, 1, 3),
(3, 2, 6),
(3, 3, 9),
(4, 1, 4);

INSERT INTO CarPhotos (car_id, photo_url)
VALUES
(1, 'https://example.com/photos/tesla_model_s.jpg'),
(2, 'https://example.com/photos/honda_civic.jpg'),
(3, 'https://example.com/photos/ford_f150.jpg'),
(4, 'https://example.com/photos/toyota_camry.jpg'),
(5, 'https://example.com/photos/ford_mustang.jpg'),
(6, 'https://example.com/photos/toyota_corolla.jpg'),
(7, 'https://example.com/photos/jeep_wrangler.jpg'),
(8, 'https://example.com/photos/tesla_model_3.jpg'),
(9, 'https://example.com/photos/ford_ranger.jpg'),
(10, 'https://example.com/photos/honda_odyssey.jpg');

INSERT INTO Comments (car_id, user_id, comment_text, created_at)
VALUES
(1, 1, 'Amazing car!', NOW()),
(2, 2, 'Very fuel efficient.', NOW()),
(3, 3, 'Perfect for long trips.', NOW()),
(4, 4, 'Comfortable and reliable.', NOW()),
(5, 5, 'Great performance!', NOW()),
(6, 6, 'Affordable and practical.', NOW()),
(7, 7, 'Perfect for off-road adventures.', NOW()),
(8, 8, 'Environmentally friendly.', NOW()),
(9, 9, 'Great value for the price.', NOW()),
(10, 10, 'Ideal for family use.', NOW());
