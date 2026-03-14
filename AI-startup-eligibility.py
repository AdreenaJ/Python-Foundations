def get_valid_score(skill_name):
    while True:
        try:
            rating = int(input(f"Enter your {skill_name} skill level (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Error: Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input: Please enter a whole number.")
def check_yes_no(prompt):
    """Ensures the user only enters 'yes' or 'no'."""
    while True:
        # 1. Capture the actual user response here
        user_input = input(prompt).strip().lower() 
        
        # 2. Check the user_input, NOT the prompt
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            # This will now only run once per wrong answer
            print(f"Error: '{user_input}' is not valid. Please type 'yes' or 'no'.")
def eligibility_check():
    print("--------AI Startup Eligibility Bot----------------")
    print("--------Rating Scale: 1-5(1:beginner,2:intermediate,3:advanced,4:expert,5:expertise)----------------")
    try:
        print("--------Enter the Details----------------")
        
        print("-------Enter your skills----------------")
        skills={"python":get_valid_score("Python"),
                "MLFrameworks":get_valid_score("ML Frameworks"),
                "BackendJava":get_valid_score("Java/Spring"),
                "deployment":get_valid_score("docker,aws")
                }
        print("--------Projects and experience----------------")
        genaiProjects=check_yes_no("Do you have experience creating generative AI projects? (yes/no): ")
        intershipExperience=check_yes_no("Do you have experience with internships? (yes/no): ")
        #Checking scores and eligibility
        score=skills["python"]*4+skills["MLFrameworks"]*3+skills["BackendJava"]*3+skills["deployment"]*2
        if genaiProjects: score+=10
        if intershipExperience: score+=5
        #Tier Determination
        print("------Assessment Results----------------")
        if score>=45:
            print("Congratulations! You are eligible for Tier 1.")
        elif score>=30:
            print("Congratulations! You are eligible for Tier 2.")
        elif score>=15:
            print("Congratulations! You are eligible for Tier 3.")
        else:
            print("Sorry! You are not eligible for any tier.")
        print("--------Thank you for using the AI Startup Eligibility Bot----------------")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    eligibility_check()
