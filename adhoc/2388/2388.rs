use std::io;
use std::convert::TryInto;
use std::str::FromStr;

fn main() {
    let n: i32 = input();
    let v: Vec<Vec<i32>> = sequencia(n);
    let distancia: i32 = regra_negocio(v);
    println!("{}", distancia);
}

fn input() -> i32 {
    let mut n:String = String::new();
    io::stdin().read_line(&mut n).expect("msg");
    return n.trim().parse::<i32>().expect("msg");
}

fn input_vec() -> Vec<i32> {
    let mut _input_string:String = String::new();
    io::stdin().read_line(&mut _input_string).expect("msg");
    return _input_string.split_whitespace().map(|part|{
        i32::from_str(part).unwrap()
    }).collect();
}

fn sequencia(n: i32) -> Vec<Vec<i32>> {
    let mut v: Vec<Vec<i32>> = Vec::new();
    while v.iter().count() <= (n-1).try_into().unwrap() {
        v.push(input_vec());
    }
    return v;
}

fn regra_negocio(mut v: Vec<Vec<i32>>) -> i32 {
    let mut distancia_total: i32 = 0;
    for i in &mut v {
        distancia_total += i[0] * i[1];
    }
    return distancia_total;
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn t1(){
        let result: i32 = regra_negocio(vec![
            vec![10,0],
            vec![55,12],
            vec![75,120]
        ]);
        assert_eq!(result, 9660);
    }
    #[test]
    fn t2(){
        let result: i32 = regra_negocio(vec![
            vec![45,46],
            vec![46,101],
            vec![7,2],
            vec![95,104],
            vec![12,107],
            vec![78,29],
            vec![10,26],
            vec![52,86],
            vec![13,79],
            vec![1,107]
        ]);
        assert_eq!(result, 26022);
    }
    #[test]
    fn t3(){
        let result: i32 = regra_negocio(vec![
            vec![37,24],
            vec![68,69],
            vec![28,26],
            vec![79,8],
            vec![36,0],
            vec![50,71],
            vec![13,68],
            vec![87,113]
        ]);
        assert_eq!(result, 21205);
    }
}