use std::io;

fn main() {
    let mut str_a = String::new();
    let mut str_b = String::new();
    let mut str_c = String::new();
    let mut str_d = String::new();

    io::stdin().read_line(&mut str_a).expect("Não foi possível ler o primeiro valor");
    io::stdin().read_line(&mut str_b).expect("Não foi possível ler o segundo valor");
    io::stdin().read_line(&mut str_c).expect("Não foi possível ler o terceiro valor");
    io::stdin().read_line(&mut str_d).expect("Não foi possível ler o quarto valor");
    
    let a:i32 = str_a.trim().parse::<i32>().expect("Não foi possivel converter o primeiro valor");
    let b:i32 = str_b.trim().parse::<i32>().expect("Não foi possivel converter o segundo valor");
    let c:i32 = str_c.trim().parse::<i32>().expect("Não foi possivel converter o terceiro valor");
    let d:i32 = str_d.trim().parse::<i32>().expect("Não foi possivel converter o quarto valor");

    let diff:i32 = (a * b) - (c * d);

    println!("DIFERENCA = {}", diff);
}