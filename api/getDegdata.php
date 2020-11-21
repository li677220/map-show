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


$attr = $data["attr"];
$position = $data["position"];

$Obj = new Obj($location, $position);
$arr = array();
$po = "test";
$sql = 'select ' . $attr . ',count(' . $attr . ') from ' . $position . ' group by ' . $attr . ' order by count(' . $attr . ') DESC';
$result = $connect->query($sql);
$i = 0;


for ($i = 1; $i < 7; $i++) {
  $row = mysqli_fetch_array($result);
  $arr['value'] = $row[1];
  $arr['name'] = $row[0];
  $Obj->datalist[] = $arr;
}
echo json_encode($Obj);
$connect->close();
