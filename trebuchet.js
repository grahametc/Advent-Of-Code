const fs = require('fs');
let data = [];
let numbs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const regexNum = /[0-9]/;
let filter = [];
let temp = "";
let temp2 = "";
let final = "";
let total = 0;
const fileContent = fs.readFileSync("input.txt", "utf-8");

data = fileContent.split('\n').map(line => line.trim());



for(let i = 0; i < data.length; i++){
    for(let j = 0; j < data[i].length; j++){
        if(regexNum.test(data[i][j])){
            temp = data[i][j];
        }
    }
    for(let z = data[i].length; z >= 0; z--){
        if(regexNum.test(data[i][z])){
            temp2 = data[i][z];
        }
    }
    final = temp2 + temp;
    final = parseInt(final);
    filter[i] = final;
}

for(let f = 0; f < filter.length; f++){
    total += filter[f];
}
console.log(total);