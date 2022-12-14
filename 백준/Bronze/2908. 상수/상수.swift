import Foundation

let input = readLine()!.split(separator: " ")
var A = Int(String(input[0].reversed()))!
var B = Int(String(input[1].reversed()))!

if(A>B){
    print(A)
} else{
    print(B)
}