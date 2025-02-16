fn main() {
    let mut frase = String::with_capacity(50);
    frase.push_str("AMO FAZER EXERCICIO NO URI");

    println!("<{}>", frase);
    println!("<{:>30}>", frase);
    println!("<{:.20}>", frase);
    println!("<{:<20}>", frase);
    println!("<{:<30}>", frase);
    println!("<{:.30}>", frase);
    println!("<{:>30.20}>", frase);
    println!("<{:<30.20}>", frase);
}