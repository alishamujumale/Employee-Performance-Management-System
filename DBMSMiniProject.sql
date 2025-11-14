CREATE DATABASE employee_performance;

USE employee_performance;

CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
);

CREATE TABLE employee (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    dept VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE performance (
    perf_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    task VARCHAR(255),
    rating INT,
    remarks VARCHAR(255),
    date DATE,
    FOREIGN KEY (emp_id) REFERENCES employee(emp_id)
);
