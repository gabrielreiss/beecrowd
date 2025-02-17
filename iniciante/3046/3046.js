"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline = require("readline");
var input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
input.question('', function (answer) {
    var n = parseInt(answer, 10);
    if (!isNaN(n)) {
        var r = ((n + 1) * (n + 2) / 2);
        console.log(r);
    }
    else {
        console.log('ERRO');
    }
    input.close();
});
