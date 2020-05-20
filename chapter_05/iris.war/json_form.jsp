<script>
  function classify(){
	// Sending and receiving data in JSON format using POST method
	//
	var pl = parseFloat(document.getElementById("pl").value);
	var pw = parseFloat(document.getElementById("pw").value);
	var sl = parseFloat(document.getElementById("sl").value);
	var sw = parseFloat(document.getElementById("sw").value);
	
	var xhr = new XMLHttpRequest();
	var url = "http://127.0.0.1:5000/classify";
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        //alert(json.especies);
        document.getElementById("category").innerHTML = "Category: " + json.especies;
        //console.log(json.email + ", " + json.password);
      }
	};
 	var data = JSON.stringify([{"pl":pl, "pw":pw, "sl":sl, "sw":sw}]);
	xhr.send(data);
  }
</script>

<form method="post">
<p>Petal Length (cm):
<br/>
<input type="text" name="pl" id="pl">
</p>
<p>Petal Width (cm):
<br/>
<input type="text" name="pw" id="pw">
</p>
<p>Sepal Length (cm):
<br/>
<input type="text" name="sl" id="sl">
</p>
<p>Sepal Width (cm):
<br/>
<input type="text" name="sw" id="sw">
</p>
<p><input type="button" value="Classify JSON" onclick="classify()">	
</form> 
<p id="category"></p>
