const option1 = document.getElementById("option1"),
      option2 = document.getElementById("option2"),
      option3 = document.getElementById("option3"),
      audio = document.getElementById("myAudio");  
var answer = 0;

const sounds = [
	new Audio('wronganswer.mp3'),
	new Audio('wronganswer2.webm'),
	new Audio('wronganswer3.m4a'),
	new Audio('wronganswer4.mp3')
];

function getRandomIntInclusive(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min + 1) + min);
}

function generate_equation(){ 
  var num1 = Math.floor(Math.random() * 8),
      num2 = Math.floor(Math.random() * 8),
      dummyAnswer1 = Math.floor(Math.random() * 25),
      dummyAnswer2 = Math.floor(Math.random() * 25),
      allAnswers = [],
      switchAnswers = [];

  answer = eval(num1 * num2);
  
  document.getElementById("num1").innerHTML = num1; 
  document.getElementById("num2").innerHTML = num2; 

  allAnswers = [answer, dummyAnswer1, dummyAnswer2];

  for (i = allAnswers.length; i--;){
    switchAnswers.push(allAnswers.splice(Math.floor(Math.random() * (i + 1)), 1)[0]);
  };

  option1.innerHTML = switchAnswers[0];
  option2.innerHTML = switchAnswers[1];
  option3.innerHTML = switchAnswers[2]; 

};

option1.addEventListener("click", function(){
    if(option1.innerHTML == answer){
      generate_equation();
    }
    else{
      sounds[getRandomIntInclusive(0, 3)].play();
    }
});

option2.addEventListener("click", function(){
    if(option2.innerHTML == answer){
      generate_equation();
    }
    else{
      sounds[getRandomIntInclusive(0, 3)].play();
    }
});

option3.addEventListener("click", function(){
    if(option3.innerHTML == answer){
     generate_equation();
    }
    else{
      sounds[getRandomIntInclusive(0, 3)].play();
    }
});

generate_equation()
