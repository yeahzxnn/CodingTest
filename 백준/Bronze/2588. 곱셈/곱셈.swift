let input1 = Int(readLine()!)!
let input2 = Int(readLine()!)!

let three = input1 * (input2 % 10)
let four = input1 * (input2 % 100 - input2 % 10) / 10
let five = input1 * (input2 / 100)
print(three)
print(four)
print(five)
print(input1 * input2)