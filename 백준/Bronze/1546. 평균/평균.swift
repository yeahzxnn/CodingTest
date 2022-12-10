//일단 세준이는 자기 점수 중에 최댓값을 골랐다. 
//이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
//예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
//세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

let input = readLine()!
let scoreArr = readLine()!.split(separator: " ").map{ Int($0)!}
let maxScore = Double(scoreArr.max()!)
var sum: Double = 0 //합계는 변수니까, 그리고 타입 선언 해준 것.

for score in scoreArr{
    sum += Double(score) / maxScore * 100
}
print(sum/Double(scoreArr.count))