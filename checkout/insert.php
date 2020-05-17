<?php
$car_id = $_POST['car_id'];
$date_from = $_POST['d_from'];
$date_to = $_POST['d_to'];
$cin = $_POST['disp_id'];
$org = $_POST['org'];

if (!empty($car_id) || !empty($date_from) || !empty($date_to) || !empty($cin)) {
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "caraccess_db";
    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
    if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } else {
     $SELECT = "SELECT car From requests_db Where car = ? Limit 1";
     $INSERT = "INSERT Into requests_db (car, from_date, to_date, cin, organization) values(?, ?, ?, ?, ?)";
     //Prepare statement
     $stmt = $conn->prepare($SELECT);
     $stmt->bind_param("s", $car_id);
     $stmt->execute();
     $stmt->bind_result($car_id);
     $stmt->store_result();
     $rnum = $stmt->num_rows;
     if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->bind_param("sssss", $car_id, $date_from, $date_to, $cin, $org);
      $stmt->execute();
      echo "New record inserted sucessfully";
     } else {
      echo "This car is already reserved !";
     }
     $stmt->close();
     $conn->close();
    }
} else {
 echo "All field are required";
 die();
}
?>
