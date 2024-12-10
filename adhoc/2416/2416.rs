use std::io;

fn main(){
    let a = coletar();

    let resultado = a[0] % a[1];

    println!("{}", resultado);
}

fn coletar() -> Vec<i32> {
    let mut str_number:String = String::new();
    io::stdin().read_line(&mut str_number).expect("msg");

    let teste: Vec<i32> = str_number
                                    .split_whitespace()
                                    .map(|s| s.trim()
                                        .parse::<i32>()
                                        .expect("msg"))
                                    .collect();

    return teste;
}
