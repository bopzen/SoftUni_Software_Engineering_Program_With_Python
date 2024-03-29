function solve(input) {
    let grades = {};
    for (let studentEntry of input) {
        let [name, grade, avgScore] = studentEntry.split(", ");
        name = name.replace("Student name: ", "");
        grade = Number(grade.replace("Grade: ", ""));
        avgScore = Number(avgScore.replace("Graduated with an average score: ", ""));
        let studentObj = {name, grade, avgScore};
        if (studentObj.avgScore >= 3) {
            if (!grades.hasOwnProperty(studentObj.grade + 1)) {
                grades[studentObj.grade + 1] = [];
            }
            grades[studentObj.grade + 1].push(studentObj);
        }
    }
    let sortedGrades = Object.keys(grades);
    for (const grade of sortedGrades) {
        console.log(`${grade} Grade`);
        let students = grades[grade];
        let names = [];
        let sumScore = 0;
        for (const student of students) {
            sumScore += student.avgScore;
            names.push(student.name);
        }
        console.log(`List of students: ${names.join(", ")}`);
        let avgScore = sumScore / names.length;
        console.log(`Average annual score from last year: ${avgScore.toFixed(2)} \n`);
    }
}

solve([
    "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
        "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
        "Student name: George, Grade: 8, Graduated with an average score: 2.83",
        "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
        "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
        "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
        "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
        "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
        "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
        "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
        "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
        "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
    ]
    );
solve([
    'Student name: George, Grade: 5, Graduated with an average score: 2.75',
    'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
    'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
    'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
    'Student name: John, Grade: 9, Graduated with an average score: 2.90',
    'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
    'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
    ]
    );