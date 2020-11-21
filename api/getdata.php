<?php
require_once "database.php";
require_once "object.php";

$data = new Obj("haha ", "123456");

$sql = "SELECT * FROM `golang` ORDER BY `JobID` LIMIT 0, 1000";
$result = $connect->query($sql);

$arr = [];
if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    $JobID = $row["JobID"];
    // var_dump($JobID);
    array_push($arr, $JobID);
  }
} else {
  echo "错误";
}
// var_dump($arr); //arr具体元素
// echo $arr; //Array
echo json_encode($arr);
$connect->close();
