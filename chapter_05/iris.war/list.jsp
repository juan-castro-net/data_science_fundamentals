<!DOCTYPE html>
<html>
<style>
table,th,td {
  border : 1px solid black;
  border-collapse: collapse;
}
th,td {
  padding: 5px;
}
</style>
<body>

<button type="button" onclick="loadXMLDoc()">Get my Iris flowers classification from Python Flask</button>
<br><br>
<table id="demo"></table>

<script>
function loadXMLDoc() {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      myFunction(this);
    }
  };
  xmlhttp.open("GET", "http://127.0.0.1:5000/list", true);
  xmlhttp.send();
}
function myFunction(data) {	
  var str = data.responseText;
  
  var x = JSON.parse(str);
  x = x.flowers;

  var table = "<tr><th>#</th><th>Petal Length</th><th>Petal Width</th>"
  table = table + "<th>Sepal Length</th><th>Setal Width</th><th>Class</th></tr>";

  for(var i=0; i<x.length; i=i+1){
  	 table += "<tr>";
  	 table += "<td>" + (i+1) + "</td>";
  	 table += "<td>" + x[i].pl + "</td>";
  	 table += "<td>" + x[i].pw + "</td>";
  	 table += "<td>" + x[i].sl + "</td>";
  	 table += "<td>" + x[i].sw + "</td>";
  	 table += "<td>" + x[i].class + "</td>"
  	 table += "</tr>";	
  }
  document.getElementById("demo").innerHTML = table;
}
</script>

</body>
</html>
