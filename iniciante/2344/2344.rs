use std::io;

fn main() {
    println!("{}", regra_negocio(input()));
}

fn input() -> i32 {
    let mut n:String = String::new();
    io::stdin().read_line(&mut n).expect("msg");
    return n.trim().parse::<i32>().expect("msg");
}

fn regra_negocio(n: i32) -> String {
    return match n {
        0 => "E".to_string(),
        1..=35 => "D".to_string(),
        36..=60 => "C".to_string(),
        61..=85 => "B".to_string(),
        86..=100 => "A".to_string(),
        _ => "Valor fora do intervalo".to_string(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn t1(){
        let r:String = regra_negocio(12);
        assert_eq!(r, "D");
    }
    #[test]
    fn t2(){
        let r:String = regra_negocio(87);
        assert_eq!(r, "A");
    }
    #[test]
    fn t3(){
        let r:String = regra_negocio(0);
        assert_eq!(r, "E");
    }
}