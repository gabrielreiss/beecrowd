use std::io;

fn main(){
    let a = input_dados();
    let m = input_dados();

    println!("{}", reverse_mean(a, m));
}

fn reverse_mean(a:i32, m:i32) -> i32{
    return (m * 2) - a;
}

fn input_dados() -> i32 {
    let mut a: String = String::new();
    io::stdin().read_line(&mut a).expect("ERRO: Ao ler a string");
    return a.trim().parse::<i32>().expect("ERRO: ao converter");
}