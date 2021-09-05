-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema openmics_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema openmics_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `openmics_schema` DEFAULT CHARACTER SET utf8 ;
USE `openmics_schema` ;

-- -----------------------------------------------------
-- Table `openmics_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `openmics_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openmics_schema`.`openmics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `openmics_schema`.`openmics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `venue` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  `date` DATE NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_openmics_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_openmics_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `openmics_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openmics_schema`.`table1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `openmics_schema`.`table1` (
)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
