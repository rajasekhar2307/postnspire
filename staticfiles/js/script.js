const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const cpass = document.getElementById('cpass');



//functions to show error and sucess
function showError(input,message){
	if(input!= null){
	const formcontrol = input.parentElement;
	formcontrol.className = 'formcontrol error';
	const small = formcontrol.querySelector('small');
	small.innerText = message;

	}
}

//show green
function showSuccess(input){
	const formcontrol = input.parentElement;
	formcontrol.className = 'formcontrol success';

}
//function to check if an email is valid....
function checkEmail(){
	 const re = /^[^ ]+@[^ ]+\.[a-z]{2,}$/;
    //return re.test(String(email).toLowerCase());//i need to write notes about this....
    console.log(email.value)
    if(email.value.match(re)){
    	console.log("Valid")
    	showSuccess(email);
    }else{
    	console.log("Invalid")
    	showError(email,`Enter a valid email`);
    }

}
//function to check lenght
function checkUsername(){
	if(username.value.length < 4){
		showError(username,`should be min length 4`);
	}else if(username.value.length > 20){
		showError(username,`cannot be more than 20`);
	}else
	showSuccess(username);
}

function checkLength(){
	if(password.value.length < 7){
		showError(password,`should be min 8`);
	}else
	showSuccess(password);
}


function checkRequired(inputArr) {
  inputArr.forEach(function(input) {
    if (input.value.trim() === '') {
      showError(input, `${getFieldName(input)} is required`);
    } else {
      showSuccess(input);
    }
  });
}
//function to check Passwords are same or not
function checkPass(){
	console.log(password.value);
	console.log(cpass.value);

	if(password.value!=cpass.value){
		showError(cpass,'Passwords don\'t match');
	}
	else{
		showSuccess(cpass);
	}
}


// // Get fieldname
// function getFieldName(input) {
//   return input.id.charAt(0).toUpperCase() + input.id.slice(1);
// }




//adding event listeners
// form.addEventListener('submit',function(e){
// 	e.preventDefault();

// 	checkRequired([username,email,password,cpass]);
// 	checkLength(username,3,15);
// 	checkLength(password,6,25);
// 	checkEmail(email);
// 	checkPass(password,cpass);
// });
const collapsibles = document.querySelectorAll(".collapsible");
collapsibles.forEach((item) =>
  item.addEventListener("click", function () {
    this.classList.toggle("collapsible--expanded");
  })
);
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});
