import axios from "axios"
// import service from "@/utils/request"

export function GetData (data) {
  return axios({
    url: "/api/getdata2.php",
    method: "post",
    data
  })
}
export function GetSecData (data) {
  return axios({
    url: "/api/getDegdata.php",
    method: "post",
    data
  })
}