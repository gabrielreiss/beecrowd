use std::io::{self, BufRead};

fn main(){
    let r: i32 = regra_negocio(input_dados(io::stdin().lock()));
    println!("{}", r);
}

fn input_dados<R: BufRead>(reader: R) -> i32 {
    let mut input: String = String::new();
    let mut reader = reader;
    reader.read_line(&mut input).expect("ERRO: ao ler.");
    return input.trim().parse::<i32>().expect("ERRO: ao converter para int");
}

fn regra_negocio(n: i32) -> i32{
    let r: i32 = ((n+1)*(n+2))/2;
    return r;
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Cursor;

    #[test]
    fn test_converter1(){
        let input: &str = "6";
        let cursor: Cursor<&str> = Cursor::new(input);
        let result: i32 = input_dados(cursor);
        assert_eq!(result, 6);
    }

    #[test]
    fn test_converter2(){
        let input: &str = "12";
        let cursor: Cursor<&str> = Cursor::new(input);
        let result: i32 = input_dados(cursor);
        assert_eq!(result, 12);
    }

    #[test]
    fn test_regra1(){
        let n:i32 = 6;
        let result: i32 = regra_negocio(n);
        assert_eq!(result, 28);
    }
    #[test]
    fn test_regra2(){
        let n:i32 = 12;
        let result: i32 = regra_negocio(n);
        assert_eq!(result, 91);
    }
}