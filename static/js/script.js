const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const cpass = document.getElementById('cpass');

//functions to show error and sucess
function showError(input,message){
	const formcontrol = input.parentElement;
	formcontrol.className = 'formcontrol error';
	const small = formcontrol.querySelector('small');
	small.innerText = message;
}

//show green
function showSuccess(input){
	const formcontrol = input.parentElement;
	formcontrol.className = 'formcontrol success';

}
//function to check if an email is valid....
function checkEmail(email){
	 const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    //return re.test(String(email).toLowerCase());//i need to write notes about this....
    if(re.test(email.value.trim())){
    	showSuccess(email);
    }else{
    	showError(email,`${getFieldName(email)} is not a valid email`);
    }

}
//function to check lenght
function checkLength(input,min,max){
	if(input.value.length < min){
		showError(input,`${getFieldName(input)} should be min ${min}`);
	}else if(input.value.length > max){
		showError(input,`${getFieldName(input)} cannot be more than ${max}`);
	}else
	showSuccess(input);
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
function checkPass(password,cpass){
	if(password.value!==cpass.value){
		showError(cpass,'Passwords don\'t match');
	}
}


// Get fieldname
function getFieldName(input) {
  return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}




//adding event listeners
form.addEventListener('submit',function(e){
	e.preventDefault();

	checkRequired([username,email,password,cpass]);
	checkLength(username,3,15);
	checkLength(password,6,25);
	checkEmail(email);
	checkPass(password,cpass);
});