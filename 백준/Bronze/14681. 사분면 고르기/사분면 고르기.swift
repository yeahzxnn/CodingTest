//첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 
//다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
let lineX = readLine()!
let lineY = readLine()!
let x = Int(lineX)!
let y = Int(lineY)!

if(x>=1){
    if(y>=1){
        print("1")
    }else{
        print("4")
    }
}else {
    if(y>=1){
        print("2")
    }else{
        print("3")
    }
}