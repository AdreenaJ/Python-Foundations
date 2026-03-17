def job_skills_inventory():
    try:
        job={"back-end developer":["API management","Django","Flask","RESTful","SQL","System Architecture"],
        "Data Analyst":["NumPy","Pandas","Regression","Data Manipulation"],
        "Data Scientist":["NumPy","Pandas","Regression","Data Manipulation"],
        "Cloud Engineer":["Terraform","Pulumi","Crossplane","Docker"],
        "DevOps Developer":["Terraform","Pulumi","Crossplane","Docker"],
        "Automation Developer":["Terraform","Pulumi","Crossplane","Docker"],
        "Robotic Process Automation Developer":["BotCity","UiPath","Automation Anywhere","Blue Prism"],
        "Full-Stack developer":["front-end (HTML, CSS, JS, React/Angular)","back-end (Node.js, Python, Java,Ruby,PHP)",
        "database management (SQL, MongoDB)","DevOps (Git, Docker, AWS)","API Development","Version Control & Collaboration",
        "Web Fundamentals(HTTPS, CORS, OWASP)"],
        "Software developer":["Programming languages(e.g., Python, Java, JavaScript, C++)","Data Structures and Algorithms",
        "Databases & SQL(e.g., MySQL, PostgreSQL, MongoDB)","Version Control","Frameworks and Libraries(e.g.,React, Angular, or Django)",
        "Cloud Computing(e.g.,AWS,Azure,Google Cloud)","DevOps Practices(CI/CD, Docker,containerization)","System design and security"],
        "Software engineer":["Programming languages(e.g., Python, Java, JavaScript, C++)","Data Structures and Algorithms",
        "Databases & SQL(e.g., MySQL, PostgreSQL, MongoDB)","Version Control","Frameworks and Libraries(e.g.,React, Angular, or Django)",
        "Cloud Computing(e.g.,AWS,Azure,Google Cloud)","DevOps Practices(CI/CD, Docker,containerization)","System design and security"],
        }
        user_input=input("enter job role:")
        for i in job:
            if i.lower()==user_input.lower():
                print(f"Skills needed for {user_input} are: {job[i]}")
                return
        print("Job role not found.Please provide another job role.")
    except ValueError:
        print("Enter valid input!!")
if __name__=="__main__":
    job_skills_inventory()