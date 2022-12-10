let inputArr = readLine()!.split(separator: " ").map{ Int($0)! }
var numH = inputArr[0]
var numM = inputArr[1]

if numM < 45 && numM != 45 {
    if numH == 0 {
        numH = 23
    } else {
        numH = numH - 1
    }
    
    numM = numM + 15
} else {
    numM = numM - 45
}

print(String(numH) + " " + String(numM))