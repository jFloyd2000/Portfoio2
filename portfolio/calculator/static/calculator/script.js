function nextPage(){
	a = document.getElementById("inputOne").value;
	b = document.getElementById("inputTwo").value;
	c = document.getElementById("inputThree").value;
	path = "solve/" + a + "/" + b + "/" + c;
	window.location.href = path;
}
function homePage(){
	window.location.href = "../../../";
}
