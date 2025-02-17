import * as readline from 'readline';

const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

input.question('', (answer) => {
    const n:number = parseInt(answer, 10);
    
    if (!isNaN(n)){
        const r:number = ((n+1)*(n+2)/2)
        console.log(r);
    } else {
        console.log('ERRO');
    }

    input.close();
});
