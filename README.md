# GradeCalculator
FinalGrades will calculate a numerical final grade for any course. 
- Input number of categories to consider for calculation.
- For each category, provide a numerical grade & the associcated weight the category has in the grade calcualtion.
- Example: If a Math course values each midterm exam as 16% of the final grade, then input 0.16 as the associated weight.
- For any category that collects grades for multiple assignments (e.g. Homework or Quizzes) you can either treat each assignment as its own category, thus increasing the total number of categories to consider, or calculate the aggregated score of all relevant assignments and input as a single category. If you choose to do the former, remember to split the assigned weight of the category evenly across all relevant assignments.


GPACalculator will calculate a numerical GPA based on Rutgers New Brunswick's grade assignment system: 
- A -> 4, B+ -> 3.5, B -> 3, C+ -> 2.5, C -> 2, D -> 1, F -> 0
- The resultant GPA is calculated on a 4.0 scale.
- Input the total number of completed semesters. Any courses taken during winter or summer sessions should be counted as separate semesters.
- For each semester, input your semester GPA according to your transcript along with the total number of credits taken during that semester that were for courses in which you received a letter grade. Any courses that were audited, pass / no credit, or do not receive a letter grade for any other reason should not be counted.
- After inputting the information for all completed semesters, you will have the option to fill in your letter grades for the current semester. If you want to see your current GPA, simply input "0" for the number of classes and your current GPA will be provided based on your previous inputs.
- You may used the current semester information to predict how your current semester will affect your GPA by inputting hypothetical letter grades into the required input spaces.
