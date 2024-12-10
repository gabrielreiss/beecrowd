use std::io;

fn main() {
    println!("{}", regra_negocio(sequencia()));
}

fn input() -> i32 {
    let mut n:String = String::new();
    io::stdin().read_line(&mut n).expect("msg");
    return n.trim().parse::<i32>().expect("msg");
}

fn sequencia() -> Vec<i32> {
    let mut v: Vec<i32> = Vec::new();
    while v.iter().count() < 5 {
        v.push(input());
    }
    return v;
}

fn regra_negocio(v: Vec<i32>) -> i32 {
    return 
      v[0] * 300 
    + v[1] * 1500 
    + v[2] * 600
    + v[3] * 1000
    + v[4] * 150
    + 225
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn t1(){
        let r: i32 = regra_negocio(vec![1,1,1,1,1]);
        assert_eq!(r, 3775);
    }
    #[test]
    fn t2(){
        let r: i32 = regra_negocio(vec![2,2,2,2,2]);
        assert_eq!(r, 7325);
    }
}
