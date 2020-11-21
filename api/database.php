<?php
$servername = "localhost";
$username = "root";
$pwd = "root";
$dbname = "test";
//1.建立连接
$connect = new mysqli($servername, $username, $pwd, $dbname);
if ($connect->connect_error) {
  die("连接失败：" . $connect->connect_error);
}

header("content-type:application/json");
