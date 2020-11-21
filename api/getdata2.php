<?php
require_once "./database.php";
require_once "./object.php";

header('Content-Type: application/json;charset=utf-8');
header('Access-Control-Allow-Origin:*'); // *代表允许任何网址请求
header('Access-Control-Allow-Methods:POST,GET'); // 允许请求的类型
header('Access-Control-Allow-Credentials: true'); // 设置是否允许发送 cookies
header('Access-Control-Allow-Headers: Content-Type,Content-Length,Accept-Encoding,X-Requested-with, Origin'); // 设置允许自定义请求头的字段

$request_body = file_get_contents('php://input');
$data = json_decode($request_body, true);
// echo (gettype($data)); array



$location = $data["location"];
$position = $data["position"];
// echo json_encode($location);
// echo json_encode($position);

$Obj = new Obj($location, $position);
$arr = array();
$po = "test";
// $sql = "SELECT * FROM `golang` ORDER BY `JobID` LIMIT 0, 1000";
$sql = 'select JoblactionStr,count(JoblactionStr) from ' . $position . ' group by JoblactionStr order by count(JoblactionStr) DESC';
$result = $connect->query($sql);
$i = 0;
// while ($row = mysqli_fetch_array($result)) {
//   // echo $row[1];
//   // $data["location"] = $row["JoblactionStr"];
//   // $data["count"] = $row["count"];
//   // $Obj->data = $row["count"];
//   // $Obj->datalist["location"] = $row["JoblactionStr"];
//   // $Obj->datalist["count"] = $row["count"];
//   // $Obj->datalist = $arr;
//   // $data = new Data($row["JoblactionStr"], $row["count"]);
//   // $Obj->datalist . array_push($data);
//   // $Obj->datalist
//   // print($row["count"]);
//   echo json_encode(gettype($row));
//   $i++;
// }

for ($i = 1; $i < 7; $i++) {
  $row = mysqli_fetch_array($result);
  $arr['value'] = $row[1];
  $arr['name'] = $row[0];
  $Obj->datalist[] = $arr;

  // echo json_encode($arr);
}
echo json_encode($Obj);
// echo json_encode($data);
$connect->close();
