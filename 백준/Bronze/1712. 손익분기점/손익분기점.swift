import Foundation
let n = (readLine()?.split(separator: " ").map{ Int($0)! })!
let A = n[0]
let B = n[1]
let C = n[2]

if(B>=C){
    print("-1")
} else{
    print("\((A / (C-B)) + 1)")
}