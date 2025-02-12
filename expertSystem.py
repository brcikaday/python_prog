# STUDENT COURSE ADVISOR

import tkinter as tk


courses = [
    {"name": "Python Basics", "category": "Programming", "level": "Beginner", "career": "Software Developer"},
    {"name": "Web Development", "category": "Web Design", "level": "Beginner", "career": "Frontend Developer"},
    {"name": "Data Science Intro", "category": "Data Analysis", "level": "Beginner", "career": "Data Analyst/Scientist"},
    {"name": "Advanced Java", "category": "Programming", "level": "Advanced", "career": "Backend Developer"},
    {"name": "UI/UX Design Basics", "category": "Design", "level": "Beginner", "career": "UI/UX Designer"},
    {"name": "Machine Learning Fundamentals", "category": "Data Analysis", "level": "Intermediate", "career": "Data Scientist"},
    {"name": "Cloud Computing Essentials", "category": "Cloud Computing", "level": "Beginner", "career": "Cloud Engineer"},
    {"name": "Cybersecurity Basics", "category": "Cybersecurity", "level": "Beginner", "career": "Cybersecurity Analyst"},
    {"name": "React for Beginners", "category": "Web Development", "level": "Beginner", "career": "Frontend Developer"},
    {"name": "DevOps Practices", "category": "Software Development", "level": "Advanced", "career": "DevOps Engineer"},
    {"name": "Digital Marketing Strategy", "category": "Marketing", "level": "Intermediate", "career": "Digital Marketer"},
    {"name": "Blockchain Essentials", "category": "Blockchain", "level": "Beginner", "career": "Blockchain Developer"},
    {"name": "Mobile App Development", "category": "Programming", "level": "Intermediate", "career": "Mobile Developer"},
    {"name": "Game Development with Unity", "category": "Game Development", "level": "Beginner", "career": "Game Developer"},
    {"name": "Big Data Analytics", "category": "Data Analysis", "level": "Advanced", "career": "Big Data Engineer"},
    {"name": "AWS Certified Solutions Architect", "category": "Cloud Computing", "level": "Advanced", "career": "Cloud Architect"},
    {"name": "Penetration Testing", "category": "Cybersecurity", "level": "Advanced", "career": "Ethical Hacker"},
    {"name": "Adobe Photoshop Masterclass", "category": "Design", "level": "Intermediate", "career": "Graphic Designer"},
    {"name": "Leadership and Team Management", "category": "Management", "level": "Intermediate", "career": "Team Leader"},
    {"name": "AI for Beginners", "category": "Artificial Intelligence", "level": "Beginner", "career": "AI Researcher"}
]


def recommend_course(interest, level, goal):
    recommendations = []
    for course in courses:
        if interest.lower() in course["category"].lower() and level.lower() == course["level"].lower():
            recommendations.append(course["name"])
        elif goal.lower() in course["career"].lower():
            recommendations.append(course["name"])

    return recommendations


def get_recommendations():
    interest = interest_entry.get()
    level = level_entry.get()
    goal = goal_entry.get()

    recommended_course = recommend_course(interest,level,goal)

    if recommended_course:
        text_box.delete("1.0",tk.END)
        text_box.insert("1.0",f'Recoomendations are : \n' .join(recommended_course))
    else:
        text_box.insert("1.0","Sorry course cannot be found")


root = tk.Tk()
root.title("Course Advisor")


tk.Label(root, text="What is your interest (eg. programming, designing etc):").grid(row=0, column=0, padx=10, pady=5)
interest_entry = tk.Entry(root)
interest_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="What level are you , beginner or advanced:").grid(row=1, column=0, padx=10, pady=5)
level_entry = tk.Entry(root)
level_entry.grid(row=1, column=1, padx=10, pady=5)   

tk.Label(root, text="What is Your Career Goal:").grid(row=2, column=0, padx=10, pady=5)
goal_entry = tk.Entry(root)
goal_entry.grid(row=2, column=1, padx=10, pady=5)


submit_button = tk.Button(root, text="Get Recommendations", command=get_recommendations)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

text_box = tk.Text(root, height=7, width=70) 
text_box.grid(row=4 ,padx =10,pady=5 )


root.mainloop()

